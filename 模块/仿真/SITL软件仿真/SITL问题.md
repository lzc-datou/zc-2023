# SITL小问题
> 2023.7.24

### 1. urdf文件中的origin标签含义
见文章解释  
1. [ROS 的 urdf 中 link 和 joint 的子标签中 origin 的含义](https://blog.csdn.net/m0_60346726/article/details/128600473)
2. [urdf 文件 joint origin标签 rpy变换理解！](https://blog.csdn.net/qq_42226250/article/details/110861462?ydreferer=aHR0cHM6Ly93d3cuYmluZy5jb20v)

### 2. sdf文件基本标签讲解

### 3. 模型的sdf文件中添加传感器插件

### 4. blender建模并导入gazebo

### 5. gazebo环境变量设置

### 6. 仿真图像传给yolov5识别

### 7. sim_vehicle.py连接ROS

### 8. sim_vehicle.py连接mavros和QGC

`cd /home/lzc/ardupilot/Tools/autotest;sim_vehicle.py -v ArduPlane -f gazebo-zephyr --out 127.0.0.1:14551
`
### 9. sim_vehicle.py连接gazebo模型

### 10. gazebo连接ROS
`cd /home/lzc/ardupilot_gazebo;gazebo --verbose -s libgazebo_ros_api_plugin.so ./worlds/target.world`