# 提供用于删除的文件 自动生成大量文件 给delete_all.py删除测试使用
import os
mainFile = input("输入主文件夹路径")
os.chdir(mainFile)
dir_list = os.listdir()
for dir in dir_list:

    path = os.path.join(mainFile, dir)
    os.chdir(path)
    # 生成txt文件
    for i in range(10):
        name = "example_" + str(i) + ".txt"
        with open(name, 'w') as file:
            file.write(str(i))
    # 生成文件夹
    for i in range(3):
        name = "example_dir_" + str(i)
        if os.path.exists("./" + name):
            path1 = os.path.join(path, name)
            os.chdir(path1)
            # 生成txt文件
            for i in range(10):
                name = "example_" + str(i) + ".txt"
                with open(name, 'w') as file:
                    file.write(str(i))
            os.chdir(path)
            continue
        else:
            os.mkdir(name)
            path1 = os.path.join(path, name)
            os.chdir(path1)
            # 生成txt文件
            for i in range(10):
                name = "example_" + str(i) + ".txt"
                with open(name, 'w') as file:
                    file.write(str(i))
            os.chdir(path)
