import cv2
import numpy as np

# 读取灰度图
Ori_img = cv2.imread("./image/target1.jpg",0)
cv2.imshow("target",Ori_img)
cv2.waitKey(0)

# 创建核
kernal = np.ones((2,2),np.uint8)


# 腐蚀
img_erode = cv2.erode(Ori_img,kernal,iterations=1)
cv2.imshow("target",img_erode)
cv2.waitKey(0)

# 膨胀
img_big = cv2.dilate(img_erode,kernal, iterations=1)
cv2.imshow("target",img_big)
cv2.waitKey(0)

# 高斯滤波
img_filtered = cv2.GaussianBlur(img_big, (3,3),0.3)
cv2.imshow("target",img_filtered)
cv2.waitKey(0)

# 二值化
ret, thres = cv2.threshold(img_filtered,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("target",thres)
cv2.waitKey(0)

# # 膨胀
# img_big1 = cv2.dilate(thres,kernal, iterations=1)
# cv2.imshow("target",img_big1)
# cv2.waitKey(0)
# # 腐蚀
# img_erode1 = cv2.erode(img_big1,kernal,iterations=2)
# cv2.imshow("target",img_erode1)
# cv2.waitKey(0)



