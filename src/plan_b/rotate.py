import cv2
import numpy as np
# 还需要导入参数文件中的参数


# 输入要求：yolov5框出的完整靶标图片
def rotate_target(Ori_target):
    '备用方案：转正整个靶标'
    # 中间处理时不对原图操作，对原图的操作只有最后的转正   Ori_target表示 Origin target
    # 拷贝一份副本进行操作
    target = Ori_target.copy()
    # 图像预处理操作

    # 将彩色图(bgr)转成灰度图(gray)
    target = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
    # 创建核
    kernal = np.ones(kernal_size,np.uint8)
    # 腐蚀
    target = cv2.erode(target,kernal,iterations=erode_iter)
     # 膨胀
    target = cv2.dilate(target,kernal, iterations=dilate_iter)
    # 边缘检测
    target = cv2.Canny(target,canny_threshold1,canny_threshold2)

    # 图像预处理结束


    # 创建空白图片绘制外轮廓
    blank_img = np.zeros(target.shape,dtype=np.float32)

    # 寻找最大面积轮廓
    contours, hierarchy = cv2.findContours(target, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for cnt in range(len(contours)):
        area = cv2.contourArea(contours[cnt])
        areas.append(area)
        
    max_id = areas.index(max(areas))
    # 将最大外轮廓绘制到空白图上（只是绘制，并不会显示出来，相当于在制作图片）
    cv2.drawContours(blank_img,contours,max_id,255,max_contour_width)


   
    # 绘制最小外接矩形
    min_rect = cv2.minAreaRect(contours[max_id])
    # 获取最小外接矩形的四个角点 其中x坐标最小的点为第0个，以顺时针依次排序
    min_box = cv2.boxPoints(min_rect)
    # 转成int才能使用
    min_box = np.int32(min_box)

    # 找外轮廓角点
    corners = cv2.goodFeaturesToTrack(blank_img, max_corners, quality_level, min_distance)

    # 存储最大外轮廓和最小外接矩形相同点在外接矩形角点坐标中的序号（只有0，1，2，3中的两个数字）
    box_index = []
    # 对于找到的每一个最大外轮廓角点，都进行判断，是否与最小外接矩形四个点中的某个重合
    for point in corners:
        # 展成一维数组
        x,y = np.int32(point.ravel())
        # 对比最大外轮廓和最小外接矩形相同点  
        for i in range(4):
            # 如果像素点x,y差值均小于10，则认为是同一点
            if abs(x - min_box[i][0]) <= same_point_maxDistance and abs(y - min_box[i][1]) <= same_point_maxDistance:
                box_index.append(i)

    cv2.drawContours(blank_img,[min_box],0,255,min_rect_width) 

    # 如果重合角点不是两个，直接弃用
    if len(box_index) != 2:
        return False
    # 外接矩形宽  数据类型:double  转成int32使用
    width = np.int32(min_rect[1][0])
    # 外接矩形高
    height = np.int32(min_rect[1][1])
    # 长边长度
    long_side = max(width,height)
    # 短边长度
    short_side = min(width,height)
    # 角点索引升序排序  
    box_index.sort()
    # 四种情况分类讨论
    global src # 声明src是全局变量，不然报错（难绷）
    if box_index == [0,3]:
        #  靶标朝向为右上  原图顺序(1 2 3 0)为正
        src = np.float32([min_box[1],min_box[2],min_box[3],min_box[0]])
    elif box_index == [2,3]:
        #  靶标朝向为左上  原图顺序(0 1 2 3)为正
        src = np.float32([min_box[0],min_box[1],min_box[2],min_box[3]])
    elif box_index == [0,1]:
        #  靶标朝向为右下  原图顺序(2 3 0 1)为正
        src = np.float32([min_box[2],min_box[3],min_box[0],min_box[1]])
    elif box_index == [1,2]:
        #  靶标朝向为右下  原图顺序(3 0 1 2)为正
        src = np.float32([min_box[3],min_box[0],min_box[1],min_box[2]])
    
    dst = np.float32([[0,0],[short_side,0],[short_side,long_side],[0,long_side]])
    
    #透视变换转正靶标  这时对原图片进行操作，前面使用target的目的就是获取src和dst
    transformMat = cv2.getPerspectiveTransform(src,dst)  # source 和 destination  原图片和目标图片
    transform_img = cv2.warpPerspective(Ori_target,transformMat,(short_side,long_side))

    return transform_img
