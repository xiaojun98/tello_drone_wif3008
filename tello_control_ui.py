from PIL import Image
from PIL import ImageTk
import tkinter as tki
from tkinter import Toplevel, Scale, filedialog
import threading
import datetime
import cv2
import os
import time
import platform

class TelloUI:
    """Wrapper class to enable the GUI."""

    def __init__(self,tello,outputpath):
        """
        Initial all the element of the GUI,support by Tkinter

        :param tello: class interacts with the Tello drone.

        Raises:
            RuntimeError: If the Tello rejects the attempt to enter command mode.
        """        

        self.tello = tello # videostream device
        self.outputPath = outputpath # the path that save pictures created by clicking the takeSnapshot button 
        self.frame = None  # frame read from h264decoder and used for pose recognition 
        self.thread = None # thread of the Tkinter mainloop
        self.stopEvent = None
        self.preplanRouteStopEvent = None
        
        # control variables
        self.distance = 20  # default distance for 'move' cmd
        self.degree = 30  # default degree for 'cw' or 'ccw' cmd

        # if the flag is TRUE,the auto-takeoff thread will stop waiting for the response from tello
        self.quit_waiting_flag = False
        
        # initialize the root window and image panel
        self.root = tki.Tk()
        self.panel = None

        # create buttons
        self.btn_preplan_stop = tki.Button(self.root, text="Stop Preplan",
                                       command=lambda: self.stopRunPreplanRoute())
        self.btn_preplan_stop.pack(side="bottom", fill="both",
                               expand="yes", padx=10, pady=5)

        self.btn_preplan = tki.Button(self.root, text="Run Preplan",
                                       command=lambda: self.__runCommand(self.startRunPreplanRoute) )
        self.btn_preplan.pack(side="bottom", fill="both",
                               expand="yes", padx=10, pady=5)

        self.btn_preplan = tki.Button(self.root, text="Load Preplan",
                                       command=lambda: self.__runCommand(self.loadPreplanRoute))
        self.btn_preplan.pack(side="bottom", fill="both",
                               expand="yes", padx=10, pady=5)
        
        self.btn_snapshot = tki.Button(self.root, text="Snapshot!",
                                       command=self.takeSnapshot)
        self.btn_snapshot.pack(side="bottom", fill="both",
                               expand="yes", padx=10, pady=5)

        self.btn_pause = tki.Button(self.root, text="Pause", relief="raised", command=self.pauseVideo)
        self.btn_pause.pack(side="bottom", fill="both",
                            expand="yes", padx=10, pady=5)

        self.btn_landing = tki.Button(
            self.root, text="Open Command Panel", relief="raised", command=lambda: self.__runCommand(self.openCmdWindow))
        self.btn_landing.pack(side="bottom", fill="both",
                              expand="yes", padx=10, pady=5)

        # init preplan route config
        self.route = []
        self.is_running_preplan = False
        
        # start a thread that constantly pools the video sensor for
        # the most recently read frame
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        # set a callback to handle when the window is closed
        self.root.wm_title("TELLO Controller")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

        # the sending_command will send command to tello every 5 seconds
        # self.sending_command_thread = threading.Thread(target = self._sendingCommand)
        self.tello.send_command('command')
    
    def videoLoop(self):
        """
        The mainloop thread of Tkinter 
        Raises:
            RuntimeError: To get around a RunTime error that Tkinter throws due to threading.
        """
        try:
            # start the thread that get GUI image and drwa skeleton 
            time.sleep(0.5)
            # self.sending_command_thread.start()
            while not self.stopEvent.is_set():                
                system = platform.system()

            # read the frame for GUI show
                self.frame = self.tello.read()
                if self.frame is None or self.frame.size == 0:
                    continue 
            
            # transfer the format from frame to image         
                image = Image.fromarray(self.frame)

            # we found compatibility problem between Tkinter,PIL and Macos,and it will 
            # sometimes result the very long preriod of the "ImageTk.PhotoImage" function,
            # so for Macos,we start a new thread to execute the _updateGUIImage function.
                if system =="Windows" or system =="Linux":                
                    self._updateGUIImage(image)

                else:
                    thread_tmp = threading.Thread(target=self._updateGUIImage,args=(image,))
                    thread_tmp.start()
                    time.sleep(0.03)                                                            
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

           
    def _updateGUIImage(self,image):
        """
        Main operation to initial the object of image,and update the GUI panel 
        """  
        image = ImageTk.PhotoImage(image)
        # if the panel none ,we need to initial it
        if self.panel is None:
            self.panel = tki.Label(image=image)
            self.panel.image = image
            self.panel.pack(side="left", padx=10, pady=10)
        # otherwise, simply update the panel
        else:
            self.panel.configure(image=image)
            self.panel.image = image

            
    def _sendingCommand(self):
        """
        start a while loop that sends 'command' to tello every 5 second
        """    

        while True:
            self.tello.send_command('command')        
            time.sleep(5)

    def _setQuitWaitingFlag(self):  
        """
        set the variable as TRUE,it will stop computer waiting for response from tello  
        """       
        self.quit_waiting_flag = True        
   
    def openCmdWindow(self):
        """
        open the cmd window and initial all the button and text
        """        
        panel = Toplevel(self.root)
        panel.wm_title("Command Panel")

        # create text input entry
        text0 = tki.Label(panel,
                          text='This Controller map keyboard inputs to Tello control commands\n'
                               'Adjust the trackbar to reset distance and degree parameter',
                          font='Helvetica 10 bold'
                          )
        text0.pack(side='top')

        text1 = tki.Label(panel, text=
                          'W - Move Tello Up\t\t\tArrow Up - Move Tello Forward\n'
                          'S - Move Tello Down\t\t\tArrow Down - Move Tello Backward\n'
                          'A - Rotate Tello Counter-Clockwise\tArrow Left - Move Tello Left\n'
                          'D - Rotate Tello Clockwise\t\tArrow Right - Move Tello Right',
                          justify="left")
        text1.pack(side="top")

        self.btn_landing = tki.Button(
            panel, text="Land", relief="raised", command=lambda: self.__runCommand(self.telloLanding))
        self.btn_landing.pack(side="bottom", fill="both",
                              expand="yes", padx=10, pady=5)

        self.btn_takeoff = tki.Button(
            panel, text="Takeoff", relief="raised", command=self.telloTakeOff)
        self.btn_takeoff.pack(side="bottom", fill="both",
                              expand="yes", padx=10, pady=5)

        # binding arrow keys to drone control
        self.tmp_f = tki.Frame(panel, width=100, height=2)
        self.tmp_f.bind('<KeyPress-w>', lambda e: self.__runCommand(self.on_keypress_w))
        self.tmp_f.bind('<KeyPress-s>', lambda e: self.__runCommand(self.on_keypress_s))
        self.tmp_f.bind('<KeyPress-a>', lambda e: self.__runCommand(self.on_keypress_a))
        self.tmp_f.bind('<KeyPress-d>', lambda e: self.__runCommand(self.on_keypress_d))
        self.tmp_f.bind('<KeyPress-Up>', lambda e: self.__runCommand(self.on_keypress_up))
        self.tmp_f.bind('<KeyPress-Down>', lambda e: self.__runCommand(self.on_keypress_down))
        self.tmp_f.bind('<KeyPress-Left>', lambda e: self.__runCommand(self.on_keypress_left))
        self.tmp_f.bind('<KeyPress-Right>', lambda e: self.__runCommand(self.on_keypress_right))
        self.tmp_f.pack(side="bottom")
        self.tmp_f.focus_set()

        self.btn_landing = tki.Button(
            panel, text="Flip", relief="raised", command=self.openFlipWindow)
        self.btn_landing.pack(side="bottom", fill="both",
                              expand="yes", padx=10, pady=5)

        self.distance_bar = Scale(panel, from_=2, to=500, tickinterval=1, digits=3, label='Distance(cm)',
                                  resolution=1)
        self.distance_bar.set(20)
        self.distance_bar.pack(side="left")

        self.btn_distance = tki.Button(panel, text="Reset Distance", relief="raised",
                                       command=self.updateDistancebar,
                                       )
        self.btn_distance.pack(side="left", fill="both",
                               expand="yes", padx=10, pady=5)

        self.degree_bar = Scale(panel, from_=1, to=360, tickinterval=10, label='Degree')
        self.degree_bar.set(30)
        self.degree_bar.pack(side="right")

        self.btn_distance = tki.Button(panel, text="Reset Degree", relief="raised", command=self.updateDegreebar)
        self.btn_distance.pack(side="right", fill="both",
                               expand="yes", padx=10, pady=5)

    def openFlipWindow(self):
        """
        open the flip window and initial all the button and text
        """
        
        panel = Toplevel(self.root)
        panel.wm_title("Gesture Recognition")

        self.btn_flipl = tki.Button(
            panel, text="Flip Left", relief="raised", command=self.telloFlip_l)
        self.btn_flipl.pack(side="bottom", fill="both",
                            expand="yes", padx=10, pady=5)

        self.btn_flipr = tki.Button(
            panel, text="Flip Right", relief="raised", command=self.telloFlip_r)
        self.btn_flipr.pack(side="bottom", fill="both",
                            expand="yes", padx=10, pady=5)

        self.btn_flipf = tki.Button(
            panel, text="Flip Forward", relief="raised", command=self.telloFlip_f)
        self.btn_flipf.pack(side="bottom", fill="both",
                            expand="yes", padx=10, pady=5)

        self.btn_flipb = tki.Button(
            panel, text="Flip Backward", relief="raised", command=self.telloFlip_b)
        self.btn_flipb.pack(side="bottom", fill="both",
                            expand="yes", padx=10, pady=5)
       
    def takeSnapshot(self):
        """
        save the current frame of the video as a jpg file and put it into outputpath
        """

        # grab the current timestamp and use it to construct the filename
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))

        p = os.path.sep.join((self.outputPath, filename))

        # save the file
        cv2.imwrite(p, cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR))
        print("[INFO] saved {}".format(filename))


    def pauseVideo(self):
        """
        Toggle the freeze/unfreze of video
        """
        if self.btn_pause.config('relief')[-1] == 'sunken':
            self.btn_pause.config(relief="raised")
            self.tello.video_freeze(False)
        else:
            self.btn_pause.config(relief="sunken")
            self.tello.video_freeze(True)

    def telloTakeOff(self):
        return self.tello.takeoff()                

    def telloLanding(self):
        return self.tello.land()

    def telloFlip_l(self):
        return self.tello.flip('l')

    def telloFlip_r(self):
        return self.tello.flip('r')

    def telloFlip_f(self):
        return self.tello.flip('f')

    def telloFlip_b(self):
        return self.tello.flip('b')
    
    def telloFlip(self, direction):
        return self.tello.flip(direction)

    def telloCW(self, degree):
        return self.tello.rotate_cw(degree)

    def telloCCW(self, degree):
        return self.tello.rotate_ccw(degree)

    def telloMoveForward(self, distance):
        return self.tello.move_forward(distance)

    def telloMoveBackward(self, distance):
        return self.tello.move_backward(distance)

    def telloMoveLeft(self, distance):
        return self.tello.move_left(distance)

    def telloMoveRight(self, distance):
        return self.tello.move_right(distance)

    def telloUp(self, dist):
        return self.tello.move_up(dist)

    def telloDown(self, dist):
        return self.tello.move_down(dist)

    def updateTrackBar(self):
        self.my_tello_hand.setThr(self.hand_thr_bar.get())

    def updateDistancebar(self):
        self.distance = self.distance_bar.get()
        print('reset distance to %d cm' % self.distance)

    def updateDegreebar(self):
        self.degree = self.degree_bar.get()
        print('reset degree to %d' % self.degree)

    def on_keypress_w(self, event):
        print("up %d cm" % self.distance)
        self.telloUp(self.distance)

    def on_keypress_s(self, event):
        print("down %d cm" % self.distance)
        self.telloDown(self.distance)

    def on_keypress_a(self, event):
        print("ccw %d degree" % self.degree)
        self.tello.rotate_ccw(self.degree)

    def on_keypress_d(self, event):
        print("cw %d degree" % self.degree)
        self.tello.rotate_cw(self.degree)

    def on_keypress_up(self, event):
        print("forward %d cm" % self.distance)
        self.telloMoveForward(self.distance)

    def on_keypress_down(self, event):
        print("backward %d cm" % self.distance)
        self.telloMoveBackward(self.distance)

    def on_keypress_left(self, event):
        print("left %d cm" % self.distance)
        self.telloMoveLeft(self.distance)

    def on_keypress_right(self, event):
        print("right %d cm" % self.distance)
        self.telloMoveRight(self.distance)

    def on_keypress_enter(self, event):
        if self.frame is not None:
            self.registerFace()
        self.tmp_f.focus_set()

    def onClose(self):
        """
        set the stop event, cleanup the camera, and allow the rest of
        
        the quit process to continue
        """
        print("[INFO] closing...")
        self.stopEvent.set()
        del self.tello
        self.root.quit()
    
    def loadPreplanRoute(self):
        # todo:
        filepath = filedialog.askopenfilename(initialdir = "./",title = "Select preplan route file",filetypes = (("text files","*.txt"),("all files","*.*")))
        print(filepath)
        f = open(filepath, "r")
        raw = f.read()
        commands = raw.split('\n')
        self.route = commands
        f.close()
    
    def startRunPreplanRoute(self):
        self.preplanRouteStopEvent = threading.Event()
        self.preplanRouteThread = threading.Thread(target=self.runPreplanRoute, args=())
        self.preplanRouteThread.start()
    
    def stopRunPreplanRoute(self):
        if self.preplanRouteStopEvent != None and self.preplanRouteThread.isAlive():
            self.preplanRouteStopEvent.set()

    def runPreplanRoute(self):
        # todo:
        if self.is_running_preplan:
            print('[runPreplanRoute] Existing route is running...')
            return
        if self.route == None or len(self.route) == 0:
            print('[runPreplanRoute] No route is loaded')
            return
        self.is_running_preplan = True
        while len(self.route) > 0 and not self.preplanRouteStopEvent.is_set():
            self.__command2method(self.route.pop(0))
        print('runPreplanRoute done')
        print(len(self.route))
        self.is_running_preplan = False
    
    def __runCommand(self, command, *args):
        if self.is_running_preplan:
            print('* action abort, preplan is running...')
        else:
            command(*args)
    
    def __command2method(self, command):
        params = command.split(' ')
        switcher = {
            "up": self.telloUp,
            "down": self.telloDown,
            "ccw": self.telloCCW,
            "cw": self.telloCW,
            "forward": self.telloMoveForward,
            "backward": self.telloMoveBackward,
            "left": self.telloMoveLeft,
            "right": self.telloMoveRight,
            "takeoff": self.telloTakeOff,
            "land": self.telloLanding,
            # "command": self.send_command,
            "flip": self.telloFlip
        }
        # Get the function from switcher dictionary
        func = switcher.get(params[0], lambda: "Invalid command")
        # Execute the function
        if params[0] == 'command':
            self.tello.send_command('command')
        elif params[0] == 'takeoff' or params[0] == 'land':
            func()
        elif params[0] == 'flip':
            func(params[1])
        else:
            func(int(params[1]))