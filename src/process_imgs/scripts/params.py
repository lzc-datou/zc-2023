# -*-coding:utf-8-*-
# 本文件用于保存getNum_and_locate.py程序中的参数，便于在不同的环境下进行调参
# 自定义变量均为小写，库自带变量一般均为全大写
home_altitude = 604
'水平地面的海拔高度，每到一个新地方时一定记得更新'
locate_error = 0.4
time_error = 0.1
'时间同步器允许的时间误差范围（单位为秒）'
# rotate_target()函数转正靶标时的相关参数
kernal_size = (2, 2)
'''腐蚀，膨胀用到的卷积核的大小'''
erode_iter = 1
'''腐蚀操作的轮数'''
dilate_iter = 1
'''膨胀操作的轮数'''

# 边缘检测函数cv2.canny()的处理方式为：
#   如果某个像素的梯度值小于低阈值，则被判定为非边缘像素，被直接排除。
#   如果某个像素的梯度值大于高阈值，则被判定为边缘像素，并被保留。
#   如果某个像素的梯度值处于低阈值和高阈值之间，则根据其是否与某个高阈值像素连接来确定其是否为边缘像素。
# 边缘检测参数
canny_threshold1 = 50
'''低阈值'''
canny_threshold2 = 150
'''高阈值'''

# cv2.goodFeaturesToTrack()检测外轮廓角点时的参数
#   参数含义：
#   maxCorners：要检测的最大角点数量。如果检测到的角点数量超过这个值，只会返回最强的角点，默认值为 0。
#   qualityLevel：用于角点筛选的可接受的角点质量水平阈值。仅保留大于等于阈值的角点作为最终检测到的角点。取值范围为 0 到 1，默认值为 0.01。
#   minDistance：角点之间的最小欧氏距离。如果两个角点之间的距离小于这个值，则其中之一会被排除，默认值为 10。
max_corners = 9
'''要检测的最大角点数量。如果检测到的角点数量超过这个值，只会返回最强的角点，默认值为 0。'''
quality_level = 0.01
'''用于角点筛选的可接受的角点质量水平阈值。仅保留大于等于阈值的角点作为最终检测到的角点。取值范围为 0 到 1，默认值为 0.01。'''
min_distance = 10
'''角点之间的最小欧氏距离。如果两个角点之间的距离小于这个值，则其中之一会被排除，默认值为 10。'''

# 绘制轮廓时的参数   建议外轮廓线条宽度>=外接矩形线条宽度
max_contour_width = 1
'''最大外轮廓线条宽度'''
min_rect_width = 1
'''最小外接矩形线条宽度'''
# 判断相同点时的参数
same_point_maxDistance = 10
'''此参数用法是x,y差值同时小于此参数，则认为是同一点 (距离为像素点距离)'''

# 如果是正投影看靶标，白色数字底板面积占靶标总面积的比例为0.17446
numberBoard_maxArea_rate = 0.4
'图像中白色数字底板面积占靶标总面积的最大比例'
numberBoard_minArea_rate = 0.1
'图像中白色数字底板面积占靶标总面积的最小比例'

target_line_width = 2
'在空白图像上绘制靶标边缘的线的粗细'
numberBoard_line_width = 2
'在空白图像上绘制白色数字底板边缘的线的粗细'

# 裁剪处理得到的左右数字图像，去除图像边缘干扰对数字识别的影响
clip_h_rate = 0.1
'图片纵向裁剪比例（上下分别裁剪十分之一）'
clip_w_rate = 0.1
'图片横向裁剪比例(左右分别裁剪十分之一)'

min_targetArea_rate = 0.2
'靶标面积占整张图片（yolov5给的截图）面积的最小比例'


LetNet_weight_path = "./src/process_imgs/weights/best.pth"
'LetNet神经网络权重路径'
