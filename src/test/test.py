
# import cv2
# from LetNet import LetNet5
# import torch
# import torchvision
# from torch.autograd import Variable
# import os
# import numpy as np
# import sys
# import signal
# def show_img(windows_name,img_name):
#     cv2.imshow(windows_name,img_name)
#     cv2.waitKey(1)
# # 定义类：识别单个数字
# class RecoNum:

#     # 使用LetNet5神经网络模型
#     model = LetNet5()
#     # 训练好的权重路径
#     weight_path = "./best.pth"

#     # 如果有cuda，就用cuda，否则使用cpu
#     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#     # 构造函数传参：纯数字图片
#     def __init__(self) -> None:
#         # 加载该权重到模型
#         self.model.load_state_dict(torch.load(self.weight_path,map_location=self.device))
#         pass
#     def rotate_target(self,Ori_target:cv2.Mat):
#         '直接透视变换转正数字底板。返回值有两种情况，返回(原图，False)和返回(转正图，True)'

#         # 中间处理时不对原图操作，对原图的操作只有最后的转正   Ori_target表示 Origin target
#         # 拷贝一份副本进行操作
#         target = Ori_target.copy()
#         # 图像预处理

#         # 将彩色图(bgr)转成灰度图(gray)
#         target = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
#         # 创建核
#         kernal = np.ones((2,2),np.uint8)
#         # 膨胀
#         target = cv2.dilate(target,kernal, iterations=2)
#         # show_img("dilate",target) # 测试用
#         # 腐蚀
#         target = cv2.erode(target,kernal,iterations=1)
#         # show_img("erode",target) # 测试用
    
        
#         #边缘检测
#         target = cv2.Canny(target,120,200)
#         # show_img("canny_img",target) # 测试用

#         img_area = target.shape[0] * target.shape[1]
#         # print("img_area = ",img_area)

#         # 创建空白图片绘制外轮廓
#         im_test = np.zeros(target.shape,dtype=np.float32)

#         # 寻找最大面积轮廓和数字底板外轮廓 # 参数给cv2.RETR_TREE,检测所有轮廓
#         contours, __ = cv2.findContours(target, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#         areas = []
#         for c in range(len(contours)):
#             area = cv2.contourArea(contours[c])
#             # print("area = ",area) # 测试用

#             areas.append(area)
        
#         if len(areas) != 0:
#             max_id = areas.index(max(areas))
#             max_area = max(areas)
#         else:
#             return Ori_target,False
        
#         # 判断最大外轮廓是否合理
#         if max_area/img_area < 0.2:
#             # print("max_area not find")
#             return Ori_target,False
#         # 获取数字底板外轮廓
#         areas_copy = areas.copy()
#         while(True):
#             numBoard_area = max(areas_copy)
#             if numBoard_area > 0.3*max_area:
#                 areas_copy.remove(numBoard_area)
#             elif numBoard_area < 0.1*max_area:
#                 # print("number_board not find")
#                 return Ori_target,False
#             else:
#                 numBoard_id = areas.index(numBoard_area)
#                 break
#         # print("max_id = ",max_id) # 测试用
#         # print("numBoard_id = ",numBoard_id)

#         cv2.drawContours(im_test,contours,max_id,255,2) 
#         cv2.drawContours(im_test,contours,numBoard_id,255,2) 

#         box_index = []
#         # 绘制最小外接矩形
#         min_rect = cv2.minAreaRect(contours[max_id])
#         numBoard_rect = cv2.minAreaRect(contours[numBoard_id])
#         numBoard_box = cv2.boxPoints(numBoard_rect)
#         numBoard_box = np.int32(numBoard_box)
#         # 获取最小外接矩形的四个角点 其中x坐标最小的点为第0个，以顺时针依次排序
#         min_box = cv2.boxPoints(min_rect)
#         min_box = np.int32(min_box)
#         # 找外轮廓角点
#         corners = cv2.goodFeaturesToTrack(im_test, 9, 0.01, 10)
#         for point in corners:
#             x,y = np.int32(point.ravel())
#             # 对比最大外轮廓和最小近似矩形相同点
#             for i in range(4):
#                 if abs(x - min_box[i][0]) <=10 and abs(y - min_box[i][1]) <=10:
#                     box_index.append(i)
#                     # print(i) # 测试用
            
#             cv2.circle(im_test,(x,y),3,[255,0,0],5) # 测试用

        
#         cv2.drawContours(im_test,[min_box],0,255,2) 
#         cv2.drawContours(im_test,[numBoard_box],0,255,2) 
#         show_img("after draw",im_test)  # 测试用

#         # 如果重合角点不是两个，直接弃用
#         if len(box_index) != 2:
#             # print("same point less than 2")
#             return Ori_target,False
#         # 外接矩形宽  数据类型:double  转成int32使用
#         width = np.int32(numBoard_rect[1][0])
#         # 外接矩形高
#         height = np.int32(numBoard_rect[1][1])
#         # 数字底板边长（接近正方形）(取宽高平均值,宽高略微不一样，差不太多)  使用np.ceil向上取整
#         side_len = np.int32(np.ceil((width+height)/2))
#         # 角点索引升序排序  
#         box_index.sort()
#         global src
#         # 四种情况分类讨论_1
#         if box_index == [0,3]:
#             #  靶标朝向为右上  原图顺序(1 2 3 0)为正
#             src = np.float32([numBoard_box[1],numBoard_box[2],numBoard_box[3],numBoard_box[0]])
#         elif box_index == [2,3]:
#             #  靶标朝向为左上  原图顺序(0 1 2 3)为正
#             src = np.float32([numBoard_box[0],numBoard_box[1],numBoard_box[2],numBoard_box[3]])
#         elif box_index == [0,1]:
#             #  靶标朝向为右下  原图顺序(2 3 0 1)为正
#             src = np.float32([numBoard_box[2],numBoard_box[3],numBoard_box[0],numBoard_box[1]])
#         elif box_index == [1,2]:
#             #  靶标朝向为右下  原图顺序(3 0 1 2)为正
#             src = np.float32([numBoard_box[3],numBoard_box[0],numBoard_box[1],numBoard_box[2]])
#         # 目标结果都是一样的
#         dst = np.float32([[0,0],[side_len,0],[side_len,side_len],[0,side_len]])
#         #透视变换转正靶标
#         transformMat = cv2.getPerspectiveTransform(src,dst)  # source 和 destination  原图片和目标图片
#         transform_img = cv2.warpPerspective(Ori_target,transformMat,(side_len,side_len))
#         # show_img("transform_img",transform_img)

#         # print("max_area/img_area = ",max_area/img_area)
#         # print("numBoard_area/max_area = ",numBoard_area/max_area)
#         if transform_img.shape[0] < 0.5*transform_img.shape[1]:
#             return Ori_target,False
#         else:
#             return transform_img,True
  
    
#     def reco_num(self,num_img:cv2.Mat)->int:
#         '识别数字(recognize number) 。输入的图像为28*28的黑底白字图 '

#         # 把图片变成可以在网络中传递的变量
#         transf = torchvision.transforms.ToTensor() # 实例化类
#         num_img = transf(num_img) # 变成张量
#         num_img = Variable(num_img) # 使之可求梯度
        
#         # 获得网络输出，注意：网络输出不直接是数字
#         outputs = self.model(num_img)
#         # 将网络输出变成具体数字
#         predicted = torch.max(outputs.data, 1)[1]
#         num = int(predicted)
#         return num

#     def split_num(self,transform_img:cv2.Mat):
#         '''函数功能:将正方形数字底板分成左右两份，分别送入网络识别'''

#         # 转成灰度图
#         transform_img = cv2.cvtColor(transform_img,cv2.COLOR_RGB2GRAY)
#         # 图片数组的列数
#         columns = transform_img.shape[0]
#         # 将图片从中间分成两份
#         left_num_img = transform_img[:,0:int(0.5*columns)]
#         right_num_img = transform_img[:,int(0.5*columns):columns]
#         # 调整图片为28*28的黑底白字图
#         left_num_img = self.my_resize(left_num_img)
#         right_num_img = self.my_resize(right_num_img)

#         return left_num_img,right_num_img
    
     
#     def my_resize(self,img:cv2.Mat):
#         '函数功能:将图片调整为28*28的黑底白字图(网络训练的是28*28黑底白字图片的识别)'
        
#         # 直方图均衡
#         clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(2,2))
#         img = clahe.apply(img)
#         show_img("zhifangtu",img)
#         # 二值化，使得白底黑字变成黑底白字。使用OTSU二值化
#         __,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#         # img = cv2.adaptiveThreshold(img,125,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,0)
        
#         # show_img("erzhihua",img) # 测试用

#         # 获取图片的行数（rows）和列数(columns)
#         r = img.shape[0]
#         c = img.shape[1]

#         # 截取图片，宽，高均取0.1-0.9范围，去除图片边缘的干扰。
#         img = img[int(0.1*r):int(0.9*r),int(0.1*c):int(0.9*c)]

#         # 这部分放缩重点是不能使得数字变形。单个数字图片高：宽=2：1，要把这个图片调整为一个1：1的正方形图片
#         # 获取图片高度与28的比值，等比例将原图放缩为高度为28的图片（此时宽度小于28）
#         ratio = img.shape[0] / 28
#         new_c = int(img.shape[1] / ratio) # 新的宽度
#         img = cv2.resize(img,(new_c,28))
#         # show_img("to_28_h",img) 测试用

#         # 根据新宽度与28的差值，将宽度扩展到28   int()函数向下取整
#         long = (28 - new_c)/2
#         if long % 1 != 0:
#             long_l = int(long)
#             long_r = int(long)+1
#         else:
#             long_l = int(long)
#             long_r = int(long)

#         # 使用0将图片两边扩展到28
#         img = cv2.copyMakeBorder(img,0,0,long_l,long_r,cv2.BORDER_CONSTANT,0)
#         # show_img("kuobian",img) # 测试用

#         # 腐蚀膨胀，消除一些噪声
#         kernal = np.ones((2,2),np.uint8)
#         img = cv2.erode(img,kernal,iterations=1)
#         img = cv2.dilate(img,kernal,iterations=1)
#         show_img("xingtai",img) #测试用

#         return img
#     pass

# def process_img(img):
#          # 二值化，使得白底黑字变成黑底白字
#         # __,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
       
#         __,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
#         # show_img("erzhihua",img) # 测试用

#         # 获取图片的行数（rows）和列数(columns)
#         r = img.shape[0]
#         c = img.shape[1]

#         # 截取图片，宽，高均取0.1-0.9范围，去除图片边缘的干扰。
#         img = img[int(0.1*r):int(0.9*r),int(0.1*c):int(0.9*c)]

#         # 这部分放缩重点是不能使得数字变形。单个数字图片高：宽=2：1，要把这个图片调整为一个1：1的正方形图片
#         # 获取图片高度与28的比值，等比例将原图放缩为高度为28的图片（此时宽度小于28）
#         ratio = img.shape[0] / 28
#         new_c = int(img.shape[1] / ratio) # 新的宽度
#         img = cv2.resize(img,(new_c,28))
#         # show_img("to_28_h",img) 测试用

#         # 根据新宽度与28的差值，将宽度扩展到28   int()函数向下取整
#         long = (28 - new_c)/2
#         if long % 1 != 0:
#             long_l = int(long)
#             long_r = int(long)+1
#         else:
#             long_l = int(long)
#             long_r = int(long)

#         # 使用0将图片两边扩展到28
#         img = cv2.copyMakeBorder(img,0,0,long_l,long_r,cv2.BORDER_CONSTANT,0)
#         # show_img("kuobian",img) # 测试用

#         # 腐蚀膨胀，消除一些噪声
#         kernal = np.ones((2,2),np.uint8)
#         img = cv2.erode(img,kernal,iterations=1)
#         img = cv2.dilate(img,kernal,iterations=1)
#         show_img("xingtai",img) #测试用

#         return img
#     # r = img.shape[0]
#     # c = img.shape[1]
#     # img = img[int(0.1*r):int(0.9*r),int(0.1*c):int(0.9*c)]
#     # ratio = img.shape[0] / 28
#     # new_c = int(img.shape[1] / ratio)
    
#     # img = cv2.resize(img,(new_c,28))
#     # show_img("to_28_h",img)
#     # long = (28 - new_c)/2
    
#     # if long % 1 != 0:
#     #     long_l = int(long)
#     #     long_r = int(long)+1
#     # else:
#     #     long_l = int(long)
#     #     long_r = int(long)
#     # img = cv2.copyMakeBorder(img,0,0,long_l,long_r,cv2.BORDER_CONSTANT,0)
#     # show_img("kuobian",img)
#     # kernal = np.ones((2,2),np.uint8)
#     # img = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
#     #     #
#     # show_img("xingtai",img)

#     # print("img_shape = ",img.shape)
#     # long = int((28-img.shape[1])/2)
    
    
#     # img = cv2.resize(img,(28,28))
#     # show_img("resized",img)
#     # kernal = np.uint8(np.array([[0,1,0],[1,0,1],[0,1,0]]))
   


#     # erode_kernel = np.uint8(np.array([[1,0],[1,0]]))
#     # dilate_kernel = np.ones((3,3),np.uint8)
#     # img = cv2.dilate(img,erode_kernel,iterations=2)
#     # show_img("erode",img)
#     # img = cv2.erode(img,dilate_kernel,iterations=1)
#     # show_img("dialate",img)
#     # return img
#     # pass

# def show_img(name,img):
#     cv2.imshow(name,img)
#     cv2.waitKey(0)
# # 用于ctrl + c退出程序
# def quit(signum, frame):
#     print("Keyboard interruption by yourself")
#     sys.exit(0)
# class Locate:
#     img_points = []
#     obj_points = []

#     cameraMatrix = []
#     distCoeffs = []
#     def get_imgPoints(self,Ori_point:list,min_box: list):
#         for point in min_box:
#             point[0] = point[0] + Ori_point[0] 
#             point[1] = point[1] + Ori_point[1]
#             self.img_points.append(point)
#         pass

#     pass
# if __name__ == "__main__":
#     locate = Locate()
#     locate.get_imgPoints([10,20],[[1,2],[3,4],[5,6],[7,8]])
#     print(locate.img_points)
#     # for img_name in os.listdir("./images"):
#     #     signal.signal(signal.SIGINT, quit) # 用于ctrl + c退出程序
#     #     img = cv2.imread("./images/" + img_name)
#     #     # img = cv2.Canny(img,120,200)
#     #     recoNum = RecoNum()
#     #     show_img("Ori_img",img)
#     #     left_num_img,right_num_img = recoNum.split_num(img)
        
#     #     left_num = recoNum.reco_num(left_num_img)
#     #     right_num = recoNum.reco_num(right_num_img)
#     #     number = left_num*10+right_num

#     #     print("num = ",number)

       
import numpy as np
import random

class filter:
    # 使用字典来存储识别到的各数字总数
    num_dict = dict()
    def num_dict_add(self,input_num):
        for key in self.num_dict.keys():
            if key == input_num:
                # 该数字计数增加
                self.num_dict[key] = self.num_dict[key] + 1
                return True
        # 如果字典里没有该数字，则添加该数字并且将其计数调为1
        self.num_dict[input_num] = 1
        return False
            
    # 获取出现次数最多的三个数字
    def get_3_nums(self):
        num_list = list()
        for count in self.num_dict.values():
            num_list.append(count)
        # 对value值进行排序
        num_list.sort(reverse=True)
        # 通过排序后的value值找到对应的key值
        num1 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[0])]
        self.num_dict.pop(num1)
        num2 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[1])]
        self.num_dict.pop(num2)
        num3 = list(self.num_dict.keys())[list(self.num_dict.values()).index(num_list[2])]
        
        return num1,num2,num3

        pass
        
    pass
f = filter()
for times in range(100):
    num = random.randint(0,5)
    f.num_dict_add(num)
print(f.num_dict)
print(f.get_3_nums())
