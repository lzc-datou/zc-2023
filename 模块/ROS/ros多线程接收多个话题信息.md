# ros多线程接收多个话题信息

1. 使用python的threading模块添加额外线程用于执行rospy.spin()，然后主函数继续往下执行。回调函数中只是将接收到的消息赋值给全局变量，实现全局变量的实时更新，供主函数使用  
2. python创建新线程方法见[文章](https://blog.csdn.net/qq_30193419/article/details/100776075)
3. 代码样例见[thread_test](./thread_test/)