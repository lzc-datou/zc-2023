import os
import readline
with open("example_0.txt", 'r') as file:
    content = file.readline()
    print(type(content)) #readlin()函数返回一个str
