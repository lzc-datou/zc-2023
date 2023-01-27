## 本文档讲解cmake的基本使用方法  
> 2023.1.18

关于cmake的简单使用方法，细心看完[视觉SLAM十四讲：从理论到实践 作者高翔](https://wwt.lanzoui.com/imuYxwsn9if) P57-61 页即可  
关于cmake的完整使用方法，建议阅读[Cmake官方文档](https://cmake.org/cmake/help/latest/)或者阅读[《cmake实践》](http://file.ncnynl.com/ros/CMake%20Practice.pdf)

> - **lzc建议**：建议看完后上B站找一个中小型的C++项目或者python项目进行实战，全程使用cmake管理项目，建议使用vscode作为编辑器，不需要使用IDE进行操作

- `t1 - t4`文件夹是我阅读《cmake实践》时跟着做的实践内容  
- `cmake_practice`文件夹是我用`cmake`管理`B站传智教育C++课程`中`机房预约系统项目`的实践。充分利用了所学的`cmake`知识，大大提高了我对`cmake`的使用熟练度。
### 对于《cmake实践》的注解

#### cmake项目“安装”的含义： 
具体实例见《cmake实践》P15
> 1. 含义类似于windows安装软件中“安装”的意思，就是只将可执行文件，库，说明文档等文件打包成一个文件夹（就类似于一个可运行的软件一样），从而与源代码和编译产生的中间文件分离开，形成一个可以直接给用户使用的软件。由于开发项目过程中会生成很多的文件，如源代码，中间文件，可执行文件，库文件等，而这其中源代码文件和中间文件在使用时是不需要的，所以可以利用cmake的install功能将使用时需要的文件全部打包形成一个新的文件夹从而方便使用。
> 2. 在CMakeLists.txt中通过install()命令指定`文件类型`， `打包的文件名（文件路径为相对于此CMakeLists.txt的相对路径）`（注意：目标文件和库文件只需要写名称即可，其他的均要相对路径）及其`打包的目标地址（此处为相对地址）`。相对地址是相对于CMAKE_INSTALL_PREFIX变量中的地址的（就是说如果相对地址为/doc/file，则最终地址为${CMAKE_INSTALL_PREFIX}/doc/file），可以在项目目录的CMakeLists.txt中通过set()命令设定该变量的值（默认为/usr/local）。注意：其他子目录下设置该变量无效


注意：《cmake实践》这本书看到第30页即可，后面的属于扩展内容。

**cmake_lzc总结**：
> 常用指令  
> - `cmake_minimum_required(VERSION 3.0)`要求cmake最小版本为3.0
> - `project(项目名称)` 定义项目名称
> - `message(STATUS "内容")` 在命令行输出前缀为--的内容
> - `add_subdirectory(src bin)` 添加工程目录下的子目录  第一个为源码目录，第二个为目标二进制目录
> - `add_executable(hello hello.c)`生成可执行文件  第一个为可执行文件名，第二个为源码文件名
> - `add_library(hello1 SHARED hello.c)`生成库文件 第一个为库名xxx，生成的库文件名为libxxx.so（动态库）或者libxxx.a（静态库）。 第二个为源码文件名。默认生成静态库，加SHARED选项后生成动态库
> - `add_definitions(-DVAL="变量内容")`在CMakeLists.txt中为C++程序定义宏变量，`-D`前缀表示宏定义`define`的意思，`VAL`为宏变量名称，`=`赋值，后面跟着的是宏变量的内容
> - `set(变量名 变量值)`设置变量值  注意：上下层目录CMakeLists.txt中定义的变量不能互相使用，即任何CMakeLists.txt中定义的变量只能给自己使用，不能给父目录或子目录中的其他CMakeLists.txt使用。如果两个CMakeLists.txt中需要使用相同的变量，那么只能分别定义
> - `install(FILES|PROGRAMS|TARGETS|DIRECTORY 文件名 DESTINATION 目标路径)`安装相应文件到相应目录 FILES表示一般文件 PROGRAMS表示脚本文件等（如.sh .bash文件），TARGETS表示目标文件（如可执行文件和库文件) DIRECTORY表示目录或整个目录下的文件，如果文件夹路径写成`home/lzc/目录`,则安装过去时会含有`目录`本身，如果文件夹路径写成`home/lzc/目录/`，则安装过去的是目录下的所有文件，不包括目录本身。DESTNATION后的目标路径是相对于变量CMAKE_INSTALL_PREFIX的路径。即该目标路径的前缀为变量CMAKE_INSTALL_PREFIX。
> - `include_directories(/home/lzc/cmake/include)`添加第三方头文件目录，如/home/lzc/cmake/include
> - `link_directories(/home/lzc/cmake/lib)` 添加第三方库文件目录，如/home/lzc/cmake/lib
> - `target_link_libraries(hello libhello.so)` 将库文件链接到可执行文件。第一个参数为可执行文件名称，第二个参数为库文件名称。注意：要先add_executable生成可执行文件后才能进行target_link_libraries链接
>常用变量
> - `EXECUTABLE_OUTPUT_PATH` 设置生成的可执行文件存放位置  
> - `LIBRARY_OUTPUT_PATH` 设置生成的库文件存放位置  
> - `CMAKE_INSTALL_PREFIX` 安装时的前置路径，其他相对路径均是以此为前缀  
> 下面两个变量常用于更改`EXECUTABLE_OUTPUT_PATH`和`LIBRARY_OUTPUT_PATH`的值,且需要在源代码目录下的CMakeLists.txt中修改才有用
> - `项目名称_BINARY_DIR` 项目二进制目录，为使用make的目录
> - `项目名称_SOURCE_DIR` 项目源码目录，为`cmake 目标路径`命令中的目标路径目录

注意：使用cmake管理C++工程时，C++程序中的相对路径都是相对于make命令所在目录的，而不是相对于生成的可执行文件的。

可以通过add_definitions()命令使得C++程序中可以使用CMakeLists.txt中定义的变量（主要是使用定义的路径）


