import cv2

# 读取一张图片并将其转化成灰度图
img = cv2.imread("jietu.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("jietu",img)
# 等待按键
cv2.waitKey(0)
# 关闭窗口
cv2.destroyAllWindows()

# 分别打印图片的shape,类型，和size
print(img.shape)
print(type(img))
print(img.size)
