import rospy
from geometry_msgs.msg import PoseStamped


rospy.init_node("set_origin")
origin_pub = rospy.Publisher(
    "/mavros/setpoint_position/local", PoseStamped, queue_size=10)
origin = PoseStamped()
origin.header.stamp = rospy.Time.now()
origin.pose.orientation.x = 0
origin.pose.orientation.y = 0
origin.pose.orientation.z = 0
origin.pose.orientation.w = 0
origin_pub.publish(origin)
