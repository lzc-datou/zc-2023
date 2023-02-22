
import os
import sys
# 这是我半个多小时智慧的结晶！！ 试错多次终于成功

# 注意：此脚本直接删除文件不放入回收站
def del_folder(folder_absPath):
    file_list = os.listdir(folder_absPath)
    for name in file_list:
        # 获取第一层目录下的所有路径
        path = os.path.join(folder_absPath, name)
        # 是文件则直接删除
        if(os.path.isfile(path)):
            os.remove(path)
        # 如果不是文件，则当成文件夹再删除即可（递归）
        else:
            del_folder(path)


if __name__ == "__main__":
    # 此脚本接收多个命令行参数作为删除路径
    num = len(sys.argv)  #获取命令行参数个数
    for i in range(1,num):
        folder_path = sys.argv[i]
        del_folder(folder_path)
    print("删除成功")
