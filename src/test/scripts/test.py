from my_msgs.msg import Signal
import rospy


signal_1 = Signal()
signal_2 = Signal()

signal_1.signal = 1
signal_2.signal = 2

rospy.init_node("signal_pub",)
pub_1 = rospy.Publisher("/signal_pub/signal_1",Signal,queue_size=10)
pub_2 = rospy.Publisher("/signal_pub/signal_2",Signal,queue_size=10)
while not rospy.is_shutdown():
    rospy.loginfo("signal_1 = %d signal_2 = %d",signal_1.signal,signal_2.signal)
    signal_1.header.stamp = rospy.Time.now()
    signal_2.header.stamp = rospy.Time.now()
    pub_1.publish(signal_1)
    pub_2.publish(signal_2)