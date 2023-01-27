
# 生成目标二进制
add_executable(main computerReservation.cpp)




# 生成库文件
add_library(student SHARED Student.cpp)
add_library(teacher SHARED Teacher.cpp)
add_library(manager SHARED Manager.cpp)
add_library(orderFile SHARED orderFile.cpp)
# set(libcpp Student.cpp Teacher.cpp Manager.cpp)
# add_library(stm SHARED ${libcpp})



# 设置库名变量
set(lib student teacher  manager orderFile)
# 为目标二进制链接库文件
target_link_libraries(main ${lib})

# target_link_libraries(main student)   
# target_link_libraries(main teacher)     
# target_link_libraries(main manager)                   



# 设置生成的可执行文件路径

set(EXECUTABLE_OUTPUT_PATH ${COMPUTER_RESERVATION_BINARY_DIR}/bin)
# 设置生成的库文件路径
set(LIBRARY_OUTPUT_PATH ${COMPUTER_RESERVATION_BINARY_DIR}/lib)

