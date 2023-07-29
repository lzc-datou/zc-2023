# SITL仿真方法
> 2023.7.28



**2023.7.26我运行ardupilot+ros+gazebo+QGC仿真成功，能够在ubuntu下跑侦查全流程仿真。  
整个过程耗时8天，碰到了很多的问题。本文档记录了从零开始进行SITL仿真的全部步骤，为学弟学妹铺平道路**

### 1. 下载和编译ardupilot仿真源码
后面都将ardupilot简称为AP
1. 从github下载官方最新源码  
`git clone --recurse-submodules https://github.com/your-github-account/ardupilot`  
详细下载方法见AP官方文档[Downloading the code](https://ardupilot.org/dev/docs/where-to-get-the-code.html)
2. 编译源码  
进入刚刚下载的`ardupilot`文件夹内，运行  
`Tools/environment_install/install-prereqs-ubuntu.sh -y`  
此处需要连接协会的网络翻墙，自己的clash翻墙可能不好使，会卡住，这一步会往`.bashrc`文件中添加`source /home/lzc/ardupilot/Tools/completion/completion.bash`，完善`sim_vehicle.py`的环境变量。  
详细编译方法见AP官方文档[Setting up the Build Environment (Linux/Ubuntu)](https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux)

添加环境变量：将`export PATH=$PATH:$HOME/ardupilot/Tools/autotest`添加到`~/.bashrc`文件夹中。或者执行命令`echo "export PATH=$PATH:$HOME/ardupilot/Tools/autotest" >> ~/.bashrc。`方便以后使用该目录下的`sim_vehicle.py`

### 2. 阅读AP仿真文档
AP仿真文档：[Simulation](https://ardupilot.org/dev/docs/simulation-2.html#)

将该目录下的[SITL Simulator (Software in the Loop)](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html#)和[Using SITL with legacy versions of Gazebo](https://ardupilot.org/dev/docs/sitl-with-gazebo-legacy.html#sitl-with-gazebo-legacy)全部看完。  
1. 看完[SITL Simulator (Software in the Loop)](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html#)要学会`sim_vehicle.py`的使用方法，再结合命令行输入`sim_vehicle.py --help`查看该文件的使用说明，学会搭配`-v -f --out`等选项一起使用
2. 看完[Using SITL with legacy versions of Gazebo](https://ardupilot.org/dev/docs/sitl-with-gazebo-legacy.html#sitl-with-gazebo-legacy)能将ardupilot提供的gazebo模型库`ardupilot_gazebo`下载好并且按照其github仓库的文档配置gazebo环境变量,模型库下载[SwiftGust](https://github.com/SwiftGust/ardupilot_gazebo)版本的。还要学会使用gazebo打开该模型库提供的`.world`文件。我们仿真时主要是使用这个模型库里面提供的模型。
3. **gazebo环境变量讲解**：
    - `GAZEBO_MODEL_PATH`：配置gazebo模型文件的存放路径
    - `GAZEBO_RESOURCE_PATH`：配置gazebo世界文件的存放路径
    - `GAZEBO_PLUGIN_PATH`：配置gazebo插件文件的存放路径
4. **sdf模型文件中的uri标签讲解**：打开`ardupilot_gazebo/models/zephyr_delta_wing_ardupilot_demo/delta_wing.sdf`sdf模型文件，可以看到例如`<uri>model://zephyr_delta_wing`</uri>的内容。URI(Uniform Resource Identifier)意为统一资源标识符，它是一个字符串，用来标示抽象或物理资源。`model://zephyr_delta_wing`意为在`GAZEBO_MODEL_PATH`包含的路径中寻找模型`zephyr_delta_wing`。所以我们使用的模型所在的路径最好都添加进`GAZEBO_MODEL_PATH`环境变量中。如果没有添加还想要使用某个模型，需要将`model://zephyr_delta_wing`替换为该模型的绝对路径。

### 3.了解gazebo基本使用方法
阅读[gazebo官方文档](https://classic.gazebosim.org/tutorials)的入门部分，了解gazebo11界面的基本使用方法。需要阅读的内容为![gazebo官方文档_1](../../../photo/gazebo官方文档_1.png)
![gazebo官方文档_2](../../../photo/gazebo官方文档_2.png)
阅读完后能够了解gazebo11界面的基本使用以及加深对gazebo的model和world的理解。

### 4. 使用地面站QGC
[QGC官方文档](https://docs.qgroundcontrol.com/master/en/index.html)  
下载QGC见其官方文档的[Download](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html)部分

AP官网提供的样例使用的地面站为mavproxy，我们可以使用其他任意地面站代替，这里推荐使用QGC地面站。

到这里，你应该能按照AP官网样例跑起来gazebo+sim_vehicle.py+QGC的联合仿真了。接下来要做的是根据侦查的需求修改仿真模型（加摄像头）和仿真环境（加靶标）。

### 5. 模型使用
1. 飞机模型使用`ardupilot_gazebo/models/zephyr_delta_wing_ardupilot_demo`  
> 该模型自带两个摄像头，一个chase_cam是飞机跟随视角的摄像头（虚拟摄像头），一个ZED_stereocamera是机头位置的双目相机。该模型机身引用的是zephyr_delta_wing模型，在该机身的基础上添加了摄像头。想要在ROS话题中获取gazebo摄像头的图像信息，需要给相应的相机添加插件
2. 下视相机模型使用`ardupilot_gazebo/models_gazebo/camera`
3. 靶标模型使用许偌宁同学使用`blender`软件制作的红蓝靶标。
4. `.world`文件使用`ardupilot_gazebo/worlds/zephyr_ardupilot_demo.world`，以此为基础添加靶标模型后另存为其他名字的`.world`文件。我存的名字叫做`my_simulation.world`

**添加完插件的相机模型，添加完相机的飞机模型，靶标模型以及添加完靶标模型的世界文件我均已上传至`https://github.com/lzc-datou/zc-2023/tree/code/src/simulation`，下载好`ardupilot_gazebo`模型库后，用上述修改好的模型替换掉官方提供的模型，并将`biao`文件夹路径添加进`GAZEBO_MODEL_PATH`，即可运行仿真。该仓库为private仓库，使用不了时记得找李志翀获取权限。**    

### 6. 运行ardupilot+gazebo+QGC+ros联合仿真

**1. 启动ardupilot仿真源码sim_vehicle.py**   

`sim_vehicle.py -v ArduPlane -f gazebo-zephyr`  

如果发现只能连上QGC而连不上mavros，是因为sim_vehicle.py只启动了一个输出端口，在命令行输出中能看到![sim_vehicle.py输出端口](../../../photo/sim_vehicle.py输出端口.png)  
此时我们需要将命令换为  
`sim_vehicle.py -v ArduPlane -f gazebo-zephyr --out 127.0.0.1:14551`   
手动为`sim_vehicle.py`增加一个输出端口`127.0.0.1:14551`，此端口需要与`mavros`的`apm.launch`文件中的端口号相对应。然后再次查看命令行输出可以看到修改后sim_vehicle.py多开启了一个输出端口![sim_vehicle.py输出端口_1](../../../photo/sim_vehicle.py输出端口_1.png)

**2.gazebo启动相应的世界文件**  

`gazebo --verbose -s libgazebo_ros_api_plugin.so  path/to/my_simulation.world`  
此处必须添加`-s libgazebo_ros_api_plugin.so`选项，作用是让gazebo加载ros_api插件，保证gazebo与ros的连接

**3.启动QGC地面站**

下载好QGC后双击`QGroundControl.AppImage`即可

**4.启动rqt_image_view**  

命令行输入`rqt_image_view`查看ros话题中的图像信息。此时应该能看到仿真飞机三个视角的摄像头图像

**5.启动mavros**  

AP与mavros连接主要靠启动`apm.launch`文件。可以命令行输入命令  
`roslaunch mavros apm.launch`  

但是我们经常要修改`apm.launch`文件的参数，所以建议直接把`apm.launch`文件放到主目录或者代码目录下，方便修改且需要运行时直接输入命令`roslaunch apm.launch`即可。仿真时`apm.launch`文件修改如下
```xml
<launch>
	<!-- example launch script for ArduPilot based FCU's -->
	<!-- <arg name="fcu_url" default="/dev/ttyACM2:57600" /> -->
    <!-- <arg name="fcu_url" default="udp://127.0.0.1:14551@localhost14555" /> -->
    <arg name="fcu_url" default="udp://127.0.0.1:14551@:14555" />
	<arg name="gcs_url" default="" />
	<arg name="tgt_system" default="1" />
	<arg name="tgt_component" default="1" />
	<arg name="log_output" default="screen" />
	<arg name="fcu_protocol" default="v2.0" />
	<arg name="respawn_mavros" default="false" />

	<include file="$(find mavros)/launch/node.launch">
		<arg name="pluginlists_yaml" value="$(find mavros)/launch/apm_pluginlists.yaml" />
		<arg name="config_yaml" value="$(find mavros)/launch/apm_config.yaml" />

		<arg name="fcu_url" value="$(arg fcu_url)" />
		<arg name="gcs_url" value="$(arg gcs_url)" />
		<arg name="tgt_system" value="$(arg tgt_system)" />
		<arg name="tgt_component" value="$(arg tgt_component)" />
		<arg name="log_output" value="$(arg log_output)" />
		<arg name="fcu_protocol" value="$(arg fcu_protocol)" />
		<arg name="respawn_mavros" value="$(arg respawn_mavros)" />
	</include>
</launch>
```
我们主要需要修改的参数为`<arg name="fcu_url" default="udp://     " />`。飞控的英文缩写为FCU(flight control unit)
1. 连接实体飞控时该参数为`<arg name="fcu_url" default="/dev/ttyACM2:57600" />`，其中`ttyACM2`是飞控连接电脑后在电脑上的端口号，57600是飞控波特率，波特率是什么可以自行上网了解。
2. 仿真时该参数为`<arg name="fcu_url" default="udp://127.0.0.1:14551@14555`，其中`127.0.0.1:14551`就是我们`sim_vehicle.py`多分配的那个端口号，`14555`是地面站（如QGC）的端口号，有时可能会是`localhost14555`，`localhost`即代表了`127.0.0.1`。
3. 如果仿真时发现mavros连不上QGC了，可以尝试将该参数修改为`<arg name="fcu_url" default="udp://127.0.0.1:14551@localhost14555" />`。

**6.启动用于识别仿真摄像头图像的yolov5**

运行[侦查代码](https://github.com/lzc-datou/zc-2023/tree/code)中yolov5包下的detect_simulation.py文件，启动仿真的yolov5  
`rosrun yolov5 detect_simulation.py`

**7.启动识别数字与定位的程序**  

运行[侦查代码](https://github.com/lzc-datou/zc-2023/tree/code)中`process_imgs`包下的`getNum_and_locate.py`文件，启动数字识别与视觉定位  
`rosrun process_imgs getNum_and_locate.py`

**8.启动规划航线程序**

运行[侦查代码](https://github.com/lzc-datou/zc-2023/tree/code)中`mode`包下的`mode`可执行文件  
`rosrun mode mode`

至此，SITL仿真侦查全流程完毕。

**上述只是基本流程讲解，下面进行相关知识与细节的讲解**








       









