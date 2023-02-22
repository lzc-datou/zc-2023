#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def puber():
    
    rospy.init_node("pub",anonymous=True)
    pub = rospy.Publisher("chat", String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = "hello world %s" % rospy.get_time()

        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()
        


if __name__=="__main__":
    try: 
        puber()
    except rospy.ROSInterruptException:
        print("ros is shutdown")

