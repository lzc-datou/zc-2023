import math
import numpy as np
def rotate_xyz(x,y,z,roll,pitch,yaw):
        '''
        函数功能：将pnp算法获取到的相对坐标系通过旋转变换为X轴正方向为北，Y轴正方向为东的直角坐标系\n
        放置时相机朝向正下方，相机坐标系： x朝向相机平面右边，z朝向相机平面正前方，y朝向相机平面下方。\n
        参数说明：\n
        x,y,z:分别是pnp算法获取到的靶标在相机坐标系下的相对坐标x,y,z\n
        roll:飞机的滚转角\n
        pitch:飞机的俯仰角\n
        yaw:飞机的偏航角\n
        返回值：旋转过后的x,y坐标

        '''
         # 订阅飞控gps坐标 gps_sub = rospy.Subscriber('/mavros/global_position/global', NavSatFix, gps_callback)
        # 订阅飞控姿态信息（俯仰，偏航，滚转） attitude_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, attitude_callback)


        # 角度转弧度
        roll = roll/180 * math.pi
        pitch = pitch/180 * math.pi
        # 绕偏航轴旋转时，由于相机坐标系与飞控坐标系的差别，所以需要多转0.5*pi
        yaw = yaw/180 * math.pi + 0.5 * math.pi
        
       
        # 绕滚转轴旋转
        Rx = np.array(
            [[math.cos(roll),0,math.sin(roll)],
             [0,1,0],
             [-math.sin(roll),0,math.cos(roll)]]
            )
        # 绕俯仰轴旋转
        Ry = np.array(
            [[1,0,0],
             [0,math.cos(pitch),-math.sin(pitch)],
             [0,math.sin(pitch),math.cos(pitch)]]
            )
        # 绕偏航轴旋转
        Rz = np.array(
            [[math.cos(yaw),-math.sin(yaw),0],
             [math.sin(yaw),math.cos(yaw),0],
             [0,0,1]]
             )
        
        R = np.dot(np.dot(Rx,Ry),Rz)
        
        xyz = np.array(
            [[x],
             [y],
             [z]]
             )
        rotated_xyz = np.dot(R,xyz)
        print(rotated_xyz)
        rotated_x = rotated_xyz[0,0]
        rotated_y = rotated_xyz[1,0]
       
        return rotated_x,rotated_y

rotate_xyz(1,1,1,30,30,30)

