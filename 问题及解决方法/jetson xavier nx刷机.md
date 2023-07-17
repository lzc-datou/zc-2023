# jetson xavier nx 刷机方法
> 2023.7.16

1. 使用[sdk-manager](https://developer.nvidia.com/sdk-manager)安装，安装方法见[官方文档](https://docs.nvidia.com/sdk-manager/index.html)。本次安装的版本为jetpack5.1.1

问题1：登录sdk-manager时报错`Your current region has an age policy that does not allow you to use the system.`  
解决方法：建议使用google账号登录

问题2：登录sdk-manager时报错`user is not authorized on nvidia developer server`  
解决方法：在NVIDA官方也登录一下你的google账号，[NVIDIA官方](https://developer.nvidia.com/zh-cn/developer-program)

2. sdk-manager与xaiver连接需要先使xaiver进入Recovery模式，操作顺序如下：
    1. 拔掉系统电源
    2. 短接载板上的`FC REC`引脚和`GND`引脚
    3. 插上系统电源通电，载板自动开机进入Recovery模式（此模式下风扇不转且HDMI无输出）
    4. 使用usb-microusb线连接笔记本电脑和xaiver，其中笔记本电脑接usb口，xaiver接microusb口
    5. 连接完成，在sdk-manager中按照步骤刷机即可。可以命令行输入命令`lsusb`查看笔记本电脑usb连接，如果有`NVIDIA Corp. APX`字样，说明连接成功
3. 配置所需要的环境
    1. 安装ROS，方法见[ros-noetic-install](http://wiki.ros.org/noetic/Installation/Ubuntu)
    2. 安装mavros ,方法见[mavros-install](https://docs.px4.io/main/zh/ros/mavros_installation.html)
    3. 安装torch和torchvision,方法见[pytorch for jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
    4. 安装yolov5依赖，进入yolov5包，使用命令`pip3 install -r requirement.txt`即可  

以上操作需要翻墙，如果clash翻墙不好使了，就去用协会的梯子。强调一遍：尽量不要给系统换源，国内源可能会出奇怪的错误无法解决。

  
