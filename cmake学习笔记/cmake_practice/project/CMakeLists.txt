cmake_minimum_required(VERSION 3.0)

project(COMPUTER_RESERVATION) #机房预约系统

# # 编译时排除测试目录test
# set(EXCLUDE_FROM_ALL test)
# set(BINARY_DIR bin)



message(STATUS "binary dir is "${COMPUTER_RESERVATION_BINARY_DIR}/bin)
message(STATUS "source dir is "${COMPUTER_RESERVATION_SOURCE_DIR}/src)



# 设置安装的相对路径前缀
set(CMAKE_INSTALL_PREFIX ${COMPUTER_RESERVATION_SOURCE_DIR}/install)

# 为C++程序添加宏变量，使得C++程序可以使用cmake定义的变量，主要是使得C++程序能获得安装路径
add_definitions(-DCMAKE_INSTALL_PREFIX="${CMAKE_INSTALL_PREFIX}")

# 设置安装后可执行文件的RPATH，用于解决安装后可执行文件链接库失败的问题
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)


add_subdirectory(src bin) 


#进行安装   安装可以统一在工程目录下的主CMakeLists.txt下写

# 安装头文件   头文件需要标明相对路径

# install(FILES include/Student.h DESTINATION install/include)
# install(FILES include/Identity.h DESTINATION install/include)
# install(FILES include/Teacher.h DESTINATION install/include)
# install(FILES include/Manager.h DESTINATION install/include)

# 设置头文件名称变量
# set(head 
#     include/Student.h 
#     include/Identity.h 
#     include/Teacher.h 
#     include/Manager.h
#     include/globalFile.h
#     )

# install(FILES ${head} DESTINATION install/include)
# 直接安装整个目录来安装头文件
install(DIRECTORY "./include/" DESTINATION include)

# 安装记录文件
# set(document
#     src/document/student.txt
#     src/document/teacher.txt
#     src/document/admin.txt
#     src/document/order.txt
#     src/document/computerRoom.txt
# )
# install(FILES ${document} DESTINATION bin/document)

install(DIRECTORY "./src/document/" DESTINATION bin/document)

# 安装目标二进制和库文件

# install(TARGETS  main student teacher manager RUNTIME DESTINATION install/bin LIBRARY DESTINATION install/lib)
# 设置库名变量   注意：上下层CMakeLists.txt中定义的变量不能互用
set(lib student teacher manager orderFile)
install(TARGETS  main ${lib} RUNTIME DESTINATION bin LIBRARY DESTINATION lib)
# install(TARGETS  main stm RUNTIME DESTINATION install/bin LIBRARY DESTINATION install/lib)

