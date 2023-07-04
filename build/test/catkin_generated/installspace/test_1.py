from message_filters import ApproximateTimeSynchronizer,Subscriber
from my_msgs.msg import Signal
import rospy

def callback(msg1,msg2):
    
    signal_1 = msg1.signal
    signal_2 = msg2.signal
    if signal_1 == 1:
        return
    rospy.loginfo("signal_1 = %d",signal_1)
    rospy.logwarn("signal_2 = %d",signal_2)
    if signal_1 == 1:
        rospy.signal_shutdown("shoudong shutdown")
    pass
if __name__ == "__main__":
    rospy.init_node("signal_sub")
    sub_1 = Subscriber("/signal_pub/signal_1",Signal)
    sub_2 = Subscriber("/signal_pub/signal_2",Signal)

    ts = ApproximateTimeSynchronizer([sub_1,sub_2],queue_size=10,slop=0.001)

    ts.registerCallback(callback)

    rospy.spin()
    pub = rospy.Publisher("after_spin()",)
    
