# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build

# Include any dependencies generated for this target.
include bin/CMakeFiles/hello1.dir/depend.make

# Include the progress variables for this target.
include bin/CMakeFiles/hello1.dir/progress.make

# Include the compile flags for this target's objects.
include bin/CMakeFiles/hello1.dir/flags.make

bin/CMakeFiles/hello1.dir/main.c.o: bin/CMakeFiles/hello1.dir/flags.make
bin/CMakeFiles/hello1.dir/main.c.o: ../src/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object bin/CMakeFiles/hello1.dir/main.c.o"
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/hello1.dir/main.c.o   -c /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/src/main.c

bin/CMakeFiles/hello1.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/hello1.dir/main.c.i"
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/src/main.c > CMakeFiles/hello1.dir/main.c.i

bin/CMakeFiles/hello1.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/hello1.dir/main.c.s"
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/src/main.c -o CMakeFiles/hello1.dir/main.c.s

# Object files for target hello1
hello1_OBJECTS = \
"CMakeFiles/hello1.dir/main.c.o"

# External object files for target hello1
hello1_EXTERNAL_OBJECTS =

lib/libhello1.so: bin/CMakeFiles/hello1.dir/main.c.o
lib/libhello1.so: bin/CMakeFiles/hello1.dir/build.make
lib/libhello1.so: bin/CMakeFiles/hello1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library ../lib/libhello1.so"
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hello1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
bin/CMakeFiles/hello1.dir/build: lib/libhello1.so

.PHONY : bin/CMakeFiles/hello1.dir/build

bin/CMakeFiles/hello1.dir/clean:
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin && $(CMAKE_COMMAND) -P CMakeFiles/hello1.dir/cmake_clean.cmake
.PHONY : bin/CMakeFiles/hello1.dir/clean

bin/CMakeFiles/hello1.dir/depend:
	cd /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2 /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/src /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin /home/lzc/z/lzc-zc-2023/problem_and_solution/cmake/t2/build/bin/CMakeFiles/hello1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : bin/CMakeFiles/hello1.dir/depend

