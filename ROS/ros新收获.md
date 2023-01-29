# 新收获
> 2023.1.29

本文档主要记录我复习ros时的新收获

## 1.ROS常用命令
1. `roscore`   
启动核心 

2. `catkin_make`   
同时调用了`cmake..`和`make`命令构建项目

3. `source ./devel/setup.bash`   
加载由`catkin_make`生成的新的配置文件

4. `catkin_create_pkg 自定义ROS包名 依赖包`   
创建ros包，一般写成`catkin_create_pkg 自定义ROS包名 roscpp rospy std_msgs`

5. `rosrun 包名 可执行文件名`   
运行单个节点  
6. `roslaunch 包名 launch文件名`  
执行launch文件，可借助launch文件同时运行多个节点





## 2.ROS计算图
可以在终端使用`rqt_graph`命令查看当前运行的各ros节点之间的关系，详见文档[ros计算图](http://www.autolabor.com.cn/book/ROSTutorials/chapter1/15-ben-zhang-xiao-jie/153-rosji-suan-tu.html)
