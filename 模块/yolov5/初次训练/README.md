# yolov5
> 2023.2.27

本文档主要记录与yolov5相关的一些问题

## 1.yolov5学习建议
1.yolov5的相关配置和使用方法，见文章[目标检测---教你利用yolov5训练自己的目标检测模型](https://blog.csdn.net/didiaopao/article/details/119954291?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167187656116800186540452%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167187656116800186540452&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-119954291-null-null.142^v68^control,201^v4^add_ask,213^v2^t3_esquery_v2&utm_term=yolov5%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B&spm=1018.2226.3001.4187)


## 2. yolov5训练时监控cpu,gpu和训练过程
1. 监控cpu 使用ubuntu自带的系统监视器或者下载htop。  
htop下载命令：`sudo apt install htop`。  
使用方法：命令行输入`htop`
2. 监控gpu   
`watch -n 2 nvidia-smi`  
`watch -n`用于在固定时间间隔的情况下重复运行某一命令。watch命令的详细用法请命令行输入`watch -h`自行查阅
3. 监控训练过程  
使用tensorboard监控训练过程。yolov5 train.py跑起来之后命令行有提示tensorboard的操作方法


