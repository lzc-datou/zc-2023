# ROS导入python文件
> 2023.2.1

问题：在ROS架构下如何导入自己写的python文件

出问题原因：rosrun或roslaunch的默认路径为工作空间路径，所以`1.py`直接导入同目录下的`2.py`文件是会失败的

解决方法：在`1.py`中设置临时环境变量，详细方法见视频[python模块导入](https://www.bilibili.com/video/BV1Ci4y1L7ZZ/?p=145&vd_source=c5ad8ce8d13c3bb687a6f4c57bcd3ea6)(推荐)或者看文档[导入模块方法](http://www.autolabor.com.cn/book/ROSTutorials/di-3-zhang-ros-tong-xin-ji-zhi-jin-jie/33-pythonmo-kuai-dao-ru.html)