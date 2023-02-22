import rospy
from geometry_msgs.msg import Twist

if __name__=="__main__":
    rospy.init_node("control",anonymous=True)

    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

    rate = rospy.Rate(0.2)

    velocity_msg = Twist()
    velocity_msg.linear.x = 1
    velocity_msg.linear.y = 0
    velocity_msg.linear.z = 0
    velocity_msg.angular.x = 0
    velocity_msg.angular.y = 0
    velocity_msg.angular.z = 0.5

    while(True):
        pub.publish(velocity_msg)
        rate.sleep()





    pass