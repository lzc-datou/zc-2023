
# message(STATUS "this is binary dir "${HELLO_BINARY_DIR})
# message(STATUS "this is source dir "${HELLO_SOURCE_DIR})



# message(STATUS "this is exe dir " ${EXECUTABLE_OUTPUT_PATH})
# message(STATUS "this is lib dir "${LIBRARY_OUTPUT_PATH})
add_executable(hello main.c)
add_library(hello1 SHARED main.c)
set(EXECUTABLE_OUTPUT_PATH ${HELLO_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${HELLO_BINARY_DIR}/lib)
# add_library(lib SHARED main.c)

# EXECUTABLE_OUTPUT_PATH变量 设置可执行文件存放位置
# LIBRARY_OUTPUT_PATH变量 设置库存放位置
# set(EXECUTABLE_OUTPUT_PATH ${HELLO_BINARY_DIR}/bin)
# set(LIBRARY_OUTPUT_PATH ${HELLO_BINARY_DIR}/lib)