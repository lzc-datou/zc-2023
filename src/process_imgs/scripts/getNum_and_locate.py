# -*-coding:utf-8-*-

# 添加import 路径
import sys
sys.path.append("./src/process_imgs/scripts")

# 导入参数
from params import *
from path_params import *

import rospy
import cv2
import cv_bridge
from my_msgs.msg import Boundingboxs_and_image
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import numpy as np
from LetNet import LetNet5
import torch
import torchvision
from torch.autograd import Variable


# 定义类：识别单个数字
class RecoNum:

    # 使用LetNet5神经网络模型
    model = LetNet5()
    # 训练好的权重路径
    weight_path = "./src/process_imgs/weights/best.pth"

    # 如果有cuda，就用cuda，否则使用cpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 构造函数传参：纯数字图片
    def __init__(self) -> None:
        # 加载该权重到模型
        self.model.load_state_dict(torch.load(self.weight_path,map_location=self.device))
        # 模型运行使用cuda
        self.model.to(device=self.device)
        pass
    def rotate_target(self,Ori_target:cv2.Mat):
        '直接透视变换转正数字底板。返回值有两种情况，返回(False，原图，空列表)和返回(True，转正图，靶标最小外接矩形角点坐标)'

        # 中间处理时不对原图操作，对原图的操作只有最后的转正   Ori_target表示 Origin target
        # 拷贝一份副本进行操作
        target = Ori_target.copy()
        # 图像预处理

        # 将彩色图(bgr)转成灰度图(gray)
        target = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
        # 创建核
        kernal = np.ones((2,2),np.uint8)
        # 膨胀
        target = cv2.dilate(target,kernal, iterations=2)
        # show_img("dilate",target) # 测试用
        # 腐蚀
        target = cv2.erode(target,kernal,iterations=erode_iter)
        # show_img("erode",target) # 测试用
    
        
        #边缘检测
        target = cv2.Canny(target,120,200)
        # show_img("canny_img",target) # 测试用

        img_area = target.shape[0] * target.shape[1]
        # print("img_area = ",img_area)

        # 创建空白图片绘制外轮廓
        im_test = np.zeros(target.shape,dtype=np.float32)

        # 寻找最大面积轮廓和数字底板外轮廓 # 参数给cv2.RETR_TREE,检测所有轮廓
        contours, __ = cv2.findContours(target, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        areas = []
        for c in range(len(contours)):
            area = cv2.contourArea(contours[c])
            # print("area = ",area) # 测试用

            areas.append(area)
        
        if len(areas) != 0:
            max_id = areas.index(max(areas))
            max_area = max(areas)
        else:
            return False,Ori_target,np.empty(0)
        
        # 判断最大外轮廓是否合理
        if max_area/img_area < 0.2:
            # print("max_area not find")
            return False,Ori_target,np.empty(0)
        # 获取数字底板外轮廓
        areas_copy = areas.copy()
        while(True):
            numBoard_area = max(areas_copy)
            if numBoard_area > 0.3*max_area:
                areas_copy.remove(numBoard_area)
            elif numBoard_area < 0.1*max_area:
                # print("number_board not find")
                return False,Ori_target,np.empty(0)
            else:
                numBoard_id = areas.index(numBoard_area)
                break
        # print("max_id = ",max_id) # 测试用
        # print("numBoard_id = ",numBoard_id)

        cv2.drawContours(im_test,contours,max_id,255,2) 
        cv2.drawContours(im_test,contours,numBoard_id,255,2) 

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
        corners = cv2.goodFeaturesToTrack(im_test, 9, 0.01, 10)
        for point in corners:
            x,y = np.int32(point.ravel())
            # 对比最大外轮廓和最小近似矩形相同点
            for i in range(4):
                if abs(x - min_box[i][0]) <=10 and abs(y - min_box[i][1]) <=10:
                    box_index.append(i)
                    # print(i) # 测试用
            
            cv2.circle(im_test,(x,y),3,[255,0,0],5) # 测试用
        # 测试用
        # print(im_test.shape)
        # print(min_box)
        cv2.drawContours(im_test,[min_box],0,255,2) 
        cv2.drawContours(im_test,[numBoard_box],0,255,2) 
        show_img("after draw",im_test)  # 测试用

        # 如果重合角点不是两个，直接弃用
        if len(box_index) != 2:
            # print("same point less than 2")
            return False,Ori_target,np.empty(0)
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
        if box_index == [0,3]:
            #  靶标朝向为右上  原图顺序(1 2 3 0)为正
            src = np.float32([numBoard_box[1],numBoard_box[2],numBoard_box[3],numBoard_box[0]])
        elif box_index == [2,3]:
            #  靶标朝向为左上  原图顺序(0 1 2 3)为正
            src = np.float32([numBoard_box[0],numBoard_box[1],numBoard_box[2],numBoard_box[3]])
        elif box_index == [0,1]:
            #  靶标朝向为右下  原图顺序(2 3 0 1)为正
            src = np.float32([numBoard_box[2],numBoard_box[3],numBoard_box[0],numBoard_box[1]])
        elif box_index == [1,2]:
            #  靶标朝向为右下  原图顺序(3 0 1 2)为正
            src = np.float32([numBoard_box[3],numBoard_box[0],numBoard_box[1],numBoard_box[2]])
        # 目标结果都是一样的
        dst = np.float32([[0,0],[side_len,0],[side_len,side_len],[0,side_len]])
        #透视变换转正靶标
        transformMat = cv2.getPerspectiveTransform(src,dst)  # source 和 destination  原图片和目标图片
        transform_img = cv2.warpPerspective(Ori_target,transformMat,(side_len,side_len))
        # show_img("transform_img",transform_img)

        # print("max_area/img_area = ",max_area/img_area)
        # print("numBoard_area/max_area = ",numBoard_area/max_area)
        if transform_img.shape[0] < 0.5*transform_img.shape[1]:
            return False,Ori_target,np.empty(0)
        else:
            # 返回的src用于pnp算法定位
            return True,transform_img,src
  
    
    def split_num(self,transform_img:cv2.Mat):
        '''函数功能:将正方形数字底板分成左右两份，为网络识别做准备。返回左侧数字图片和右侧数字图片'''

        # 转成灰度图
        transform_img = cv2.cvtColor(transform_img,cv2.COLOR_RGB2GRAY)
        # 图片数组的列数
        columns = transform_img.shape[0]
        rows = transform_img.shape[1]
        # 将图片从中间分成两份,并做适量裁剪，去除边缘干扰  截取比例根据实际情况调整
        left_num_img = transform_img[int(0.1*rows):int(0.9*rows),int(0.1*columns):int(0.5*columns)]
        right_num_img = transform_img[int(0.1*rows):int(0.9*rows),int(0.5*columns):int(0.9*columns)]
        # 调整图片为28*28的黑底白字图
        left_num_img = self.my_resize(left_num_img)
        right_num_img = self.my_resize(right_num_img)

        return left_num_img,right_num_img
        pass

    def my_resize(self,img:cv2.Mat):
        '函数功能:将图片调整为28*28的黑底白字图(网络训练的是28*28黑底白字图片的识别)。返回28*28的黑底白字图'
        # 自适应均衡化图像 实现图像增强
        clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(2,2))
        img = clahe.apply(img)
        show_img("zengqiang_1",img)
        # # 二值化，使得白底黑字变成黑底白字。使用OTSU二值化
        __,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        show_img("erzhihua",img) # 测试用
        # 这部分放缩重点是不能使得数字变形。单个数字图片高：宽=2：1，要把这个图片调整为一个1：1的正方形图片
        # 获取图片高度与28的比值，等比例将原图放缩为高度为28的图片（此时宽度小于28）
        ratio = img.shape[0] / 28
        new_c = int(img.shape[1] / ratio) # 新的宽度
        if ratio >=1:
            # 缩小，使用下采样最合适的方法
            img = cv2.resize(img,(new_c,28),cv2.INTER_AREA)
            show_img("to_28_h",img) #测试用
        else:
            # 放大，使用上采样最合适的方法
            img = cv2.resize(img,(new_c,28),cv2.INTER_LINEAR)
            show_img("to_28_h",img) #测试用
        
        # 根据新宽度与28的差值，将宽度扩展到28   int()函数向下取整
        long = (28 - new_c)/2
        if long % 1 != 0:
            long_l = int(long)
            long_r = int(long)+1
        else:
            long_l = int(long)
            long_r = int(long)

        # 使用0将图片两边扩展到28
        img = cv2.copyMakeBorder(img,0,0,long_l,long_r,cv2.BORDER_CONSTANT,0)
        # show_img("kuobian",img) # 测试用

        # 腐蚀膨胀，消除一些噪声
        kernal = np.ones((2,2),np.uint8)
        img = cv2.erode(img,kernal,iterations=1)
        img = cv2.dilate(img,kernal,iterations=1)
        show_img("xingtai",img) #测试用
        return img
    
    def reco_num(self,num_img:cv2.Mat)->int:
        '识别数字(recognize number) 。输入的图像为28*28的黑底白字图。返回识别出的数字(int) '

        # 把图片变成可以在网络中传递的变量
        transf = torchvision.transforms.ToTensor() # 实例化类
        num_img = transf(num_img) # 变成张量
        num_img = Variable(num_img) # 使之可求梯度
        
        # 获得网络输出，注意：网络输出不直接是数字
        outputs = self.model(num_img)
        # 将网络输出变成具体数字
        predicted = torch.max(outputs.data, 1)[1]
        num = int(predicted)
        return num
    pass
# 定义类：定位，获取相对坐标
class Locate:
    img_points = []
    # 根据靶标大小直接得出世界坐标系（以靶标正方形中心为原点）下靶标最小外接矩形的坐标
    # obj_points = np.float32([[-0.5,1.366,0],[0.5,1.366,0],[0.5,-0.5,0],[-0.5,-0.5,0]]) # 最小外接矩形世界坐标
    obj_points = np.float32([[-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0]])
    # 相机内参
    cameraMatrix = np.float32([[755.74684643,   0. ,        453.27087484],
 [  0.    ,     755.48113315, 298.77898827],
 [  0.     ,      0.      ,     1.        ]])
    # 相机畸变系数
    distCoeffs = np.float32([ 0.00482361,  0.1217625 , -0.00093535 , 0.00044296, -0.40165563])

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
        x = tvecs[0][0]
        y = tvecs[1][0]
        z = tvecs[2][0]
        print(x,y,z)
        return x,y,z
        pass
        
    pass
class filter:
    # 使用字典来存储识别到的各数字总数
    num_dict = dict()
    def num_dict_add(self,input_num):
        ''' 函数功能：将识别到的数字添加到字典中计数\n
            输入：识别到的数字\n
            输出：True,则该数字在字典中已存在，输出为False，则该数字在字典中还没存在\n
        '''
        for key in self.num_dict.keys():
            if key == input_num:
                # 该数字计数增加,返回true
                self.num_dict[key] = self.num_dict[key] + 1
                return True
        # 如果字典里没有该数字，则添加该数字并且将其计数调为1，返回false
        self.num_dict[input_num] = 1
        return False
    # 获取出现次数最多的三个数字
    def get_3_nums(self):
        ''' 函数功能：返回识别次数最多的三个数字（元组）\n
            输入：无输入值\n
            输出：三个数字（元组）
        '''
        num_list = list()
        for count in self.num_dict.values():
            num_list.append(count)
        # 对value值进行排序
        num_list.sort(reverse=True)
        # 通过排序后的value值找到对应的key值
        num1 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[0])]
        self.num_dict.pop(num1) # 注意，一定要把已获取的key删除掉，避免两个key对应相同的value时通过value获取不到后一个key值
        num2 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[1])]
        self.num_dict.pop(num2)
        num3 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[2])]
        
        return num1,num2,num3

        pass
        
    pass


# 测试： 接收图片并保存
def call_back(boxs_and_image):
    bridge = CvBridge()
    reco = RecoNum()
    locate = Locate()
    for i in range(len(boxs_and_image.image_list)):
        cv_image = bridge.imgmsg_to_cv2(boxs_and_image.image_list[i],"bgr8")
        flag1,transform_img,num_board = reco.rotate_target(cv_image)
        box = boxs_and_image.bounding_boxs[i]
        # Ori_point = [[box.x1,box.y1],[box.x2,box.y1],[box.x1,box.y2],[box.x2,box.y2]]
        Ori_point = [box.x1,box.y1]
        flag2 = locate.get_imgPoints(Ori_point,num_board)
        if flag1 == False:
            continue
        else:
            left_num_img,right_num_img = reco.split_num(transform_img)
            left_num = reco.reco_num(left_num_img)
            right_num = reco.reco_num(right_num_img)
            number = left_num *10 + right_num
            print("num = ",number)
            # cv2.imwrite("./src/process_imgs/images/left_" + str(boxs_and_image.header.seq) + ".jpg",left_num_img)
            # cv2.imwrite("./src/process_imgs/images/right_" + str(boxs_and_image.header.seq) + ".jpg",right_num_img)
            show_img("cv_img",cv_image)
            # cv2.imwrite("./src/process_imgs/images/transform_img_"+str(boxs_and_image.header.seq) + ".jpg",transform_img)
            show_img("transform_img",transform_img)
        if flag2 == True:
            locate.get_xyz()
    # for image in boxs_and_image.image_list:
    #     cv_image = bridge.imgmsg_to_cv2(image,"bgr8")
    #     flag,transform_img,box = reco.rotate_target(cv_image)
    #     if flag == False:
    #         continue
    #     else:
    #         left_num_img,right_num_img = reco.split_num(transform_img)
    #         left_num = reco.reco_num(left_num_img)
    #         right_num = reco.reco_num(right_num_img)
    #         number = left_num *10 + right_num
    #         print("num = ",number)
    #         # cv2.imwrite("./src/process_imgs/images/left_" + str(boxs_and_image.header.seq) + ".jpg",left_num_img)
    #         # cv2.imwrite("./src/process_imgs/images/right_" + str(boxs_and_image.header.seq) + ".jpg",right_num_img)
    #         show_img("cv_img",cv_image)
    #         # cv2.imwrite("./src/process_imgs/images/transform_img_"+str(boxs_and_image.header.seq) + ".jpg",transform_img)
    #         show_img("transform_img",transform_img)
    # for box in boxs_and_image.bounding_boxs:
    #     # Ori_point = [[box.x1,box.y1],[box.x2,box.y1],[box.x1,box.y2],[box.x2,box.y2]]
    #     Ori_point = [box.x1,box.y1]
    #     flag = locate.get_imgPoints(Ori_point,box)
    #     if flag == True:
    #         locate.get_xyz()

    pass
# 测试：展示图片
def show_img(windows_name,img_name):
    cv2.imshow(windows_name,img_name)
    cv2.waitKey(5)
if __name__ == "__main__":
    rospy.init_node("num_and_location")
    rospy.Subscriber("/yolov5/Boundingboxs_and_image",Boundingboxs_and_image,call_back,queue_size=20)
    rospy.spin()
