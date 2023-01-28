# python的版本问题  
> 2023.1.28

## 1.两大类
目前`python`主要分为`python2`和`python3`,截止当前日期，`python2`最新版为`python2.7.18`（应该不会再新了）,`python3`最新版为`python3.11.1`。

## 2.区别  
对于我们而言，`python2`与`python3`在语法上相差不大，lzc认为主要区别为命令行的命令不同。`python2`的解释器命令行命令为`python xxx.py`，而`python3`的解释器命令行命令为`python3 xxx.py`。
## 3.python版本对ros的影响
最新的ros2我还没有研究过，这里先不说。  
ros库使用的python版本不是最新版的，所以让ros用最新版的python环境肯定会出问题，这时候需要给ros设置老版本的python环境。lzc经验：老版本ros使用的python为`python2.7`，新版本的ros使用的python至少为`python3`，但是不是`python3`的最新版。具体的版本限制可以看命令行报错提示，会直接告诉你要求的python版本。  
给ros设置python环境方法：`例: set(PYTHON_EXECUTABLE /usr/bin/python3)`在外层CMakeLists.txt中将变量`PYTHON_EXECUTABLE`设置成我们所需要的python版本的路径即可。具体路径在哪，可以使用`locate`命令查找或者手动找