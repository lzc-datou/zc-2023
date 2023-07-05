import rospy
from my_msgs.msg import Signal
count = 0
def callback(msg):
    global count
    print(msg.signal)
    print("get it"+str(count))
    count = count + 1
    pass

rospy.init_node("sub_2")
rospy.Subscriber("/signal_sub/pub",Signal,callback,queue_size=1)
rospy.spin()
