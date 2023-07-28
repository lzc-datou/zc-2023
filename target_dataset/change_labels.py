import os
import sys
'''
程序功能：用于修改红蓝标签反了的情况。如red_target 对应0改为blue_target对应0
命令行第一个参数为标签目录，无更多参数
使用前注意修改line[0]的值
'''

dir = sys.argv[1]  # 标签目录
file_list = os.listdir(dir)

for file in file_list:
    with open(dir+"/"+file,"r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            line = list(line)
            # 将每行开头的字符修改为0或者1
            line[0] = '1' # 或者修改为'0' 
            line = ''.join(line)
            lines[i] = line
        with open(dir+"/"+file,"w") as f:
            for i in range(len(lines)):
                # write函数每次都会自动换行写入
                f.write(lines[i])
        
