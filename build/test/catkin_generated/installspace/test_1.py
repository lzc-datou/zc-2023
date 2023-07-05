from message_filters import ApproximateTimeSynchronizer,Subscriber
from my_msgs.msg import Signal
import rospy
after_spin = Signal()
after_spin.signal = 10
def ts_callback(msg1,msg2):
    
    signal_1 = msg1.signal
    signal_2 = msg2.signal
    rospy.loginfo("signal_1 = %d",signal_1)
    rospy.logwarn("signal_2 = %d",signal_2)
    
    pass
def callback(msg):
    if msg.signal == 1:
        rospy.signal_shutdown("shutdown ts_callback")
      
        return
    pass
def shutdown_callback():
    rospy.loginfo("rospy shutdown successfully")
if __name__ == "__main__":
    rospy.init_node("signal_sub")
    sub_1 = Subscriber("/signal_pub/signal_1",Signal)
    sub_2 = Subscriber("/signal_pub/signal_2",Signal)
    sub_control = rospy.Subscriber("/control",Signal,callback)
    ts = ApproximateTimeSynchronizer([sub_1,sub_2],queue_size=10,slop=0.001)

    ts.registerCallback(ts_callback)

    rospy.spin()
    rospy.on_shutdown(shutdown_callback)
    print("run after spin()")

   
    pub_after = rospy.Publisher("/signal_sub/pub",Signal,queue_size=10)
    while(True):
        print("pub_after")
        pub_after.publish(after_spin)


        
    
    
