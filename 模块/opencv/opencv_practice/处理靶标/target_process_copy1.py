import cv2
import numpy as np
import os
# 显示图片
def show_img(box_name, img):
    cv2.imshow(box_name, img)
    cv2.waitKey(0)

def process(image_name):
    # 读取灰度图
    Ori_img = cv2.imread(image_name,0)
    show_img("target",Ori_img)


    # 创建核
    kernal = np.ones((2,2),np.uint8)
    # 腐蚀
    img_erode = cv2.erode(Ori_img,kernal,iterations=1)
    show_img("target",img_erode)
    

    # 膨胀
    img_big = cv2.dilate(img_erode,kernal, iterations=1)
    show_img("target",img_big)
    

    # # 高斯滤波
    img_filtered = cv2.GaussianBlur(img_big, (3,3),0.3)
    show_img("target",img_filtered)




    # 边缘检测
    img_canny = cv2.Canny(img_filtered,120,250)
    show_img("target",img_canny)
    # 二值化
    # ret, thres = cv2.threshold(img_canny,200,255,cv2.THRESH_BINARY_INV)
    # show_img("target",thres)


    # # 膨胀
    # img_big1 = cv2.dilate(thres,kernal, iterations=1)
    # cv2.imshow("target",img_big1)
    # cv2.waitKey(0)
    # # 读取灰度图
    # Ori_img = cv2.imread(image_name,0)
    # cv2.imshow("target",Ori_img)
    # cv2.waitKey(0)

    # # 二值化
    # ret, thres = cv2.threshold(Ori_img,200,255,cv2.THRESH_BINARY_INV)
    # cv2.imshow("target",thres)
    # cv2.waitKey(0)

    # # 高斯滤波
    # img_filtered = cv2.medianBlur(thres, 3)
    # cv2.imshow("target",img_filtered)
    # cv2.waitKey(0)

    # # 创建核
    # kernal = np.ones((2,2),np.uint8)
    # # 腐蚀
    # img_erode = cv2.erode(img_filtered,kernal,iterations=1)
    # cv2.imshow("target",img_erode)
    # cv2.waitKey(0)

    # # 膨胀
    # img_big = cv2.dilate(img_erode,kernal, iterations=1)
    # cv2.imshow("target",img_big)
    # cv2.waitKey(0)

    result = img_canny
    return result
if __name__ == "__main__":

    image_path = "./image/"

    img_list = os.listdir(image_path)
    for img_name in img_list:
        res = process(image_path + img_name)
        cv2.imwrite("./processed/" + img_name, res)
    # for i in range(1,13):
    #     image_name = "./image/target" + str(i) + ".jpg"
    #     res = process(image_name)
    #     cv2.imwrite("./processed/target" + str(i) + ".jpg", res)






# # 腐蚀
# img_erode1 = cv2.erode(img_big1,kernal,iterations=2)
# cv2.imshow("target",img_erode1)
# cv2.waitKey(0)



