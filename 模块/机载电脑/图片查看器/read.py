import cv2
import os
import time
import numpy as np

pic=cv2.imread('white.jpg')

"""
输入：图片、长、宽
输出：1-->下一张 | -1-->上一张 | 0-->退出程序 | 6-->删除图片
"""
def Show_pic(img,lenth,width):
    cv2.imshow("image", img)

    while True:
        k=cv2.waitKey(0)
        if k==27:
            print("退出")
            cv2.destroyallwindows()
            return 0
        elif k==97:
            # print('上一张')
            return -1
        elif k==100:
            # print('下一张')
            return 1
        elif k==120:
            # print('删除')
            return 6
        
"""
输入：读取文件夹名，长（默认1080），宽（默认720）
功能：A上一张,D下一张,X删除,ESC退出(无图片时C掉即可)
"""
def img_reader(dir_name,lenth=1080,width=720):
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image",lenth,width)
    
    if dir_name[-1]!='/':
        dir_name=dir_name+'/'

    position=0
    while True:
        Dir_list=os.listdir(dir_name)
        p=[]
        for x in Dir_list:
            if x[-3:]=='jpg':
                p.append(x)
        Dir_list=p
        Dir_list.sort()
        
        if Dir_list !=[]:
            img=cv2.imread(dir_name+Dir_list[position])
            command=Show_pic(img,lenth,width)
            if command==0:
                return 0
            elif command==-1:
                if position !=0:
                    print("上一张")
                    position-=1
            elif command==1:
                if position+1<len(Dir_list):
                    if os.path.exists(dir_name+Dir_list[position+1]):
                        print("下一张")
                        position+=1
            elif command==6:
                print("删除")
                os.remove(dir_name+Dir_list[position])
                if position !=0:
                    position-=1
        else:
            time.sleep(0.01)

img_reader("images",1080,720)