import rospy
from std_msgs.msg import String
import threading
msg_1 = "0"
msg_2 = "0"
def callback_1(msg):
    global msg_1
    msg_1 = msg.data
    print("callback_1")
    pass
def callback_2(msg):
    global msg_2
    msg_2 = msg.data
    print("callback_2")
    pass
# def listener_1():
#     sub_1 = rospy.Subscriber("topic_1",String,callback_1)
#     rospy.spin()
# def listener_2():
#     sub_2 = rospy.Subscriber("topic_2",String,callback_2)
#     rospy.spin()
def thread_job():
    rospy.spin()
    
if __name__ == "__main__":
    rospy.init_node("sub",anonymous=True)
    
    # thread_1 = threading.Thread(target=listener_1)
    # thread_1.start()
    # print("thread 1 start")

    # thread_2 = threading.Thread(target=listener_2)
    # thread_2.start()
    sub_1 = rospy.Subscriber("topic_1",String,callback_1)
    sub_2 = rospy.Subscriber("topic_2",String,callback_2)
    thread_1 = threading.Thread(target=thread_job)
    thread_1.start()
    print("thread 1 start")

    
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    print("msg_1 = ",msg_1)
    print("msg_2 = ",msg_2)
    rate.sleep()
    
        



