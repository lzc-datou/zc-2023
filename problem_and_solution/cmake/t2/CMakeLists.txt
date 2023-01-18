cmake_minimum_required(VERSION 3.16)
PROJECT (HELLO)
# message(STATUS "this is binary dir "${HELLO_BINARY_DIR})
# message(STATUS "this is source dir "${HELLO_SOURCE_DIR})

set(CMAKE_INSTALL_PREFIX /home/lzc/t2) # 设置安装路径，其他路径都是此路径的相对路径
add_subdirectory(src bin)

install(FILES COPYRIGHT README DESTINATION file)
install(PROGRAMS runhello.sh  DESTINATION bin)
install(TARGETS hello  DESTINATION binRun)
install(DIRECTORY doc/ DESTINATION file)


