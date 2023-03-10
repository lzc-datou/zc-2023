# 作用：将摄像头的内容保存成一个视频文件
import cv2

video = cv2.VideoCapture(0)
# 创建编码器对象，建议使用mp4v生成.mp4格式视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
# 创建“写对象“ 其中分辨率不建议设置太高，建议640*480
writer = cv2.VideoWriter("camera_video.mp4", fourcc, 30, (640,480))

while(video.isOpened()):
    # 读取图片
    ret, frame = video.read()
    # 将图片写入到“写对象”中
    writer.write(frame)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放对象
video.release()
writer.release()
cv2.destroyAllWindows()

