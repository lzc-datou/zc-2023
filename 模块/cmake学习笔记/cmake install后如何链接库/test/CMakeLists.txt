cmake_minimum_required(VERSION 3.0)
project(TEST)

set(CMAKE_INSTALL_PREFIX ${TEST_SOURCE_DIR}/install)

# 三步操作使得install后的可执行文件链接库成功
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)




add_executable(test test.cpp)

add_library(lib SHARED lib.cpp)

target_link_libraries(test lib)



install(TARGETS test lib  RUNTIME DESTINATION bin LIBRARY DESTINATION lib )
install(FILES lib.h DESTINATION include)



