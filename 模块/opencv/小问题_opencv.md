# 小问题

**本文档主要记录看官方文档学习Opencv时没理解的一些函数的使用问题**

## 1. cv2.waitKey()的详细使用方法
相关内容与补码及ASCII码有关，参考以下两篇文章  
1. [Opencv 中 waitkey（）& 0xFF，“0xFF”的作用解释](https://blog.csdn.net/hao5119266/article/details/104173400)
2. [用python opencv 调用摄像头之if cv2.waitKey(1) & 0xFF == ord('q')分析](https://blog.csdn.net/weixin_42480593/article/details/82751180)

注意：如果imshow()函数后没有跟waitKey()，则无法正常显示视频流内容。详细解释见文章[OpenCV： imshow后不加waitkey无法显示视频](https://www.cnblogs.com/kissfu/p/3608016.html)。还有一个问题，如果在 `cv2.waitKey(1) & 0xFF == ord('q')`前没有`imshow()`的窗口操作的话，按q不能达到跳出循环的目的

## 2. cv2.VideoWriter()详解
1. 函数详解见文章[python opencv写视频——cv2.VideoWriter()](https://blog.csdn.net/mao_hui_fei/article/details/107573021)
2. 有关视频的基本知识见文章[视频基本知识](https://blog.csdn.net/weixin_36670529/article/details/100977537)

## 3. np.zeros使用方法
详见文章[np.zeros函数知识大全（numpy.zeros()）](https://blog.csdn.net/qq_39072607/article/details/89321495)

## 4.opencv显示图像方式
opencv读取和显示彩色图像的顺序为b,g,r。而Matplotlib显示图像的顺序为r,g,b。注意区别

## 5. opencv旋转图像方法
见文章[使用OpenCV进行图像旋转和平移](https://blog.csdn.net/weixin_38346042/article/details/122595084)

## 5.opencv二值化方法汇总
见文章[python图像二值化方法汇总](https://cloud.tencent.com/developer/article/1722736)
