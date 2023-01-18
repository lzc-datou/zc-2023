## 本文档讲解cmake的基本使用方法  
> 2023.1.13

关于cmake的简单使用方法，细心看完[视觉SLAM十四讲：从理论到实践 作者高翔](https://wwt.lanzoui.com/imuYxwsn9if) P57-61 页即可  
关于cmake的完整使用方法，建议阅读[Cmake官方文档](https://cmake.org/cmake/help/latest/)或者阅读[《cmake实践》](http://file.ncnynl.com/ros/CMake%20Practice.pdf)

> - **lzc建议**：建议看完后上B站找一个中小型的C++项目或者python项目进行实战，全程使用cmake管理项目，建议使用vscode作为编辑器，不需要使用IDE进行操作


### 对于《cmake实践》的注解

#### cmake项目“安装”的含义： 
具体实例见《cmake实践》P15
> 1. 含义类似于windows安装软件中“安装”的意思，就是只将可执行文件，库，说明文档等文件打包成一个文件夹（就类似于一个可运行的软件一样），从而与源代码和编译产生的中间文件分离开，形成一个可以直接给用户使用的软件。由于开发项目过程中会生成很多的文件，如源代码，中间文件，可执行文件，库文件等，而这其中源代码文件和中间文件在使用时是不需要的，所以可以利用cmake的install功能将使用时需要的文件全部打包形成一个新的文件夹从而方便使用。
> 2. 在CMakeLists.txt中通过install()命令指定`文件类型`， `打包的文件名（文件路径为相对于此CMakeLists.txt的相对路径）`（注意：目标文件和库文件只需要写名称即可，其他的均要相对路径）及其`打包的目标地址（此处为相对地址）`。相对地址是相对于CMAKE_INSTALL_PREFIX变量中的地址的（就是说如果相对地址为/doc/file，则最终地址为${CMAKE_INSTALL_PREFIX}/doc/file），可以在CMakeLists.txt中通过set()命令设定该变量的值（默认为/usr/local）


