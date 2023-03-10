# 环境变量
> 2023.1.28  

关于linux系统开机过程中都先后读取了哪些配置文件以及环境变量的储存位置，可以参考文章[Ubuntu 环境变量位置](https://blog.csdn.net/doublefi123/article/details/8827626)
## 1. 环境变量是什么  
lzc理解：环境变量就是一个可执行文件所在的路径，添加环境变量后可以让你在任意路径下打开的终端中只要输入该可执行文件名就能运行它，而不需要输入该可执行文件完整的绝对路径。环境变量使得调用可执行文件更加便捷。  
## 2. ubuntu下如何添加环境变量  
使用`export`命令设置环境变量。所有的环境变量均储存在变量`PATH`中，且不同环境变量（路径）之间用`:`隔开。  
最原始的`PATH`变量存放在`/etc/environment`文件中  
**下面假设我们要添加的环境变量为`/home/lzc/bin`**
### 2.1 只是当前终端适用的环境变量
在当前终端输入命令`export PATH="/home/lzc/bin:$PATH"`其中`${变量名}`或者`$变量名`是linux shell中的变量引用方式。（这里建议读者学习一下bash基础命令，方便自己看懂一些`.bash`文件且有时候可以自己写点bash脚本进行便捷操作）此命令意思是将`/home/lzc/bin`放在了原来的`PATH`变量头部并且再次赋值给了变量`PATH`，从而达到了在`PATH`变量中添加了新环境变量`/home/lzc/bin`的目的
### 2.2 所有终端都适用的环境变量  
`~/.bashrc`文件是所有终端打开时都会加载的配置文件。`~`表示`/home/lzc`目录（其中lzc是我的的用户名）。所以我们只要将命令`export PATH="/home/lzc/bin:$PATH"`写入`~/.bashrc`文件，那么任何终端在打开时都会自动执行该命令从而自动添加好了环境变量。可以直接用`记事本`或者`vscode`打开该文件进行写入，也可以在当前终端输入命令`echo "export PATH="/home/lzc/bin:$PATH"" >> ~/.bashrc`,利用`echo`命令将所需内容写入`~/.bashrc`文件中。