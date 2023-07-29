# yolov5小问题
> 2023.7.29

### 1. 运行train.py时报错attributeerror: ‘FreeTypeFont‘ object has no attribute ‘getsize‘
原因是pillow版本过高，解决方法：`pip install Pillow==9.5`。  
详细说明见文章[已解决：attributeerror: ‘FreeTypeFont‘ object has no attribute ‘getsize‘](https://blog.csdn.net/qq_63034152/article/details/131626091)