#! /usr/bin/env python
import rospy
from std_msgs.msg import String

def call_back(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s"%data.data)
    pass
def suber():
    rospy.init_node("sub",anonymous=True)
    sub = rospy.Subscriber("chat", String, call_back, queue_size=10)
    rospy.spin()
    pass


if __name__ == "__main__":
    suber()
    pass
