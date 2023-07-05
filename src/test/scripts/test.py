from my_msgs.msg import Signal
import rospy
# 测试多回调函数的启动与终止

signal_1 = Signal()
signal_2 = Signal()
control = Signal()

control.signal = 1

signal_1.signal = 1
signal_2.signal = 2

rospy.init_node("signal_pub",)
pub_1 = rospy.Publisher("/signal_pub/signal_1",Signal,queue_size=10)
pub_2 = rospy.Publisher("/signal_pub/signal_2",Signal,queue_size=10)
pub_control = rospy.Publisher("/control",Signal,queue_size=10)
while True:
    rospy.loginfo("signal_1 = %d signal_2 = %d",signal_1.signal,signal_2.signal)
    signal_1.header.stamp = rospy.Time.now()
    signal_2.header.stamp = rospy.Time.now()
    pub_1.publish(signal_1)
    pub_2.publish(signal_2)
    pub_control.publish(control)