# -*-coding:utf-8-*-
# 本文件用于保存getNum_and_locate.py程序中的参数，便于在不同的环境下进行调参
# 自定义变量均为小写，库自带变量一般均为全大写

# rotate_target()函数转正靶标时的相关参数  
kernal_size = (2,2)  
'''腐蚀，膨胀用到的卷积核的大小'''
erode_iter = 1 
'''腐蚀操作的轮数'''
dilate_iter = 1 
'''膨胀操作的轮数'''

    # 边缘检测参数
canny_threshold1 = 120  
'''第一个阈值'''
canny_threshold2 = 200  
'''第二个阈值'''
    # 检测外轮廓角点时的参数
max_corners = 9   
'''最大角点数量'''
quality_level = 0.1  
'''角点质量（暂时不知道明确含义和具体怎么调整）'''
min_distance = 20  
'''识别出的角点间的最小距离（像素点距离）'''

    # 绘制轮廓时的参数   建议外轮廓线条宽度>=外接矩形线条宽度
max_contour_width = 1 
'''最大外轮廓线条宽度'''
min_rect_width = 1 
'''最小外接矩形线条宽度'''
    # 判断相同点时的参数
same_point_maxDistance = 10  
'''此参数用法是x,y差值同时小于此参数，则认为是同一点 (距离为像素点距离)'''
