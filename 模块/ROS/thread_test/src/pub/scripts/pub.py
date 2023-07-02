import rospy
from std_msgs.msg import String

rospy.init_node("pub",anonymous=True)
pub_1 = rospy.Publisher("topic_1",String)
pub_2 = rospy.Publisher("topic_2",String)

msg1 = String()
msg2 = String()

rate = rospy.Rate(1)
count = 0

while not rospy.is_shutdown():
    msg1.data = "msg_1" + str(count)
    msg2.data = "msg_2" + str(count)
    print(msg1.data)
    pub_1.publish(msg1)
    pub_2.publish(msg2)
    count = count + 1
    rate.sleep()
