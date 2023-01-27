#pragma once

// 本头文件用于将需要用到的文件名进行宏定义以方便调用

// linux下宏定义字符串的拼接通过空格即可，其中CMAKE_INSTALL_PREFIX是在CMakeLists.txt添加的宏定义，使得C++程序可以使用cmake定义的变量

// 管理员文件
#define ADMIN_FILE CMAKE_INSTALL_PREFIX "/bin/document/admin.txt" // 拼接字符串

// 学生文件
#define STUDENT_FILE CMAKE_INSTALL_PREFIX "/bin/document/student.txt"

// 老师文件
#define TEACHER_FILE CMAKE_INSTALL_PREFIX "/bin/document/teacher.txt"

// 机房信息文件
#define COMPUTER_FILE CMAKE_INSTALL_PREFIX "/bin/document/computerRoom.txt"

// 订单文件
#define ORDER_FILE CMAKE_INSTALL_PREFIX "/bin/document/order.txt"