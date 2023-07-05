import rospy
num = 10
is_processed = 0
def fun():
    global num
    global is_processed

    if is_processed == 0:
        is_processed = 1
        print('processing:',num)
        num = num + 1

    print('processed:',num)


rospy.init_node("global_value")
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    fun()
    rate.sleep()