# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

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
CMAKE_COMMAND = /home/lzc/.local/lib/python3.9/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/lzc/.local/lib/python3.9/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build

# Include any dependencies generated for this target.
include bin/CMakeFiles/main.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include bin/CMakeFiles/main.dir/compiler_depend.make

# Include the progress variables for this target.
include bin/CMakeFiles/main.dir/progress.make

# Include the compile flags for this target's objects.
include bin/CMakeFiles/main.dir/flags.make

bin/CMakeFiles/main.dir/computerReservation.cpp.o: bin/CMakeFiles/main.dir/flags.make
bin/CMakeFiles/main.dir/computerReservation.cpp.o: /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/src/computerReservation.cpp
bin/CMakeFiles/main.dir/computerReservation.cpp.o: bin/CMakeFiles/main.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object bin/CMakeFiles/main.dir/computerReservation.cpp.o"
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT bin/CMakeFiles/main.dir/computerReservation.cpp.o -MF CMakeFiles/main.dir/computerReservation.cpp.o.d -o CMakeFiles/main.dir/computerReservation.cpp.o -c /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/src/computerReservation.cpp

bin/CMakeFiles/main.dir/computerReservation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/main.dir/computerReservation.cpp.i"
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/src/computerReservation.cpp > CMakeFiles/main.dir/computerReservation.cpp.i

bin/CMakeFiles/main.dir/computerReservation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/main.dir/computerReservation.cpp.s"
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/src/computerReservation.cpp -o CMakeFiles/main.dir/computerReservation.cpp.s

# Object files for target main
main_OBJECTS = \
"CMakeFiles/main.dir/computerReservation.cpp.o"

# External object files for target main
main_EXTERNAL_OBJECTS =

bin/main: bin/CMakeFiles/main.dir/computerReservation.cpp.o
bin/main: bin/CMakeFiles/main.dir/build.make
bin/main: lib/libstudent.so
bin/main: lib/libteacher.so
bin/main: lib/libmanager.so
bin/main: lib/liborderFile.so
bin/main: bin/CMakeFiles/main.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable main"
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/main.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
bin/CMakeFiles/main.dir/build: bin/main
.PHONY : bin/CMakeFiles/main.dir/build

bin/CMakeFiles/main.dir/clean:
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin && $(CMAKE_COMMAND) -P CMakeFiles/main.dir/cmake_clean.cmake
.PHONY : bin/CMakeFiles/main.dir/clean

bin/CMakeFiles/main.dir/depend:
	cd /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/src /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin /home/lzc/lzc-doc/模块/cmake学习笔记/cmake_practice/project/build/bin/CMakeFiles/main.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : bin/CMakeFiles/main.dir/depend

