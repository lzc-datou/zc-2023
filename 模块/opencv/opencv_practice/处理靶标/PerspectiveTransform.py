'''
    程序功能：转正靶标
'''

import cv2
import numpy as np
import os
def show_img(windows_name,img_name):
    cv2.imshow(windows_name,img_name)
    cv2.waitKey(0)
# 输入要求：yolov5框出的完整靶标图片
def rotate_target(img_name):
    Ori_target = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
    target = Ori_target.copy()
    show_img("Ori_target",target)
    # 创建核
    kernal = np.ones((2,2),np.uint8)
    # 腐蚀
    target = cv2.erode(target,kernal,iterations=1)
    cv2.imshow("erode",target)
    cv2.waitKey(0)
    # 膨胀
    target = cv2.dilate(target,kernal, iterations=1)
    cv2.imshow("dilate",target)
    cv2.waitKey(0)
   
    #边缘检测
    canny_img = cv2.Canny(target,120,200)
    show_img("canny_img",canny_img)
    img_area = canny_img.shape[0] * canny_img.shape[1]
    print("img_area = ",img_area)

    # 创建空白图片绘制外轮廓
    im_test = np.zeros(target.shape,dtype=np.float32)

    # 寻找最大面积轮廓和数字底板外轮廓 # 参数给cv2.RETR_TREE,检测所有轮廓
    contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        print("area = ",area) # 测试用

        areas.append(area)
    max_id = areas.index(max(areas))
    max_area = max(areas)
    # 判断最大外轮廓是否合理
    if max_area/img_area < 0.25:
        print("max_area not find")
        return False
    # 获取数字底板外轮廓
    areas_copy = areas.copy()
    while(True):
        numBoard_area = max(areas_copy)
        if numBoard_area > 0.3*max_area:
            areas_copy.remove(numBoard_area)
        elif numBoard_area < 0.1*max_area:
            print("no number board")
            return False
        else:
            numBoard_id = areas.index(numBoard_area)
            break
    print("max_id = ",max_id) # 测试用
    print("numBoard_id = ",numBoard_id)

    cv2.drawContours(im_test,contours,max_id,255,1) 
    cv2.drawContours(im_test,contours,numBoard_id,255,1) 

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
    corners = cv2.goodFeaturesToTrack(im_test, 9, 0.1, 20)
    for point in corners:
        x,y = np.int32(point.ravel())
        # 对比最大外轮廓和最小近似矩形相同点
        for i in range(4):
            if abs(x - min_box[i][0]) <=10 and abs(y - min_box[i][1]) <=10:
                box_index.append(i)
                print(i) # 测试用
        
        cv2.circle(im_test,(x,y),3,[255,0,0],5) # 测试用

    
    cv2.drawContours(im_test,[min_box],0,255,2) 
    cv2.drawContours(im_test,[numBoard_box],0,255,2) 
    show_img("after draw",im_test)  # 测试用

    # 如果重合角点不是两个，直接弃用
    if len(box_index) != 2:
        print("same point less than 2")
        return False
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
    show_img("transform_img",transform_img)

    print("max_area/img_area = ",max_area/img_area)
    print("numBoard_area/max_area = ",numBoard_area/max_area)

    return transform_img
if __name__ == "__main__":

    image_path = "./image/"

    img_list = os.listdir(image_path)
    for img_name in img_list:
        # result
        res = rotate_target(image_path + img_name)
        # cv2.imwrite("./processed/" + img_name, res)
        