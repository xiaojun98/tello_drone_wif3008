# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/thechee/Developer/miniconda3/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/thechee/Developer/miniconda3/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build

# Include any dependencies generated for this target.
include CMakeFiles/h264decoder.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/h264decoder.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/h264decoder.dir/flags.make

CMakeFiles/h264decoder.dir/h264decoder.cpp.o: CMakeFiles/h264decoder.dir/flags.make
CMakeFiles/h264decoder.dir/h264decoder.cpp.o: ../h264decoder.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/h264decoder.dir/h264decoder.cpp.o"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/h264decoder.dir/h264decoder.cpp.o -c /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder.cpp

CMakeFiles/h264decoder.dir/h264decoder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/h264decoder.dir/h264decoder.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder.cpp > CMakeFiles/h264decoder.dir/h264decoder.cpp.i

CMakeFiles/h264decoder.dir/h264decoder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/h264decoder.dir/h264decoder.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder.cpp -o CMakeFiles/h264decoder.dir/h264decoder.cpp.s

CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o: CMakeFiles/h264decoder.dir/flags.make
CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o: ../h264decoder_python.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o -c /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder_python.cpp

CMakeFiles/h264decoder.dir/h264decoder_python.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/h264decoder.dir/h264decoder_python.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder_python.cpp > CMakeFiles/h264decoder.dir/h264decoder_python.cpp.i

CMakeFiles/h264decoder.dir/h264decoder_python.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/h264decoder.dir/h264decoder_python.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/h264decoder_python.cpp -o CMakeFiles/h264decoder.dir/h264decoder_python.cpp.s

# Object files for target h264decoder
h264decoder_OBJECTS = \
"CMakeFiles/h264decoder.dir/h264decoder.cpp.o" \
"CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o"

# External object files for target h264decoder
h264decoder_EXTERNAL_OBJECTS =

libh264decoder.so: CMakeFiles/h264decoder.dir/h264decoder.cpp.o
libh264decoder.so: CMakeFiles/h264decoder.dir/h264decoder_python.cpp.o
libh264decoder.so: CMakeFiles/h264decoder.dir/build.make
libh264decoder.so: /usr/lib/x86_64-linux-gnu/libboost_python38.so.1.71.0
libh264decoder.so: /usr/lib/x86_64-linux-gnu/libpython2.7.so
libh264decoder.so: CMakeFiles/h264decoder.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared library libh264decoder.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/h264decoder.dir/link.txt --verbose=$(VERBOSE)
	/home/thechee/Developer/miniconda3/lib/python3.8/site-packages/cmake/data/bin/cmake -E create_symlink /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build/libh264decoder.so /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/libh264decoder.so

# Rule to build all files generated by this target.
CMakeFiles/h264decoder.dir/build: libh264decoder.so

.PHONY : CMakeFiles/h264decoder.dir/build

CMakeFiles/h264decoder.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/h264decoder.dir/cmake_clean.cmake
.PHONY : CMakeFiles/h264decoder.dir/clean

CMakeFiles/h264decoder.dir/depend:
	cd /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build /home/thechee/Documents/Acedemic/S1_21/WIF3008/Assignment/DroneAssignment/h264decoder/build/CMakeFiles/h264decoder.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/h264decoder.dir/depend
