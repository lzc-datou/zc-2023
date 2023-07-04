import math
import numpy as np
class Locate:
    '定义类：定位，获取相对坐标'
    ref_longitude = 0.
    '飞机的经度'
    ref_latitude = 0.
    '飞机的纬度'
    ref_altitude = 0.
    '飞机的海拔'
    roll = 0.
    '飞机滚转角'
    pitch = 0.
    '飞机俯仰角'
    yaw = 0.
    '飞机偏航角'


    img_points = []
    # 根据靶标大小直接得出世界坐标系（以靶标正方形中心为原点）下靶标最小外接矩形的坐标
    # obj_points = np.float32([[-0.5,1.366,0],[0.5,1.366,0],[0.5,-0.5,0],[-0.5,-0.5,0]]) # 最小外接矩形世界坐标

    obj_points = np.float32([[-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0]])  #目前参数为IR 1080P 18.0mm 1/2.7''相机的参数
    # 相机内参
    cameraMatrix = np.float32([[1312.071067,   0. ,        446.061005
],
 [  0.    ,     1313.617388, 309.887004],
 [  0.     ,      0.      ,     1.        ]])
    # 相机畸变系数
    distCoeffs = np.float32([ -0.505909,  0.469929 , -0.021110 , -0.018548, 0])

    def get_imgPoints(self,Ori_point,num_board):
        '函数功能：获取到图像坐标系下的坐标并将结果保存至self.img_points，成功获取则返回True，否则返回False'
        # 如果数字底板坐标未获取到,即num_board为空，则返回False
        if num_board.any() == False:
            return False
        # 清除上一次循环获取的图像坐标
        self.img_points.clear()
        for i in range(4):
            point = [Ori_point[0] + num_board[i][0],Ori_point[1]+num_board[i][1]]
            self.img_points.append(point)
        return True
        
    def get_xyz(self):
        '函数功能：获取相对坐标（靶标相对于相机）'
        __,rvecs,tvecs,__=cv2.solvePnPRansac(self.obj_points,np.float32(self.img_points),self.cameraMatrix,self.distCoeffs)
        # r,__ = cv2.Rodrigues(rvecs)
        # 放置时相机朝向正下方，相机坐标系： x朝向相机平面右边，z朝向相机平面正前方，y朝向相机平面下方。
        # 偏航角：飞机机头与正北方向夹角（0-360°），向东顺时针转动为正
        # 俯仰角：-180°——+180°，机头仰起为正，低头为负
        # 滚转角：-90°——+90°，向右转为正，向左为负
        x = tvecs[0][0]
        y = tvecs[1][0]
        z = tvecs[2][0]
        print(x,y,z)
        return x,y,z
    
    def rotate_xyz(self,x,y,z):
        '''
        函数功能：将pnp算法获取到的相对坐标系通过旋转变换为X轴正方向为北，Y轴正方向为东的直角坐标系\n
        放置时相机朝向正下方，相机坐标系： x朝向相机平面右边，z朝向相机平面正前方，y朝向相机平面下方。\n
        参数说明：\n
        x,y,z:分别是pnp算法获取到的靶标在相机坐标系下的相对坐标x,y,z\n
        self.roll:飞机的滚转角\n
        self.pitch:飞机的俯仰角\n
        self.yaw:飞机的偏航角\n
        返回值：旋转过后的x,y,z坐标\n
        说明：ros使用的世界坐标系均为北东地（对应XYZ轴）坐标系，不管是东北天还是北东地坐标系，导航坐标系->载体坐标系旋转顺序（即姿态角旋转顺序）均为偏航-俯仰-滚转(ZYX顺序为北东地，ZXY顺序为东北天)

        '''
         # 订阅飞控gps坐标 gps_sub = rospy.Subscriber('/mavros/global_position/global', NavSatFix, gps_callback)
        # 订阅飞控姿态信息（俯仰，偏航，滚转） attitude_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, attitude_callback)


        # 角度转弧度
        roll = math.radians(self.roll)
        pitch = math.radians(self.pitch)
        # 绕偏航轴旋转时，由于飞控用的是东北天，而我们的目标坐标系是北东地，所以需要多转0.5*pi
        yaw = math.radians(self.yaw) + 0.5 * math.pi
        
        # 飞控使用的是东北天导航坐标系，对应载体坐标系为右前上坐标系
        # 相机坐标系->载体坐标系（右前上）
        x = x
        y = -y
        z = -z
        # 绕滚转轴旋转
        Ry = np.array(
            [[math.cos(roll),0,math.sin(roll)],
             [0,1,0],
             [-math.sin(roll),0,math.cos(roll)]]
            )
        # 绕俯仰轴旋转
        Rx = np.array(
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
        # 旋转矩阵顺序为 ZXY
        R = np.dot(np.dot(Rz,Rx),Ry)
        xyz = np.array(
            [[x],
             [y],
             [z]]
             )
        rotated_xyz = np.dot(R,xyz)

        rotated_x = rotated_xyz[0,0]
        rotated_y = -rotated_xyz[1,0]
        rotated_z = -rotated_xyz[2,0]
       
        return rotated_x,rotated_y,rotated_z
        pass
    def xy_to_gps(self,x, y):
        '''
        函数功能：将旋转变换后的相对坐标转化为靶标的GPS坐标。实质为北东地相对坐标系转gps坐标系\n
        参数说明：\n
        x:rotate_xyz函数返回的rotated_x值\n
        y:rotate_xyz函数返回的rotated_y值\n
        self.latitude:飞机自身的纬度\n
        self.longitude:飞机自身的经度\n
        '''
        x_rad = float(x) / self.CONSTANTS_RADIUS_OF_EARTH
        y_rad = float(y) / self.CONSTANTS_RADIUS_OF_EARTH
        c = math.sqrt(x_rad * x_rad + y_rad * y_rad)

        ref_lat_rad = math.radians(self.ref_latitude)
        ref_lon_rad = math.radians(self.ref_longitude)

        ref_sin_lat = math.sin(ref_lat_rad)
        ref_cos_lat = math.cos(ref_lat_rad)

        if abs(c) > 0:
            sin_c = math.sin(c)
            cos_c = math.cos(c)

            lat_rad = math.asin(cos_c * ref_sin_lat + (x_rad * sin_c * ref_cos_lat) / c)
            lon_rad = (ref_lon_rad + math.atan2(y_rad * sin_c, c * ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c))

            lat = math.degrees(lat_rad)
            lon = math.degrees(lon_rad)

        else:
            lat = math.degrees(self.ref_latitude)
            lon = math.degrees(self.ref_longitude)

        return lat, lon

    pass
locate = Locate()
locate.roll = 0
locate.pitch = 0
locate.yaw = 30
print(locate.rotate_xyz(1,1,1))

