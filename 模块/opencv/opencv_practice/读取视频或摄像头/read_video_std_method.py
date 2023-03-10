# 作用：打开并显示摄像头画面
# 读取摄像头或者视频的标准语法（以下以摄像头为例）
import cv2

# 首先创建一个VideoCapture对象，内置摄像头为0，若有其他摄像头则依次为1,2,3,4，.....
video = cv2.VideoCapture(0)

# 检测视频或摄像头是否正常打开，如果没打开，则主动打开
if not video.isOpened():
    video.open()

# 在视频或摄像头持续打开期间才进行操作，如果结束或关闭，则退出循环
while(video.isOpened()):
    ret, frame = video.read()

    # cap.read() 返回一个 bool 值(True/False)。如果加载成功，它会返回True。因此，你可以通过这个返回值判断视频是否结束。
    if(ret):
        cv2.imshow("video", frame)
        #如果按下q键，则退出循环
        # 注意：如果imshow()后没有跟waitKey()函数，则无法正常显示视频流内容
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cv2.destroyAllWindows()
# 释放对象video
video.release()
        

