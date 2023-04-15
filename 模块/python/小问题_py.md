# python_小问题

**本文档是使用python过程中遇到的一些小问题的记录及解决方法**

## 1. python字符串前加*的作用
在列表前加*号，会将列表拆分成一个一个的独立元素。在字符串前加*会将字符串拆分成一个个字符  

详细解释见文章[python 在列表，元组，字典变量前加*号](https://blog.csdn.net/weixin_40877427/article/details/82931899)


## 2.python中丢弃不需要的返回值
使用双下划线接收不需要的返回值，即可实现丢弃  
例：  
```
def f():
    return arg1,arg2

a, __ = f()  # a接收第一个返回值，第二个返回值被丢弃
```
## pip3安装失败的问题
报错一堆红字
```
raise packaging.version.InvalidVersion(f"{str(ex)} {info}") from None
pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: '0.23ubuntu1' (package: distro-info)
```
错误原因：setuptools版本过高，卸载后重新安装低版本即可。
详见文章[【linux】报错pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: ‘0.23ubuntu1’](https://blog.csdn.net/weixin_44244190/article/details/128863818)