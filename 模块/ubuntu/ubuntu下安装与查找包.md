# 安装与查找

> 2023.1.29

## 1.安装的三种方式

1. `dpkg -i xxx.deb` 采用dpkg进行安装
2. `sudo apt install 包名` 采用apt进行安装
3. `sudo pip install 包名` 采用pip安装python包注意：python2对应 `pip`，python3对应 `pip3`
4. `sudo pip install -r requirements.txt` 按照txt文件内容下载包，用于同时下载多个包的情况

## 2.查找包的方法

使用该工具安装的包只能由该工具找到并删除，所以找包之前我们需要确定一下这个包是用哪个工具安装的，然后使用对应工具去查找。

1. `dpkg`查找方法：`dpkg --get-selections | grep 包名`
2. `apt`查找方法：`sudo apt list | grep 包名`或者 `apt search 包名`
3. `pip`查找方法：`pip show 包名`
4. `pip3`查找方法：`pip3 show 包名`

## 3.安装ros包的方法
可以使用apt直接安装，也可以使用ros的包管理器rosdep安装
1. 使用 apt 安装 ` sudo apt install ros-noetic-包名` 其中`noetic`是你的ros版本名称，此位置应根据你自己的版本填写，可以通过命令`rosparam get /rosdistro`获取你的ros版本名称。
2. 使用rosdep安装（有些时候可能找不到需要的包），命令`sudo rosdep install 包名`