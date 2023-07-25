# 重装ubuntu步骤
> 2023.7.25


1. 删除ubuntu系统，参考文章[buntu双系统“彻底”删除ubuntu系统]（https://blog.csdn.net/yldmkx/article/details/103949640）
2. 安装ubuntu系统，拿着做好的启动盘对着装就行。也可参考文章[Ubuntu20.04安装详细图文教程（双系统）](https://blog.csdn.net/hwh295/article/details/113409389)
3. 安装edge浏览器。[官方链接](https://www.microsoft.com/zh-cn/edge)
4. 安装vscode。[官方链接](https://code.visualstudio.com/Download)
5. 下载搜狗输入法。[官方链接](https://shurufa.sogou.com)。[安装指导教程](https://shurufa.sogou.com/linux/guide)  

6. 卸载火狐浏览器，参考文章[Ubuntu卸载火狐firefox浏览器](https://blog.csdn.net/liuyuekelejic/article/details/106013185)

7. 删除软件密钥环的方法。命令行输入`seahorse`，在打开的界面中将默认密钥环删除即可。但是软件一直会要你设置密钥环，建议可以都设置成“1”
8. 隐藏上边栏。  
    1. `sudo apt install gnome-tweak-tool`
    2.  ` sudo apt install gnome-shell-extension-autohidetopbar
`   
    3. 重启电脑，打开扩展软件，再将其中的`Hide Top Bar`插件打开即可
9. 安装显卡驱动cuda。（无NVIDIA显卡的电脑可跳过）  
官网：[NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit-archive)

10. 安装gpu版本的torch和torchvision。参考文档[笔记本安装gpu版torch与torchvision](./笔记本安装gpu版torch与torchvision.md)
