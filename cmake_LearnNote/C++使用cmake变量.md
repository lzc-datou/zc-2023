# C++使用cmake变量
> 2023.1.26

本文档主要用于讲解如何在C++程序中使用CMakeLists.txt中的变量。最初需求是让C++程序获取到安装之后的路径，即获取CMAKE_INSTALL_PREFIX变量

阅读的文章
1. [C语言中如何使用宏连接多个字符串](https://blog.csdn.net/leon1741/article/details/78149881)
2. [Cmake 两种方式设置变量及源码中使用](https://blog.csdn.net/lanmolei814/article/details/120269149)

注意：使用cmake管理C++工程时，C++程序中的相对路径都是相对于make命令所在目录的，而不是相对于生成的可执行文件的。

可以通过add_definitions()命令使得C++程序中可以使用CMakeLists.txt中定义的变量（主要是使用定义的路径）

**add_definitions()使用方法**:  

例子：`add_definitions(-DCMAKE_INSTALL_PREFIX="${CMAKE_INSTALL_PREFIX}")`

`-D`前缀表示宏定义`define`，`-D`后面是宏变量名称，使用`=`进行赋值，注意：在CMakeLists.txt中在`""`中也可以通过`${}`来使用变量。由于我们需要的路径是字符串，而${CMAKE_INSTALL_PREFIX}不是字符串（是没有引号的路径），所以需要给它加上`""`变成字符串再赋值给宏变量，这样再C++程序中就可以使用宏变量`CMAKE_INSTALL_PREFIX`来获取安装路径了。linux下C++通过空格即可拼接宏变量字符串，详见文章1