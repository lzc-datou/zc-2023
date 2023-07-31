# -*-coding:utf-8-*-

# 添加import 路径
import sys
sys.path.append("./src/process_imgs/scripts")
sys.path.append("./src")
# 导入参数
from params import *

# 导入神经网络
from LetNet import LetNet5

# 导入python库
import os
import math
from torch.autograd import Variable
import torchvision
import torch
import numpy as np
from cv_bridge import CvBridge
import cv2
import rospy

# 导入消息类型
from message_filters import ApproximateTimeSynchronizer, Subscriber
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from my_msgs.msg import Median_gps
from my_msgs.msg import Signal
from my_msgs.msg import Boundingboxs_and_image

# 导入四元数转欧拉角函数
from tf.transformations import euler_from_quaternion

# 定义全局变量
CONSTANTS_RADIUS_OF_EARTH = 6371000.     # meters (m)
'''地球半径，相对坐标转化为gps坐标时使用'''
num_and_location = dict()
'存储每个数字出现的次数及多次定位到的gps坐标'
stop_ts_callback = 0
'标志变量：判断侦查航线是否结束，如果结束，该变量值赋为1，则停止执行消息同步器的回调函数的逻辑，并汇总处理所有得到的数据'
is_processed = 0
'标志变量：判断侦查获取到的数据是否已经处理过'
median_gps = list()
'存储中位数靶标gps坐标，方便侦查结束后循环发布中位数靶标gps坐标'
three_nums = []
'存储识别到的三个靶标数字'


sequence = 0 # 测试


class Times_and_GPS:
    '单个数字出现的次数和多次获取到的该数字的经纬度'
    times = 0
    '次数'
    longitude = []
    '经度列表'
    latitude = []
    '纬度列表'
    pass


class RecoNum:
    '定义类：识别单个数字'
    # 使用LetNet5神经网络模型
    model = LetNet5()
    # 训练好的权重路径


    weight_path = LetNet_weight_path

    # 如果有cuda，就用cuda，否则使用cpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    print("LetNet5 device = ", device)

    # 构造函数传参：纯数字图片
    def __init__(self) -> None:
        # 加载该权重到模型
        self.model.load_state_dict(torch.load(self.weight_path, map_location=self.device))
        # 模型运行使用cuda
        self.model.to(device=self.device)
        pass

    def rotate_target(self, Ori_target: cv2.Mat):
        '直接透视变换转正数字底板。返回值有两种情况，返回(False，原图，空列表)和返回(True，转正图，靶标最小外接矩形角点坐标)'
        
        # 中间处理时不对原图操作，对原图的操作只有最后的转正   Ori_target表示 Origin target
        # 拷贝一份副本进行操作
        
        # <测试>
        global sequence 
        global save_img_path
        save_img_path = "./src/simulation/simulation_image/img_in_rotate/"+str(sequence)+'/'
        if not os.path.exists(save_img_path):
            os.makedirs(save_img_path)
            print(save_img_path+" be created")
        # </测试>

        target = Ori_target.copy()

        cv2.imwrite(save_img_path+'Ori_target.jpg',Ori_target) # 测试
        # 图像预处理

        # 进行仿真时，由于仿真里面的图像过于平滑，如果转成灰度图后无法检测出边缘，故仿真时直接省去灰度图和膨胀腐蚀，直接边缘检测即可
        # # 将彩色图(bgr)转成灰度图(gray)
        # target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite(save_img_path+'grep.jpg',target) # 测试

        # # 创建核
        # kernal = np.ones(kernal_size, np.uint8)
        # # 膨胀
        # target = cv2.dilate(target, kernal, iterations=dilate_iter)
        # cv2.imwrite(save_img_path+'dilate.jpg',target) # 测试
        # # show_img("dilate",target) # 测试用

        # # 腐蚀
        # target = cv2.erode(target, kernal, iterations=erode_iter)
        # cv2.imwrite(save_img_path+'erode.jpg',target) # 测试
        # # show_img("erode",target) # 测试用

        # 边缘检测
        target = cv2.Canny(target, canny_threshold1, canny_threshold2)
        cv2.imwrite(save_img_path+'canny.jpg',target) # 测试
        # show_img("canny_img",target) # 测试用

        img_area = target.shape[0] * target.shape[1]
        # print("img_area = ",img_area)

        # 创建空白图片绘制外轮廓
        im_test = np.zeros(target.shape, dtype=np.float32)

        # 寻找最大面积轮廓和数字底板外轮廓 # 参数给cv2.RETR_TREE,检测所有轮廓
        contours, __ = cv2.findContours(target, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        areas = []
        for c in range(len(contours)):
            area = cv2.contourArea(contours[c])
            # print("area = ",area) # 测试用

            areas.append(area)
        # 此处的检测很有必要，从报错中修改而来
        if len(areas) != 0:
            max_id = areas.index(max(areas))
            max_area = max(areas)
        else:
            rospy.logwarn("contour areas number = 0")
            # <测试>
            warn_path = save_img_path + 'warn.txt'
            with open(warn_path,'w') as file:
                file.write("contour areas number = 0")
            # </测试>
            return False, Ori_target, np.empty(0)

        # 判断最大外轮廓是否合理,最大外轮廓即靶标外轮廓（三角形+正方形）  
        if max_area/img_area < min_targetArea_rate:
            # print("max_area not find")
            rospy.logwarn("max contour area not fit")
            # <测试>
            warn_path = save_img_path + 'warn.txt'
            with open(warn_path,'w') as file:
                file.write("max contour area not fit")
            # </测试>
            return False, Ori_target, np.empty(0)

    
        # 获取数字底板外轮廓
        # <测试>
        areas_path = save_img_path + 'areas.txt'
        with open(areas_path,'w') as file:
            file.write("img_area = "+str(img_area)+'\n')
            file.write("contour areas = \n")
            for area in areas:
                file.write(str(area)+'\n')
                pass
        # </测试>

        areas_copy = areas.copy()
        
        while (True):
            # 此处的检测很有必要，从报错中修改而来
            if len(areas_copy) == 0:
                rospy.logwarn("areas list len = 0")
                # <测试>
                warn_path = save_img_path + 'warn.txt'
                with open(warn_path,'w') as file:
                    file.write("areas list len = 0")
                # </测试>
                return False, Ori_target, np.empty(0)
            else:
                numBoard_area = max(areas_copy)
                if numBoard_area > numberBoard_maxArea_rate * max_area:
                    areas_copy.remove(numBoard_area)
                elif numBoard_area < numberBoard_minArea_rate * max_area:
                    # print("number_board not find")
                    rospy.logwarn("number board area is too small")
                    # <测试>
                    warn_path = save_img_path + 'warn.txt'
                    with open(warn_path,'w') as file:
                        file.write("number board area is too small")
                    # </测试>
                    return False, Ori_target, np.empty(0)
                else:
                    numBoard_id = areas.index(numBoard_area)
                    break
        # print("max_id = ",max_id) # 测试用
        # print("numBoard_id = ",numBoard_id)
        
        cv2.drawContours(im_test, contours, max_id, 255, target_line_width)
        cv2.drawContours(im_test, contours, numBoard_id, 255, numberBoard_line_width)

        
      
        box_index = []
        # 绘制最小外接矩形
        min_rect = cv2.minAreaRect(contours[max_id])
        numBoard_rect = cv2.minAreaRect(contours[numBoard_id])
        numBoard_box = cv2.boxPoints(numBoard_rect)
        numBoard_box = np.int32(numBoard_box)
        # 获取最小外接矩形的四个角点 其中x坐标最小的点为第0个，以顺时针依次排序
        min_box = cv2.boxPoints(min_rect)

        min_box = np.int32(min_box)
        # 找外轮廓角点
        corners = cv2.goodFeaturesToTrack(im_test, max_corners, quality_level, min_distance)
        for point in corners:
            x, y = np.int32(point.ravel())
            # 对比最大外轮廓和最小近似矩形相同点
            for i in range(4):
                if abs(x - min_box[i][0]) <= same_point_maxDistance and abs(y - min_box[i][1]) <= same_point_maxDistance:
                    box_index.append(i)
                    # print(i) # 测试用

            cv2.circle(im_test, (x, y), 3, [255, 0, 0], 5)  # 测试用

        
       
        # 测试用
        # print(im_test.shape)
        # print(min_box)
        
        cv2.drawContours(im_test, [min_box], 0, 255, 2)
        cv2.drawContours(im_test, [numBoard_box], 0, 255, 2)
        cv2.imwrite(save_img_path+'im_test.jpg',im_test) # 测试
        # show_img("after draw", im_test)  # 测试用
       
        # 如果重合角点不是两个，直接弃用
        if len(box_index) != 2:
            # print("same point less than 2")
            rospy.logwarn("same corner point number != 2")
            # <测试>
            warn_path = save_img_path + 'warn.txt'
            with open(warn_path,'w') as file:
                file.write("same corner point number = "+str(box_index))
                
            # </测试>
            return False, Ori_target, np.empty(0)
        # 外接矩形宽  数据类型:double  转成int32使用
        width = np.int32(numBoard_rect[1][0])
        # 外接矩形高
        height = np.int32(numBoard_rect[1][1])
        # 数字底板边长（接近正方形）(取宽高平均值,宽高略微不一样，差不太多)  使用np.ceil向上取整
        side_len = np.int32(np.ceil((width+height)/2))
        # 角点索引升序排序
        box_index.sort()
       
        global src
        # 四种情况分类讨论_1
        if box_index == [0, 3]:
            #  靶标朝向为右上  原图顺序(1 2 3 0)为正
            src = np.float32([numBoard_box[1], numBoard_box[2],numBoard_box[3], numBoard_box[0]])
        elif box_index == [2, 3]:
            #  靶标朝向为左上  原图顺序(0 1 2 3)为正
            src = np.float32([numBoard_box[0], numBoard_box[1],numBoard_box[2], numBoard_box[3]])
        elif box_index == [0, 1]:
            #  靶标朝向为右下  原图顺序(2 3 0 1)为正
            
            src = np.float32([numBoard_box[2], numBoard_box[3],numBoard_box[0], numBoard_box[1]])
        elif box_index == [1, 2]:
            #  靶标朝向为右下  原图顺序(3 0 1 2)为正
            
            src = np.float32([numBoard_box[3], numBoard_box[0],numBoard_box[1], numBoard_box[2]])
        # 目标结果都是一样的
        dst = np.float32(
            [[0, 0], [side_len, 0], [side_len, side_len], [0, side_len]])
        
        # 透视变换转正靶标
        transformMat = cv2.getPerspectiveTransform(src, dst)  # source 和 destination  原图片和目标图片
        transform_img = cv2.warpPerspective(Ori_target, transformMat, (side_len, side_len))
        cv2.imwrite(save_img_path+'transform.jpg',transform_img) # 测试
        # show_img("transform_img",transform_img)
       
        # print("max_area/img_area = ",max_area/img_area)
        # print("numBoard_area/max_area = ",numBoard_area/max_area)
        if transform_img.shape[0] < 0.5*transform_img.shape[1]:
            rospy.logwarn("transform direction wrong")
            # <测试>
            warn_path = save_img_path + 'warn.txt'
            with open(warn_path,'w') as file:
                file.write("transform direction wrong")
            # </测试>
            return False, Ori_target, np.empty(0)
        else:
            # 返回的src用于pnp算法定位
            return True, transform_img, src

    def split_num(self, transform_img: cv2.Mat):
        '''函数功能:将正方形数字底板分成左右两份，为网络识别做准备。返回左侧数字图片和右侧数字图片'''

       
        # 转成灰度图
        transform_img = cv2.cvtColor(transform_img, cv2.COLOR_RGB2GRAY)
     
        # 图片数组的列数
        columns = transform_img.shape[0]
        rows = transform_img.shape[1]
     
        # 将图片从中间分成两份,并做适量裁剪，去除边缘干扰  截取比例根据实际情况调整
        left_num_img = transform_img[int(clip_h_rate * rows):int((1-clip_h_rate) * rows), int(clip_w_rate * columns):int(0.5 * columns)]
        right_num_img = transform_img[int(clip_h_rate * rows):int((1-clip_h_rate) * rows), int(0.5 * columns):int((1- clip_w_rate) * columns)]
      
        # 调整图片为28*28的黑底白字图
        left_num_img = self.my_resize(left_num_img)
        right_num_img = self.my_resize(right_num_img)
        cv2.imwrite(save_img_path+'left_num.jpg',left_num_img) # 测试
        cv2.imwrite(save_img_path+'right_num.jpg',right_num_img) # 测试
        return left_num_img, right_num_img
        pass

    def my_resize(self, img: cv2.Mat):
        '函数功能:将图片调整为28*28的黑底白字图(网络训练的是28*28黑底白字图片的识别)。返回28*28的黑底白字图'
        # 自适应均衡化图像 实现图像增强
        clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(2, 2))
        img = clahe.apply(img)
        # show_img("zengqiang_1", img) # 测试用
        # # 二值化，使得白底黑字变成黑底白字。使用OTSU二值化
        __, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # show_img("erzhihua", img)  # 测试用
        # 这部分放缩重点是不能使得数字变形。单个数字图片高：宽=2：1，要把这个图片调整为一个1：1的正方形图片
        # 获取图片高度与28的比值，等比例将原图放缩为高度为28的图片（此时宽度小于28）
        ratio = img.shape[0] / 28
        new_c = int(img.shape[1] / ratio)  # 新的宽度
        if ratio >= 1:
            # 缩小，使用下采样最合适的方法
            img = cv2.resize(img, (new_c, 28), cv2.INTER_AREA)
            # show_img("to_28_h", img)  # 测试用
        else:
            # 放大，使用上采样最合适的方法
            img = cv2.resize(img, (new_c, 28), cv2.INTER_LINEAR)
            # show_img("to_28_h", img)  # 测试用

        # 根据新宽度与28的差值，将宽度扩展到28   int()函数向下取整
        long = (28 - new_c)/2
        if long % 1 != 0:
            long_l = int(long)
            long_r = int(long)+1
        else:
            long_l = int(long)
            long_r = int(long)

        # 使用0将图片两边扩展到28
        img = cv2.copyMakeBorder(img, 0, 0, long_l, long_r, cv2.BORDER_CONSTANT, 0)
        # show_img("kuobian",img) # 测试用

        # 腐蚀膨胀，消除一些噪声
        kernal = np.ones((2, 2), np.uint8)
        img = cv2.erode(img, kernal, iterations=1)
        img = cv2.dilate(img, kernal, iterations=1)

        global save_img_path # 测试
        cv2.imwrite(save_img_path+'xintai.jpg',img) # 测试
        # show_img("xingtai", img)  # 测试用
        return img

    def reco_num(self, num_img: cv2.Mat) -> int:
        '识别数字(recognize number) 。输入的图像为28*28的黑底白字图。返回识别出的数字(int) '

        # 把图片变成可以在网络中传递的变量
        
        transf = torchvision.transforms.ToTensor()  # 实例化类
        num_img = transf(num_img)  # 变成张量
        num_img = Variable(num_img)  # 使之可求梯度

        # 获得网络输出，注意：网络输出不直接是数字
        if torch.cuda.is_available():
            # 使用cuda
            outputs = self.model(num_img.cuda())
        else:
            # 使用cpu
            outputs = self.model(num_img)
        # 将网络输出变成具体数字
        predicted = torch.max(outputs.data, 1)[1]
        num = int(predicted)
        return num
    pass


class Locate:
    '定义类：定位，获取相对坐标'
    ref_longitude = 0.
    '飞机的经度'
    ref_latitude = 0.
    '飞机的纬度'
    ref_altitude = 0.
    '飞机的海拔(对地高度)'
    roll = 0.
    '飞机滚转角'
    pitch = 0.
    '飞机俯仰角'
    yaw = 0.
    '飞机偏航角'

    img_points = []
    # 根据靶标大小直接得出世界坐标系（以靶标正方形中心为原点）下靶标最小外接矩形的坐标
    # obj_points = np.float32([[-0.5,1.366,0],[0.5,1.366,0],[0.5,-0.5,0],[-0.5,-0.5,0]]) # 最小外接矩形世界坐标

    # 打印的靶标数字底板边长为1cm
    # obj_points = np.float32([[-0.01, 0.01, 0], [0.01, 0.01, 0],
    #                          [0.01, -0.01, 0], [-0.01, -0.01, 0]
    #                          ])  # 目前参数为IR 1080P 18.0mm 1/2.7''相机的参数

    # # 实际靶标边长为1m，数字底板边长0.5m
    # obj_points = np.float32([[-0.25, 0.25, 0], [0.25, 0.25, 0],
    #                          [0.25, -0.25, 0], [-0.25, -0.25, 0]
    #                          ])
    
    # 仿真中靶标边长为2m，数字底板边长1m
    obj_points = np.float32([[-0.5, 0.5, 0], [0.5, 0.5, 0],
                             [0.5, -0.5, 0], [-0.5, -0.5, 0]
                             ])
    # # 相机内参
    # cameraMatrix = np.float32([[ 1312.071067,       0.        , 446.061005],
    #                            [    0.      ,   1313.617388   , 309.887004],
    #                            [    0.      ,       0.        ,     1.    ]
    #                            ])
    # # 相机畸变系数
    # distCoeffs = np.float32([-0.505909,    0.469929,   -0.021110,  -0.018548,  0])

    # 仿真相机参数
    # 相机内参
    cameraMatrix = np.float32([[ 553.686293,       0.        , 320.340100],
                               [    0.      ,   553.594422   , 240.264610],
                               [    0.      ,       0.        ,     1.    ]
                               ])
    # 相机畸变系数
    distCoeffs = np.float32([-0.001381,    -0.001568,   0.000214,  0.000549,  0])

    def get_imgPoints(self, Ori_point, num_board):
        '函数功能：获取到图像坐标系下的坐标并将结果保存至self.img_points，成功获取则返回True，否则返回False'
        # 如果数字底板坐标未获取到,即num_board为空，则返回False
        if num_board.any() == False:
            return False
        # 清除上一次循环获取的图像坐标
        self.img_points.clear()
        for i in range(4):
            point = [Ori_point[0] + num_board[i][0], Ori_point[1]+num_board[i][1]]
            self.img_points.append(point)
        return True

    def get_xyz(self):
        '函数功能：获取相对坐标（靶标相对于相机）'
        __, rvecs, tvecs, __ = cv2.solvePnPRansac(self.obj_points, np.float32(
            self.img_points), self.cameraMatrix, self.distCoeffs)
        # r,__ = cv2.Rodrigues(rvecs)
        # 放置时相机朝向正下方，相机坐标系： x朝向相机平面右边，z朝向相机平面正前方，y朝向相机平面下方。
        # 偏航角：飞机机头与正北方向夹角（0-360°），向东顺时针转动为正
        # 俯仰角：-180°——+180°，机头仰起为正，低头为负
        # 滚转角：-90°——+90°，向右转为正，向左为负
        x = tvecs[0][0]
        y = tvecs[1][0]
        z = tvecs[2][0]
        
        return x, y, z

    def rotate_xyz(self, x, y, z):
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

        #  从mavros获取的角度单位是弧度
        roll = self.roll
        pitch = self.pitch
        # 绕偏航轴旋转时，由于飞控用的是东北天，而我们的目标坐标系是北东地，所以需要多转0.5*pi
        yaw = self.yaw + 0.5 * math.pi

        # 飞控使用的是东北天导航坐标系，对应载体坐标系为右前上坐标系
        # 相机坐标系->载体坐标系（右前上）
        x = x
        y = -y
        z = -z
        # 绕滚转轴旋转，对应载体坐标系Y轴
        Ry = np.array(
            [[math.cos(roll), 0, math.sin(roll)],
             [0, 1, 0],
             [-math.sin(roll), 0, math.cos(roll)]]
        )
        # 绕俯仰轴旋转，对应载体坐标系X轴
        Rx = np.array(
            [[1, 0, 0],
             [0, math.cos(pitch), -math.sin(pitch)],
             [0, math.sin(pitch), math.cos(pitch)]]
        )
        # 绕偏航轴旋转，对应载体坐标系Z轴
        Rz = np.array(
            [[math.cos(yaw), -math.sin(yaw), 0],
             [math.sin(yaw), math.cos(yaw), 0],
             [0, 0, 1]]
        )
        # 旋转矩阵顺序为 ZXY
        R = np.dot(np.dot(Rz, Rx), Ry)
        xyz = np.array(
            [[x],
             [y],
             [z]]
        )
        # 载体坐标系->东北天坐标系逆时针多转90度得到的坐标系（简称坐标系1）
        rotated_xyz = np.dot(R, xyz)
        # 坐标系1->北东地坐标
        # 没多转90度前，结果应为X轴朝东，Y轴朝北，Z轴朝天。多转90度后，变为X轴朝北，Y轴朝西，Z轴朝天。所以还需要将Y轴和Z轴反向从而得到北东地坐标
        rotated_x = rotated_xyz[0, 0]
        rotated_y = -rotated_xyz[1, 0]
        rotated_z = -rotated_xyz[2, 0]
        
        
        return rotated_x, rotated_y, rotated_z
        
        
    def xy_to_gps(self, x, y):
        '''
        函数功能：将旋转变换后的相对坐标转化为靶标的GPS坐标。实质为北东地相对坐标系转gps坐标系\n
        参数说明：\n
        x:rotate_xyz函数返回的rotated_x值\n
        y:rotate_xyz函数返回的rotated_y值\n
        self.latitude:飞机自身的纬度\n
        self.longitude:飞机自身的经度\n
        返回值：靶标经纬度->(longitude,latitude)
        '''
        global CONSTANTS_RADIUS_OF_EARTH
        x_rad = float(x) / CONSTANTS_RADIUS_OF_EARTH
        y_rad = float(y) / CONSTANTS_RADIUS_OF_EARTH
        c = math.sqrt(x_rad * x_rad + y_rad * y_rad)

        ref_lat_rad = math.radians(self.ref_latitude)
        ref_lon_rad = math.radians(self.ref_longitude)

        ref_sin_lat = math.sin(ref_lat_rad)
        ref_cos_lat = math.cos(ref_lat_rad)

        if abs(c) > 0:
            sin_c = math.sin(c)
            cos_c = math.cos(c)

            lat_rad = math.asin(cos_c * ref_sin_lat +(x_rad * sin_c * ref_cos_lat) / c)
            lon_rad = (ref_lon_rad + math.atan2(y_rad * sin_c, c *ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c))

            lat = math.degrees(lat_rad)
            lon = math.degrees(lon_rad)

        else:
            lat = math.degrees(self.ref_latitude)
            lon = math.degrees(self.ref_longitude)

        return lon, lat

    pass


class Filter:
    '过滤器，执行全局变量num_and_location的相关操作'

    def num_dict_add(self, input_num, locate_is_accurate: bool, longitude, latitude):
        ''' 函数功能：将定位到的数字及其经纬度放入全局变量num_and_location中\n
            input_num：识别到的数字\n
            locate_is_accurate: 判断定位是否精确的标志变量,bool类型\n
            longitude:定位得到的数字靶标经度\n
            latitude:定位得到的数字靶标纬度\n
            返回值：True,则该数字在字典中已存在，输出为False，则该数字在字典中还没存在\n
        '''
        global num_and_location
        for key in num_and_location.keys():
            if key == input_num:
                # 该数字计数增加,返回true
                num_and_location[key].times = num_and_location[key].times + 1
                # 如果定位精确，才将定位得到的靶标经纬度放入num_and_location中，否则只增加该数字出现的次数，而不采用其定位
                if locate_is_accurate == True:
                    num_and_location[key].longitude.append(longitude)
                    num_and_location[key].latitude.append(latitude)
                return True
        # 如果字典里没有该数字，则添加该数字及其位置并且将其计数调为1，返回false
        times_and_gps = Times_and_GPS()
        times_and_gps.times = 1
        if locate_is_accurate == True:
            times_and_gps.longitude.append(longitude)
            times_and_gps.latitude.append(latitude)
        num_and_location[input_num] = times_and_gps
        return False

    def get_3_nums_gps(self):
        ''' 函数功能：获取出现次数最多的三个数字及其多次定位的经纬度平均值\n
            输入：无输入值\n
            返回值：三个数字及其对应的经纬度平均值（字典），具体结构为{num:[longitude,latitude]}
        '''
        global num_and_location
        count_list = list()
        for value in num_and_location.values():
            count = value.times
            count_list.append(count)
        # 对times值进行排序
        count_list.sort(reverse=True)
        # 通过排序后的times值找到对应的key值,并对出现次数最多的三个数字的经纬度值进行处理
        num1 = self.times_to_key(count_list[0], num_and_location)
        # 处理经纬度列表数据
        num1_longitude = self.data_process(num_and_location[num1].longitude)
        num1_latitude = self.data_process(num_and_location[num1].latitude)
        # 注意，一定要把已获取的key删除掉，避免两个key对应相同的value时通过value获取不到后一个key值
        num_and_location.pop(num1)

        num2 = self.times_to_key(count_list[1], num_and_location)
        num2_longitude = self.data_process(num_and_location[num2].longitude)
        num2_latitude = self.data_process(num_and_location[num2].latitude)
        num_and_location.pop(num2)

        num3 = self.times_to_key(count_list[2], num_and_location)
        num3_longitude = self.data_process(num_and_location[num3].longitude)
        num3_latitude = self.data_process(num_and_location[num3].latitude)

        num_gps = {num1: [num1_longitude, num1_latitude], num2: [num2_longitude, num2_latitude], num3: [num3_longitude, num3_latitude]}

        return num_gps

    def times_to_key(self, times, num_and_location):
        '''
        说明：此函数配合get_3_nums_gps()使用\n
        函数功能：在字典中根据出现的次数找到对应数字\n
        times:出现的次数\n
        num_and_location:全局变量，存储每个数字出现的次数及多次定位到的gps坐标\n
        返回值：与该出现次数匹配的数字值（key值），获取失败则返回False\n
        '''
        for key, value in num_and_location.items():
            if value.times == times:
                return key

        else:
            print("times to key failure")
            return False

    def data_process(self, data):
        '''
        函数功能：处理定位得到的经纬度数据,目前处理方法暂时为求所有数据平均值\n
        '''
        mean_value = sum(data)/len(data)
        return mean_value
    pass


# 测试： 接收图片并保存
def call_back(boxs_and_image):
    bridge = CvBridge()
    reco = RecoNum()
    locate = Locate()
    for i in range(len(boxs_and_image.image_list)):
        cv_image = bridge.imgmsg_to_cv2(boxs_and_image.image_list[i], "bgr8")
        flag1, transform_img, num_board = reco.rotate_target(cv_image)
        box = boxs_and_image.bounding_boxs[i]
        # Ori_point = [[box.x1,box.y1],[box.x2,box.y1],[box.x1,box.y2],[box.x2,box.y2]]
        Ori_point = [box.x1, box.y1]
        flag2 = locate.get_imgPoints(Ori_point, num_board)
        if flag1 == False:
            continue
        else:
            left_num_img, right_num_img = reco.split_num(transform_img)
            left_num = reco.reco_num(left_num_img)
            right_num = reco.reco_num(right_num_img)
            number = left_num * 10 + right_num
            print("num = ", number)
            # cv2.imwrite("./src/process_imgs/images/left_" + str(boxs_and_image.header.seq) + ".jpg",left_num_img)
            # cv2.imwrite("./src/process_imgs/images/right_" + str(boxs_and_image.header.seq) + ".jpg",right_num_img)
            show_img("cv_img", cv_image)
            # cv2.imwrite("./src/process_imgs/images/transform_img_"+str(boxs_and_image.header.seq) + ".jpg",transform_img)
            show_img("transform_img", transform_img)
        if flag2 == True:
            locate.get_xyz()
    pass

# 测试：展示图片


def show_img(windows_name, img_name):
    cv2.imshow(windows_name, img_name)
    cv2.waitKey(1)


# 实例化对象
reco = RecoNum()
locate = Locate()
filter = Filter()
bridge = CvBridge()

# 消息同步使用的回调函数  注意：该回调函数需要同时收到三个消息后方能触发


def ts_callback(msg1, msg2, msg3):
    '回调函数功能：处理单张图片及定位该图片中的靶标，并把识别到的数字和靶标gps坐标放入全局变量num_and_location中'
    # rospy.loginfo("get into ts_callback")
    # 判断同步器的回调函数是否执行，如果不执行直接返回
    if stop_ts_callback == 1:
        rospy.loginfo("ts_callback is stopped")
        return
    else:
        
        global sequence # 测试
        sequence = sequence + 1 # 测试

        rospy.loginfo("ts_callback begin")
        # 1. 获取飞机自身gps坐标及姿态角
        global locate
        locate.ref_longitude = msg2.longitude
        locate.ref_latitude = msg2.latitude
        # 减去地面海拔从而获得对地高度
        locate.ref_altitude = msg2.altitude - home_altitude

        # 输出飞机自身gps坐标
        rospy.loginfo("plane longitude = %f latitude = %f altitude = %f",locate.ref_longitude, locate.ref_latitude, locate.ref_altitude)

        # 四元数转姿态角
        quaternion = (
            msg3.pose.orientation.x,
            msg3.pose.orientation.y,
            msg3.pose.orientation.z,
            msg3.pose.orientation.w
        )
        # 姿态角赋值
        locate.roll, locate.pitch, locate.yaw = euler_from_quaternion(quaternion)

        # 输出姿态角
        rospy.loginfo("plane roll = %f pitch = %f yaw = %f",math.degrees(locate.roll), math.degrees(locate.pitch), math.degrees(locate.yaw))
        # 2. 图像处理
        rospy.loginfo("len of image is %d ",len(msg1.image_list))
        if len(msg1.image_list) == 0:
            return
        for i in range(len(msg1.image_list)):
            # 将ros图片格式转为opencv图片格式
            cv_image = bridge.imgmsg_to_cv2(msg1.image_list[i],'bgr8')
            # 转正靶标
            is_rotated, transform_img, num_board = reco.rotate_target(cv_image)
            # 获取yolov5矩形框的左上角在原图中的坐标（现在处理的图片是yolov5从原图中截取出来的，靶标在原图中的坐标=yolov5矩形框左上角坐标+现在处理的图片中靶标的实际坐标（实际坐标所在坐标系的原点即为矩形框左上角））
            box = msg1.bounding_boxs[i]
            Ori_point = [box.x1, box.y1]
            # 获取靶标中心正方形白色数字板的四个顶点坐标（在原图中的坐标）
            
            imgPoints_is_got = locate.get_imgPoints(Ori_point, num_board)
            # 如果靶标转正失败，发出警告消息，直接进入下次循环
            if is_rotated == False:
                rospy.logwarn("target rotated failure")
                continue
            # 如果转正成功，则识别数字
            else:
                # 将转正图像分割为左右两个图像
               
                left_num_img, right_num_img = reco.split_num(transform_img)
                # 分别识别左右两个数字
               
                left_num = reco.reco_num(left_num_img)
                right_num = reco.reco_num(right_num_img)
                # 得到最终结果
                number = left_num * 10 + right_num
                rospy.loginfo("num = %d", number)

            # 如果靶标中心正方形白色数字板的四个顶点坐标获取成功，则使用Pnp算法进行视觉定位
            if imgPoints_is_got == True:
                # pnp算法定位，获取相机坐标系下的靶标坐标
                x, y, z = locate.get_xyz()
                # 坐标系变换，将相机坐标系变换为北东地坐标系
                rotated_x, rotated_y, rotated_z = locate.rotate_xyz(x, y, z)
                rospy.loginfo("rotated_x = %f rotated_y = %f rotated_z = %f", rotated_x, rotated_y, rotated_z)
                # 如果视觉定位得到的飞机高度与飞控得到的飞机高度在误差范围内，则认为视觉定位准确，予以采用。否则，则舍弃此次定位
                if rotated_z >= (1 - locate_error) * locate.ref_altitude and rotated_z <= (1 + locate_error) * locate.ref_altitude:
                    #定位精确，予以采用
                    longitude, latitude = locate.xy_to_gps(rotated_x, rotated_y)
                    rospy.loginfo("target longitude = %f  latitude = %f ", longitude, latitude)
                    filter.num_dict_add(number, True, longitude, latitude) 

                    # <测试>
                    rotated_z_save_path = "./src/simulation/simulation_image/img_in_rotate/height.txt"
                    data_save_path = "./src/simulation/simulation_image/img_in_rotate/data.txt"
                    try:
                        # 尝试以添加模式打开文件
                        with open(rotated_z_save_path, "a") as file:
                            file.write("rotated_z_"+ str(sequence) + " = " + str(rotated_z)+"\n")
                            
                    except FileNotFoundError:
                        # 如果文件不存在，则创建文件并以添加模式打开
                        with open(rotated_z_save_path, "w") as file:
                            file.write("rotated_z_"+ str(sequence) + " = " + str(rotated_z)+"\n")


                    
                        # data.txt覆盖写入
                    with open(data_save_path,'w') as file:
                        for key in num_and_location.keys():
                            data_times = num_and_location[key].times
                            data_longitude = num_and_location[key].longitude
                            data_latitude = num_and_location[key].latitude
                            file.write(str(key) + ":" + str(data_times) + "\n")
                            file.write("longitude = " + str(data_longitude) + "\n")
                            file.write("latitude = " + str(data_latitude) + "\n")
                            file.write('\n')
                            pass
                    # </测试>
                else:
                    # 定位不精确，弃用
                    rospy.logwarn("inaccurate locate")

                     # <测试>
                    warn_path = save_img_path + 'warn.txt'
                    with open(warn_path,'w') as file:
                        file.write("inaccurate locate")
                    # </测试>
                    
                    filter.num_dict_add(number, False, 0, 0)
    pass


def state_callback(msg):
    # 如果接收到侦查终止信号，将全局变量stop_ts_callback赋值为1，并发布中位数gps坐标
    if msg.signal == 1:
        rospy.loginfo("signal = %d",msg.signal)
        global stop_ts_callback
        global is_processed
        global median_gps
        global three_nums
        stop_ts_callback = 1

        if is_processed == 0:
            # 处理一次后，下次回调时不再处理
            is_processed = 1
            # 获取得到的三个数字及其对应的精确gps坐标
            num_gps = filter.get_3_nums_gps()
            # 对三个数字进行排序
            num_list = []
            for key in num_gps.keys():
                num_list.append(key)
            num_list.sort(reverse=True)

            three_nums = num_list
            median_num = num_list[1]
            median_gps = [num_gps[median_num][0], num_gps[median_num][1]]
        # 打印结果
        rospy.loginfo("results = %d %d %d",three_nums[0], three_nums[1], three_nums[2])
        rospy.loginfo("median number = %d", three_nums[1])
        rospy.loginfo("median number longitude = %f latitude = %f",median_gps[0],median_gps[1])
        # 发布中位数靶标的gps坐标
        # 赋值
        median_gps_1 = Median_gps()
        median_gps_1.longitude = median_gps[0]
        median_gps_1.latitude = median_gps[1]

        # 发布
        gps_pub = rospy.Publisher("/median_gps", Median_gps, queue_size=10)
        gps_pub.publish(median_gps_1)


if __name__ == "__main__":
    # 初始化ros节点
    rospy.init_node("num_and_location")
    rospy.loginfo("节点初始化完毕")
    # rospy.Subscriber("/yolov5/Boundingboxs_and_image",Boundingboxs_and_image,call_back,queue_size=20) # 测试用，可删除

    # 创建消息订阅者
    box_sub = Subscriber("/yolov5/Boundingboxs_and_image",Boundingboxs_and_image)  # 获取yolov5图像和坐标信息
    gps_sub = Subscriber('/mavros/global_position/global',NavSatFix)  # 获取飞控gps坐标
    pose_sub = Subscriber('/mavros/local_position/pose', PoseStamped)  # 获取飞控姿态
    rospy.loginfo("订阅者创建完毕")
    state_sub = rospy.Subscriber('/is_investigation_over', Signal, state_callback, queue_size=20)  # 获取侦查状态（正在侦查还是已侦查完毕）
    # 创建时间同步器
    ts = ApproximateTimeSynchronizer([box_sub, gps_sub, pose_sub], queue_size=10, slop=time_error)
    rospy.loginfo("同步器创建完毕")
    # 注册回调函数
    ts.registerCallback(ts_callback)
    rospy.loginfo("回调函数注册完毕")

    # 启动回调
    rospy.spin()
