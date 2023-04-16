'''
程序功能：将白底黑子图片转换成黑底白字
'''

import cv2
import os
path = "./dataset/"

for num in range(10):
    num_path = path + str(num) + "/"
    img_list = os.listdir(num_path)
    for img_name in img_list:
        img = cv2.imread(num_path + img_name,cv2.IMREAD_GRAYSCALE)
        __,img = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
        cv2.imwrite(num_path + img_name,img)
