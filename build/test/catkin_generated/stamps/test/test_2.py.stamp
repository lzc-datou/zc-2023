import rospy
from my_msgs.msg import Signal

def callback(msg):
    print(msg.signal)
    print("get it")
    pass

rospy.init_node("pub_2")
rospy.Subscriber("/signal_sub/pub",Signal,callback)
