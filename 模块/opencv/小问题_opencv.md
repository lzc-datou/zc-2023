# 小问题

**本文档主要记录看官方文档学习Opencv时没理解的一些函数的使用问题**

## 1. cv2.waitKey()的详细使用方法
相关内容与补码及ASCII码有关，参考以下两篇文章  
1. [Opencv 中 waitkey（）& 0xFF，“0xFF”的作用解释](https://blog.csdn.net/hao5119266/article/details/104173400)
2. [用python opencv 调用摄像头之if cv2.waitKey(1) & 0xFF == ord('q')分析](https://blog.csdn.net/weixin_42480593/article/details/82751180)

注意：如果imshow()函数后没有跟waitKey()，则无法正常显示视频流内容。详细解释见文章[OpenCV： imshow后不加waitkey无法显示视频](https://www.cnblogs.com/kissfu/p/3608016.html)
