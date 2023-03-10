import cv2
import os
# 打开摄像头并且将图片逐帧保存到image文件夹中
video = cv2.VideoCapture(0)

if not os.path.exists("image"):
    os.mkdir("image")
num = 1
while (video.isOpened()):
    ret, frame = video.read()
    print(num)
    cv2.namedWindow("video",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("video",frame)
    cv2.imwrite("./image/person" + str(num) + ".jpg", frame)
    cv2.waitKey(1)
    num = num + 1

video.release()
    
