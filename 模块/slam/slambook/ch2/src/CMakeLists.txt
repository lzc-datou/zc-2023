message(STATUS "This is BINARY dir" ${HelloSLAM_BINARY_DIR})
message(STATUS "This is SOURCE dir" ${HelloSLAM_SOURCE_DIR})
add_library(hellolib SHARED libhelloSLAM.cpp)

add_executable( hello helloSLAM.cpp libhelloSLAM.cpp)
add_executable(uselibhello uselibhello.cpp)



target_link_libraries(uselibhello hellolib)

