# anaconda启用与退出
> 2023.1.29
详见文章[《【Linux】安装Anaconda后默认不进入conda环境方法》](https://blog.csdn.net/qq_39856931/article/details/109862865)

首先添加anaconda环境变量，使得命令行能识别conda命令
1.  `conda activate base` 启用base环境
2. `conda deactivate` 退出base环境
3. `conda config --set auto_activate_base false` 打开终端时不自动进入base环境