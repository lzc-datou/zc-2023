from message_filters import ApproximateTimeSynchronizer,Subscriber
from my_msgs.msg import Signal
import rospy
import threading
after_spin = Signal()
after_spin.signal = 10
stop = 0
count = 0
def ts_callback(msg1,msg2):
    print("同步")
    if stop == 0:
        signal_1 = msg1.signal
        signal_2 = msg2.signal
        rospy.loginfo("signal_1 = %d",signal_1)
        rospy.logwarn("signal_2 = %d",signal_2)
    else:
        return
    
    pass

def callback(msg):
    if msg.signal == 1:
        global stop
        stop = 1
        pub_after = rospy.Publisher("/signal_sub/pub",Signal,queue_size=1)
       
        pub_after.publish(after_spin)
        
        global count
        print("pub successfully"+str(count))
        count = count + 1
        
    return
    pass
def shutdown_callback():
    rospy.loginfo("rospy shutdown successfully")


       
        
if __name__ == "__main__":
    rospy.init_node("signal_sub")
    sub_1 = Subscriber("/signal_pub/signal_1",Signal)
    sub_2 = Subscriber("/signal_pub/signal_2",Signal)
    
    ts = ApproximateTimeSynchronizer([sub_1,sub_2],queue_size=10,slop=100)
    
    ts.registerCallback(ts_callback)
    
    sub_control = rospy.Subscriber("/control",Signal,callback)
    rospy.spin()
    rospy.on_shutdown(shutdown_callback)
    print("run after spin()")
    add_thread = threading.Thread(target=thread)
    add_thread.start()

   
    


        
    
    
