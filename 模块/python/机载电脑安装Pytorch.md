# 机载电脑下安装pytorch
> 2023.5.12

本文档记录了机载电脑nvidia nx xavier 安装pytorch的方法

## 1. 主要步骤
见文章[Nvidia Jetson篇----Jetson Xavier nx安装pytorch](https://blog.csdn.net/m0_46825740/article/details/121696967)

由于机载电脑的架构为arm架构，与普通的x64架构不同，所以机载电脑上的pytorch不能直接使用pip安装，而需要进入nvidia官网下载nvidia提供的arm架构的pytorch版本。官网为[Pytorch for Jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048/1)

## 2. nvidia官网进不去的问题
进入官网后，点击相应版本进行下载时，会显示无法打开[nvidia.app.box.com](nvidia.app.box.com)的现象，导致无法下载对应的`.whl`文件。解决方法见文章[Jetson错误(二):wget命令提示无法解析主机地址的问题解决](https://blog.csdn.net/m0_51004308/article/details/115407068)。

我使用的方法为：
1. 通过ctrl+alt+t打开终端
2. 然后gedit /etc/resolv.conf

3. 修改内容为下（将DNS地址改为google域名服务器）  
`nameserver 127.0.0.53` -> `nameserver 8.8.8.8`

## 3.pillow的版本问题
安装torchvision时可能会碰到pillow版本过高导致报错，重新安装降低pillow版本即可。可尝试安装8.4.0以下的版本，如果不行就再降低点。安装命令`pip3 install 'pillow <=8.4.0'`

## 4.Jetpack的版本问题
Jetpack的版本需要与python的版本相匹配，如果不匹配，重新安装合适版本的Python是较好的解决方法。安装指定版本的python方法`sudo apt install python3.6`，直接在python后面紧接版本号即可。建议使用`Python3.6`，问题较少且出问题后网上解决方案较多。具体如何更改ubuntu系统下python版本的方法请自行上网搜索。