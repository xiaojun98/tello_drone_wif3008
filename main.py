import tello
from tello_control_ui import TelloUI


def main():

    drone = tello.Tello('', 8889, command_timeout=2.0, tello_ip='192.168.10.1')  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
