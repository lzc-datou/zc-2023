#! /usr/bin/env python
"""
    订阅方:
        订阅消息

"""
import rospy
from geometry_msgs.msg import PoseStamped
import math
from tf.transformations import euler_from_quaternion

def quaternion_to_euler(x, y, z, w):
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    roll_z = math.atan2(t3, t4)

    return roll_x, pitch_y, roll_z

def pose_callback(msg):
    # 四元数转姿态角
        quaternion = (
            msg.pose.orientation.x,
            msg.pose.orientation.y,
            msg.pose.orientation.z,
            msg.pose.orientation.w
        )
        # 姿态角赋值
        roll, pitch, yaw = euler_from_quaternion(quaternion)
        
        # TODO
        pitch = -pitch
        yaw = -yaw + math.pi/2


        # 输出姿态角
        rospy.loginfo("plane roll = %.16f pitch = %.16f yaw = %.16f",math.degrees(roll), math.degrees(pitch), math.degrees(yaw))
        # 2. 图像处理

def main():
    rospy.init_node('attitude_listener', anonymous=True)
    rospy.Subscriber('/mavros/local_position/pose', PoseStamped, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    main()