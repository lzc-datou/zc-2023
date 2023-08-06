import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

if __name__ == "__main__":
    rospy.init_node("my_usb_cam")
    cam_pub = rospy.Publisher("/my_usb_cam/image_raw",Image,queue_size=10)
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            frame = bridge.cv2_to_imgmsg(frame,"bgr8")
            cam_pub.publish(frame)
        else:
            print("open camera fail")
        