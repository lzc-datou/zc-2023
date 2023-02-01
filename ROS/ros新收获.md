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

## 3.回调函数
- [C 语言回调函数详解](https://www.runoob.com/w3cnote/c-callback-function.html)

- [有关ros::spin()和ros::spinonce()若干感受](https://www.cnblogs.com/agvcfy/p/9314682.html#:~:text=ros%3A%3Aspin,%28%29%EF%BC%8C%E7%94%A8%E4%BA%8E%E5%9B%9E%E8%B0%83%E5%87%BD%E6%95%B0%E7%9A%84%E5%A4%84%E7%90%86%EF%BC%8C%E5%B9%B6%E4%B8%94%E6%89%A7%E8%A1%8C%E8%BF%99%E6%AE%B5%E7%A8%8B%E5%BA%8F%E5%B0%B1%E4%BC%9A%E8%BF%9B%E5%85%A5%E6%97%A0%E9%99%90%E6%AC%A1%E5%BE%AA%E7%8E%AF%EF%BC%88%E6%B6%88%E6%81%AF%E6%9D%A5%E4%B8%80%E6%AC%A1%EF%BC%8C%E5%9B%9E%E8%B0%83%E5%87%BD%E6%95%B0%E5%B0%B1%E4%BC%9A%E7%AB%8B%E5%8D%B3%E5%A4%84%E7%90%86%E4%B8%80%E6%AC%A1%EF%BC%8C%E6%B2%A1%E6%9C%89%E9%98%85%E8%AF%BB%E5%88%B0%E6%B6%88%E6%81%AF%E7%9A%84%E6%97%B6%E5%80%99%EF%BC%8Cspin%E5%BE%AA%E7%8E%AF%E5%B0%86%E4%BC%9A%E5%A0%B5%E5%A1%9E%EF%BC%8C%E4%B8%8D%E4%BC%9A%E5%8D%A0%E7%94%A8CPU%E8%B5%84%E6%BA%90%EF%BC%89%EF%BC%8C%E7%9B%B4%E5%88%B0ctrl_c%E6%9D%A5%E4%B8%B4%EF%BC%8C%E6%88%96%E8%80%85%E5%85%B6%E4%BB%96%E7%BB%88%E6%AD%A2%E4%BF%A1%E5%8F%B7%E6%9D%A5%E4%B8%B4%E3%80%82%20%E4%B8%80%E8%88%AC%E6%89%80%E6%9C%89%E7%9A%84%E7%A8%8B%E5%BA%8F%E9%83%BD%E5%86%99%E5%9C%A8%E8%BF%99%E6%AE%B5%E8%AF%AD%E5%8F%A5%E4%B9%8B%E5%89%8D%EF%BC%8C%E5%9B%A0%E4%B8%BA%E5%85%B6%E4%B9%8B%E5%90%8E%E7%9A%84%E7%A8%8B%E5%BA%8F%EF%BC%8C%E4%B8%8D%E4%BC%9A%E8%A2%AB%E6%89%A7%E8%A1%8C%E3%80%82)


## 4.参数服务器

相关语法见文章[参数服务器](http://www.autolabor.com.cn/book/ROSTutorials/di-2-zhang-ros-jia-gou-she-ji/24-can-shu-fu-wu-qi/233-can-shu-caozuo-b-python.html)  

参数服务器使用方式：运行一次相应的python文件即可
可以在launch文件中添加一行命令来运行参数服务器的py文件，运行一次后所有参数就都设置完成了，成为了ros系统中的全局变量，可以通过`rospy.get_param("变量名")`来获取

## 5.ROS常用命令

### 5.1命令行获取话题发布的消息内容  
假设话题名称为topic_name,消息类型为msg_type
```
rostopic list
rostopic type topic_name
rosmsg show msg_type

```

1. `rostopic list`  列出当前运行的所有话题名称
2. `rostopic type 话题名称`   打印对应话题名称的消息类型
3. `rosmsg show 消息类型 ` 打印该消息类型具体所含内容（与打印出结构体变量内部结构类似），其中`rosmsg show` 与`rosmsg info`作用相同

将`rostopic`命令换成`rosservice`，`rosmsg`命令换成`rossrv`，按照上述流程，也可以获取到相应服务的消息类型与具体内容  
流程如下:  

```
//假如服务名称为service_name，消息类型为srv_type
rosservice list
rosservice type service_name
rossrv show srv_type

```

## 6. 日志输出函数
```
rospy.logdebug("hello,debug")  #不会输出
rospy.loginfo("hello,info")  #默认白色字体
rospy.logwarn("hello,warn")  #默认黄色字体
rospy.logerr("hello,error")  #默认红色字体


```



