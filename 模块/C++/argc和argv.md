## 本文档解释C/C++ 中的argc和argv的含义与使用方法 
> 2023.1.12

详见链接<https://zhuanlan.zhihu.com/p/267822985>

lzc总结：
1. argc(argument count) 记录了命令行输入参数的个数  
2. argv(argument value) 记录了命令行输入参数的内容（值），argv是一个指针，指向储存了命令行参数的字符数组

一般定义方法
> - `int argc, char** argv ` 

或者  
> - `int argc, char* argv[]`

两者意思相同，只是一个从指针角度定义，一个从数组角度定义。本质上来说是：数组，可以用指向它首地址的指针来表示



