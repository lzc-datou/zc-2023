# ros与anaconda
> 2023.1.29  

今天碰到一个问题：安装完ros后又安装了anaconda，然后运行`catkin_make`时出错

anaconda是什么，可以参考文章[《anaconda是什么，是干嘛用的，与python的区别是什么》](https://www.zhihu.com/question/353409585)，通俗易懂。

![tupian](../photo/ros%E4%B8%8Eanaconda%E5%86%B2%E7%AA%81.png)

可以看到报错找不到模块`python3-empy`。但是这个问题重点不在这里。错误的原因是`-- Using PYTHON_EXECUTABLE: /home/lzc/anaconda3/bin/python3`这行。ros使用的python版本较低而anaconda的python版本较高，二者不兼容导致错误。  

解决方法：使用系统自带的python版本即可。在ros包外层CMakeLists.txt中重新给变量`PYTHON_EXECUTABLE`复制。具体命令为`set(PYTHON_EXECUTABLE  /usr/bin/python3)`其中`/usr/bin/python3`为系统python解释器的绝对路径。

解决的原因：首先在网上找，得知是ros用错了python解释器，但是不知道如何调整。仔细阅读了命令行输出后，由于最近`cmake`写的比较多，一眼看出所有字母大写的`PYTHON_EXECUTABLE`是个变量，而且这个变量的内容貌似就是网上描述的现象的罪魁祸首，故尝试在CMakeLists.txt中修改该变量内容，最终成功。