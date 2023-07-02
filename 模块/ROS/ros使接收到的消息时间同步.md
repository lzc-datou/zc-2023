# ros使接收到的消息时间同步
> 2023.7.2  

如果你想在ROS中筛选同一时刻接收到的消息，你可以使用message_filters工具来实现。message_filters提供了一些方便的接口来进行消息的时间同步和消息的筛选。

下面是一个示例，展示如何在ROS中筛选同一时刻接收到的消息：

```python
#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from message_filters import ApproximateTimeSynchronizer, Subscriber

def callback(msg1, msg2):
    # 处理接收到的消息
    rospy.loginfo("Received messages at the same time!")

# 初始化ROS节点
rospy.init_node('message_filter_example')

# 创建消息订阅者
sub1 = Subscriber('topic1', String)
sub2 = Subscriber('topic2', Image)

# 创建时间同步器
ts = ApproximateTimeSynchronizer([sub1, sub2], queue_size=10, slop=0.1)

# 指定回调函数
ts.registerCallback(callback)

# 使用rospy.spin()启动异步线程，处理回调函数
rospy.spin()
```

在这个例子中，首先通过rospy.init_node()初始化ROS节点。然后，使用Subscriber类创建两个消息订阅者sub1和sub2，分别订阅了'topic1'和'topic2'两个话题。

接下来，创建ApproximateTimeSynchronizer对象ts，并传入sub1和sub2作为参数。'queue_size'参数指定了消息队列的最大容量，而'slop'参数用于设置消息时间戳的误差范围，单位是秒。

然后，使用registerCallback()方法将callback函数注册为回调函数。这样，当在接收到的消息中有相近的时间戳时，就会调用callback函数进行处理。

最后，使用rospy.spin()来启动ROS的主循环，一直等待接收消息并进行处理。

注意，如果使用ExactTimeSynchronizer来实现精确的同步，可以将ApproximateTimeSynchronizer替换为ExactTimeSynchronizer即可。同时还可以使用其他的消息容器，如TimeSynchronizer来实现更多的时间同步功能。