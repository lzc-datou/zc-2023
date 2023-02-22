import os
file_name = input("请输入你要删除内容的文件夹绝对路径")
file_list = os.listdir(file_name)
for name in file_list:
    name_path = file_name + "/" + name
    if os.path.isfile(name_path):
        os.remove(name_path)
    else:
        file_list2 = os.listdir(name_path)
        os.chdir(name_path)
        for file in file_list2:
            os.remove(file)

