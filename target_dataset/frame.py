#!/usr/bin/env python
'''
程序功能：从视频流中按照指定间隔帧数提取图片
'''
import cv2
import sys

# 注意：每个人使用前记得修改全局变量name，修改为自己的名字缩写以防图片名字与其他人重复
name = "lzc"
# 从视频中间隔几帧提取一张图片
interval = 5



# 记录读到当前视频的第几帧
fps = 0

def video2frame():
    global fps
    video_path = sys.argv[1] # 命令行第一个参数：视频路径
    save_path = sys.argv[2] # 命令行第二个参数：视频帧保存路径
    # 读取txt文件中的图片序数
    with open("./num.txt","r") as f:
        num = int(f.read())
        
    video = cv2.VideoCapture(video_path)
    while video.isOpened():
        ret, frame = video.read()
        if ret == 1 and fps % interval == 0:
            cv2.imwrite(save_path + "/" + name + "_" + str(num) + ".jpg",frame)
            num = num + 1
            fps = fps + 1
        elif ret == 1 and fps % interval != 0:
            fps = fps +1 
            continue
        elif ret != 1:
            break
    # 将新的图片序数写入txt文件中
    with open("./num.txt","w") as f:
        f.write(str(num))
    print("0=blue_target,1=red_target")

if __name__ == "__main__":
    if sys.argv[1] == "--help":
        print("use of frame.py:")
        print("命令行第一个参数：视频路径")
        print("命令行第二个参数：视频帧保存路径")
        exit(0)
    video2frame()
