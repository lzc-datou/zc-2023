import cv2
import os
import numpy as np
import threading

def show_img(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(100)


def rotate_target(image):
    global hmin
    global hmax
    global smin
    global smax
    global vmin
    global vmax
    show_img("ori",image)
    image = blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    # 将图像从RGB颜色空间转换为HSV颜色空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    show_img("hsv",hsv_image)
    # 定义蓝色范围在HSV颜色空间中的上下限
    lower_blue = np.array([hmin,smin,vmin])
    upper_blue = np.array([hmax,smax,vmax])
    
    # 根据上下限创建一个蓝色掩码
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    show_img("mask",blue_mask)
    # 将掩码应用于原始图像，提取蓝色区域
    blue_extracted = cv2.bitwise_and(hsv_image,hsv_image,mask= blue_mask)
    show_img("image",blue_extracted)

    pass

def empty(a):

    pass

if __name__ == "__main__":
    cv2.namedWindow("param")
    cv2.resizeWindow("param",640,240)
    cv2.createTrackbar("hmin","param",90,255,empty)
    cv2.createTrackbar("hmax","param",130,255,empty)
    cv2.createTrackbar("smin","param",40,255,empty)
    cv2.createTrackbar("smax","param",255,255,empty)
    cv2.createTrackbar("vmin","param",40,255,empty)
    cv2.createTrackbar("vmax","param",255,255,empty)
    
    img_path = "./image"
    for filename in os.listdir(img_path):
        filename = img_path + "/" + filename
        image = cv2.imread(filename)
        while True:
            hmin = cv2.getTrackbarPos("hmin","param")
            hmax = cv2.getTrackbarPos("hmax","param")
            smin = cv2.getTrackbarPos("smin","param")
            smax = cv2.getTrackbarPos("smax","param")
            vmin = cv2.getTrackbarPos("vmin","param")
            vmax = cv2.getTrackbarPos("vmax","param")
            rotate_target(image)