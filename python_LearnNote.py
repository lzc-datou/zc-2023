# # make a calculator by dict
# def cclt(x, y, operator="+"):
#     result = {
#         "+": x + y,
#         "-": x - y,
#         "*": x * y,
#         "/": x / y
#     }
#     return result.get(operator)

# # generator key word: yield
# def func(n):
#     for i in range(n):
#         yield i

# if __name__ == "__main__":
#     a = func(10)
#     while(True):
#         print(a.__next__())
#         print(next(a))

# 正则表达式
# 使用r消除转义的问题
# 常见匹配字符 /d 数字  /w 字母  /d{3}表示三个数字 /d{3,9}表示3-9个数字
# 使用re 模块进行正则表达式匹配
# import re
# input0 = input("请输入您的密码")
# if re.match(r"^\w{3}\d{3,8}$", input0):
#     print("yes")
# else:
#     print("no")

# [0-9]表示匹配范围是0-9，[0-9a-z]表示匹配范围为0-9和a-z
# if re.match(r"^[0-9a-zA-Z]{1,3}\d{1,10}$", input0):
#     print("yes")
# else:
#     print("no")

# py*表示可以匹配以py开头的任意字符，如py12334455都可
# py.表示可以匹配py开头且加一个任意字符，如py1
# 即*表示匹配*前的那个字符的任意多个都可以，.表示匹配一个任意字符
# 所以.*表示可以匹配任意多个的任意字符
# +表示至少一个字符，?表示0个或者一个字符
# 实例：
# import re
# putin = input("请输入一个字符串")
# # if re.match(r"py*", putin):
# #     print("ok")
# # else:
# #     print("no")
# # if re.match(r"py.$", putin):
# #     print("ok")
# # else:
# #     print("no")
# if re.match(r"[a-z]$", putin):
#     print("ok")
# else:
#     print("no")

# class test:
#     def cFunc(self):
#         print("this is a cFunc")
#     pass

# def func(self):
#     print("this is a function")

# def func1():
#     print("this is a function")

# if __name__ == "__main__":
#     test.addFunc = func
#     t1 = test()
#     t1.addFunc()  # 动态给类添加方法, func需要有self函数以说明该函数是对象调用的而不是类直接调用的函数
#     t1.cFunc = func1  # 动态修改替换类中的方法，其中func1不能有self函数了不然会重复
#     t1.cFunc()
# 列表的使用方法实例：将八个老师随机分配到三个办公室中
# import random
# teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# offices = [[], [], []]

# for name in teachers:
#     # create random number
#     num = random.randint(0, 2)
#     offices[num].append(name)

# i = 1
# for office in offices:
#     print(f"办公室{i}共有老师{len(office)}人，他们分别是{office}")
#     i = i + 1

# 字典的三种遍历方式 ： 1、遍历Key值 2、遍历value值 3、遍历键值对的值（可以通过for循环进行拆包）
# dict = {}
# dict.items()
# dict.keys()
# dict.values()

# 判断元素是否在容器中 in or not in
# print('a' in 'abc')
# list1 = [1, 2, 10]
# print(10 in list1)
# print(10 not in list1)

# 推导式
# 1、字典推导式
# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 18, 'man']
# dict = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict)
# # 2、列表推导式
# list3 = [i for i in range(10)]
# print(list3)
# list3 = [(i, j) for i in range(10) for j in range(5, 15)]
# print(list3)

# 3、字典推导式提取数据
# dict = {1: 1, 2: 2, 3: 3}
# dict1 = {key: value for key, value in dict.items() if value > 2}
# print(dict1)

# 自定义函数说明文档的写法 三引号卸载def下一行即可
# def sum(x, y):
#     """sum up function"""
#     return x+y

# sum1 = sum(1, 2)
# help(sum)
# def test(value):
#     if value < 0:
#         key = 1
#     elif value < 10:
#         key = 2
#     elif value < 20:
#         key = 3
#     return key

# key = test(10)
# print(key)
# 位置参数和关键字参数
# def usrInfo(name, age, gender):
#     print(f"用户的年龄是{age},姓名是{name},性别是{gender}")

# usrInfo(age=10, gender='女', name="小明")  # 指定给哪个参数传哪个值，成为关键字参数赋值法
# usrInfo("小明", 10, "女")  # 根据参数位置赋值，称为位置参数赋值法

# 不定长参数传递的函数

# def test(*args):
#     print(args)
#     print(len(args))

# def test1(**args):
#     print(args)
#     print(len(args))

# test(1, 2, 3, 4)
# test1(name='nihao', age=2, gender='girl')

# 元组和字典拆包

# 元组拆包
# tuple = (1, 2, 3)
# num1, num2, num3 = tuple
# print(num1, num2, num3)
# # 字典拆包
# dict = {'name': 'xiaoli', 'age': 18}
# a, b = dict
# print(a, b)
# # 注意：字典拆包得到的是key值，可以通过dict[key]来获取对于的value值
# python 中交换变量数值的快捷写法
# a, b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b)

# python中所有变量都是一个引用，可以通过id()方法来获取引用指向的内存地址
# # 不可变变量的引用
# a = 1
# b = a
# print(id(a))
# print(id(b))  # 二者都是数据1的地址
# a = 2
# print(id(a))
# print(id(b))  # a变成了数据2的地址，b还是数据1的地址
# # 你会发现在修改a值前 a,b的地址一样，修改a值为2后a的地址变化为新地址，而b的地址还是原来的
# 可变变量的引用

# import os
# import time
# aa = [1, 2]
# bb = aa
# print(id(aa))
# print(id(bb))
# aa.append(3)
# print(id(aa))

# print(id(bb))

# input("请按任意键继续")
# os.system("clear")

# 你会发现从头到尾 aa bb 的地址都没有变化，且修改aa的值后bb的值也会跟着一起变化，因为bb 指向的地址就是aa的，aa和bb都只是一个引用
# 学员管理系统实现

# 功能：
# 1、添加学员
# 2、删除学员
# 3、修改学员信息
# 4、查询学员信息
# 5、显示所有学员信息
# 6、退出系统

# import os


# student_info = []


# def show_info():
#     print("1、add student\n2、delete student\n3、modify student information\n4、find student information\n5、show all information of student\n6、exit\n")


# def check_repeat(type, value):
#     # the first arg is info type, the second arg is actual info value
#     for info in student_info:
#         if info[type] == value:
#             print("student is existed, please enter another")
#             return True
#         else:
#             return False


# def add_info():
#     # input and check
#     name = input("input your name:")
#     while check_repeat("name", name):
#         name = input("input your name:")

#     id = input("input your student_id:")
#     while check_repeat("id", id):
#         id = input("input your student_id:")

#     gender = input("input your gender:")

#     info = {"name": name, "id": id, "gender": gender}
#     student_info.append(info)


# def del_info():
#     name = input("please enter the student name you want to delete:")
#     for info in student_info:
#         if info["name"] == name:
#             del info


# def mod_info():
#     name = input("please enter the student name you want to modify:")
#     for info in student_info:
#         if info["name"] == name:
#             info["name"] = input("please enter new name:")
#             info["id"] = input("please enter new id:")
#             info["gender"] = input("please enter new gender:")


# def find_info():
#     name = input("please enter the student name you want to find:")
#     for info in student_info:
#         if info["name"] == name:
#             print("student_name: %s  student_id: %s  student_gender: %s" %
#                   (info['name'], info["id"], info["gender"]))


# def show_all_info():
#     for info in student_info:
#         print(info['name'], "\t", info["id"], "\t", info["gender"])


# if __name__ == "__main__":
#     while True:
#         show_info()
#         choice = int(input("please input the function number you chose:"))
#         os.system("clear")
#         if choice == 1:
#             add_info()
#         elif choice == 2:
#             del_info()
#         elif choice == 3:
#             mod_info()
#         elif choice == 4:
#             find_info()
#         elif choice == 5:
#             show_all_info()
#         elif choice == 6:
#             exit()
#         input("press random key to continue")
#         os.system("clear")


# abs()函数可以进行绝对值运算，round()函数可以进行四舍五入计算

# map()函数匹配函数与多个参数
# 计算一个列表中所有数的平方
# def func(x):
#     return x**2


# list0 = [1, 2, 3, 4, 5]
# print(map(func, list0))  # 返回一个map对象
# print(list(map(func, list0)))  # 转为一个list对象

# filter 函数过滤出列表中我们需要的元素
# 样例作用：过滤出偶数
# list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def func(x):
#     return x % 2 == 0  # 过滤的条件


# f = filter(func, list0)  # 返回一个filter对象，可以强转为list
# print(f)
# print(list(f))

# seek(偏移字符量，起始位置（0表示开头，1表示当前位置，2表示文件末尾）)方法可以改变文件指针位置，从而可以灵活读取文件内容
# import os
# with open("./file.txt", 'r') as file:
#     file.seek(10, 0)
#     # filelist = file.readlines()
#     # for info in filelist:
#     #     print(info)
#     info = file.read()
#     print(info)
# 备份文件的实践
# import shutil  # shutil可看做是os模块的补充
# import os
# 分离出文件路径+文件名（无后缀）和文件后缀
# file_name = os.path.splitext("./test.txt.mp3.docx")
# print(file_name)
# 分离出目录路径和文件名
# ls = os.path.split("./test.py")
# print(ls)
# file_path = os.path.join("./nihao/wohao", "test.py")  # 做路径的字符串连接，可跨系统
# print(file_path)
# flag = os.path.isabs(file_path)  # 判断是否为绝对路径
# print(flag)
# os.system("pwd")
# file_path1 = "/home/lzc/code/vscode_code/python_code/learnNote/file.txt"
# flag = os.path.isabs(file_path1)  # 判断是否为绝对路径
# print(flag)
# print(os.path.isfile(file_path1))  # 判断是否为文件
# flag = os.path.isdir(file_path1)  # 判断是否为目录
# print(flag)
# flag = os.path.exists(file_path1)  # 判断该路径是否存在
# print(flag)
# shutil.copyfile(file1, file2)  # 将file1复制到file2  注意，两者都是文件路径

# file_path1 = "file.txt"
# index = file_path1.rfind(".")  # 找到该字符在字符串中最后出现的下标
# print(index)
# print(file_path1[:index])  # 从0开始到Index切片
# print(file_path1[index:])  # 从index开始到字符串末尾切片

# 文件读写操作实例作用：备份文件  --> 复制文件
# old_file = input("请输入要备份的文件路径：")
# new_file = input("请输入新的文件路径:")
# # 注意：文件复制一定要以二进制方式打开，才能保证所有种类的文件都可以读取和写入成功
# # 注意：可以采用一次读完，然后再一次性写入的方法，这种方法代码量少但是非常消耗内存。建议使用Buf载体，读一点写一点，使用循环读取完整个文件
# # read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
# with open(old_file, 'rb') as of:
#     with open(new_file, 'wb') as nf:
#         while True:
#             buf = of.read(1024)  # 每次读取1MB
#             print(type(buf))
#             print(len(buf))
#             if len(buf) == 0:
#                 break
#             nf.write(buf)
# import os
# size = os.path.getsize("./file.deb") # 获取文件大小的方法
# print(size)
# import os
# # 注意：rename不仅可以重命名，还可以转移文件，会直接将原文件命名成新名字并且转移到新路径下
# 注意： rename还可以重命名和转移文件夹
# os.rename("/home/lzc/code/vscode_code/python_code/1.deb",
#           "/home/lzc/code/vscode_code/python_code/first/2.deb")
# 所以不需要使用shutil模块的copyfile来复制文件了，直接使用rename复制就可以了
# import os
# # os.remove("file2.txt")
# # 删除文件函数
# os.remove("/home/lzc/code/vscode_code/python_code/first/1.deb")

# import time
# import os
# os.mkdir("./test")
# time.sleep(1)
# os.system("rmdir test") # 直接调用命令行窗口命令删除目录
# os.rmdir("./test")
# cwd = os.getcwd()  # 获取当前工作目录路径
# print(cwd)
# dir_list = os.listdir() # 列出当前路径下的文件名
# print(dir_list)
# python中的文件操作函数与linux命令行中的命令对应
# os.chdir == cd
# os.rmdir == rmdir
# os.mkdir == mkdir
# os.getcwd == pwd
# os.listdir == ls
# 批量重命名文件  1、添加字符，直接用+号即可  2、删除字符 使用字符串切片来删除掉我们不想要的字符

# 类中的方法的参数self指的是调用该函数的对象


# class Washer:
#     # 注意：魔法方法都不需要程序员手动调用，都是系统自动调用的
#     # 魔法方法: 带__前后双下划线的方法成为魔法方法，类中内置了几个魔法方法
#     def __init__(self) -> None:
#         self.height = None
#         self.width = None

#     def __str__(self) -> str:  # 如果定义该函数，打印对象的时候会打印该函数的返回值
#         return 'hello this is magic method'

#     def __del__(self):  # 在对象被释放时自动调用
#         print("nihao")


# wash = Washer()
# # __dict__属性是类和对象都有的，返回类或对象的属性和方法组成的字典
# print(Washer.__dict__)
# print(wash.__dict__)
# class Test:
#     num = 0

#     def __init__(self) -> None:
#         self.num1 = 100

#     def func():
#         print("this is no self function")


# # test1 = Test()  # 称作实例对象
# # test2 = Test()
# # print(Test)
# # print(test1)
# # print(test1.num)
# # test1.func()  # 报错！ 注意不带self参数的方法实例对象是不能访问的，会报错，因为实例对象调用方法时会自动给函数传参self，如果该方法定义时无self则会报错
# # # 所以，不带self参数的方法只能由类对象调用
# # Test.func()
# # print(Test.num)  # 这里的Test也称作类对象，实例对象是由类对象创建而来的
# # # print(Test.num1)  # 报错，类定义中带有self关键字的属性只有实例对象才能访问，而不带self关键字的属性类对象和实例对象均可访问
# # del Test  # 实例对象创建后就不依赖于类对象了，就算类对象被删除，实例对象依然存在且可以使用

# # print(test1.num)
# print(Test.mro())
# 类名.mro()方法可以查看当前类的继承情况

# 继承
# 现在的版本默认没有写父类的类都会继承object类
# 单继承  easy 继承后子类会拥有父类的所有属性和方法（能不能访问是一回事，但是都继承了）
# 多继承
# class Master:
#     def __init__(self) -> None:
#         self.kongfu = "祖传煎饼果子"

#     def make_cake(self):
#         print(f"使用{self.kongfu}做煎饼果子")


# class School:
#     def __init__(self) -> None:
#         self.kongfu = "老师教的煎饼果子"

#     def make_cake(self):
#         print(f"使用{self.kongfu}做煎饼果子")


# class Apprentice(Master, School):  # 继承了Master 和 School
#     pass
# # 如果继承的两个类中方法重名，那么会优先继承的第一个类的方法而不继承后面的类的同名方法
# pupil = Apprentice()
# print(pupil.kongfu)
# class Apprentice(Master, School):
#     def __init__(self) -> None:
#         super().__init__()
#         self.kongfu = "独创煎饼果子"

#     def make_cake(self):
#         self.__init__()  # 一定要再调用一次自己的初始化以确保kongfu中的值是我自己的值，不然kongfu的值是会被其他父类的初始化函数修改的
#         # 一个收获： python中类的构造函数是能被反复调用的
#         print(f"使用{self.kongfu}做煎饼果子")  # 子类中重写父类方法，则子类方法会覆盖原父类方法
#         # return super().make_cake()

#     def make_Master_cake(self):
#         Master.__init__(self)  # 使用父类初始化函数修改self自身属性的值
#         Master.make_cake(self)


# pupil = Apprentice()
# pupil.make_cake()
# pupil.make_Master_cake()

# 大于两层的继承关系叫做多层继承，python允许多层继承，都可以继承下来

# super用来调用继承多个类的
# class Master:
#     def __init__(self) -> None:
#         self.kongfu = "祖传煎饼果子"

#     def make_cake(self):
#         print(f"使用{self.kongfu}做煎饼果子")


# class School:
#     def __init__(self) -> None:
#         self.kongfu = "老师教的煎饼果子"

#     def make_cake(self):
#         print(f"使用{self.kongfu}做煎饼果子")


# class Apprentice(Master, School):
#     def __init__(self) -> None:
#         # super().__init__()
#         self.kongfu = "独创煎饼果子"

#     def make_cake(self):
#         self.__init__()  # 一定要再调用一次自己的初始化以确保kongfu中的值是我自己的值，不然kongfu的值是会被其他父类的初始化函数修改的
#         # 一个收获： python中类的构造函数是能被反复调用的
#         print(f"使用{self.kongfu}做煎饼果子")  # 子类中重写父类方法，则子类方法会覆盖原父类方法
#         # return super().make_cake()

#     def make_Master_cake(self):
#         Master.__init__(self)  # 使用父类初始化函数修改self自身属性的值
#         Master.make_cake(self)

#     def make_both(self):
#         super().__init__()  # 注意：此处super()为 super(Apprentice, self)的简写，由于super会自动查找，故我们不用写了，但是这时不要再给init()传self了，因为super()已经传过了
#         super().make_cake()
#         # 注意：继承两个类后，super默认是第一个类的，后面的类不管


# pupil = Apprentice()
# pupil.make_both()  # 结果只能make一个，只能make第一个类的
# super用来解决多层继承的
# class Master:
#     def __init__(self) -> None:
#         self.kongfu = "祖传手艺"

#     def make_cake(self):
#         print(f"用{self.kongfu}做的")


# class School(Master):
#     def __init__(self) -> None:
#         self.kongfu = "老师手艺"

#     def make_cake(self):
#         print(f"用{self.kongfu}做的")
#         super().__init__()  #再调用祖传手艺
#         super().make_cake()


# class Apprentice(School):
#     def __init__(self) -> None:
#         self.kongfu = "徒弟手艺"

#     def make_cake(self):
#         print(f"用{self.kongfu}做的")
# # 层层往上调用的方式使得能一下调用完
#     def make_tradition(self):
#         super().__init__() # 调用老师手艺
#         super().make_cake()


# pupil = Apprentice()
# pupil.make_tradition()

# 私有属性写法 __变量名  在变量名前加上两道下划线即是私有属性
# 私有方法写法 __方法名  也是加两道下划线
# 私有属性获取修改方法： 只能类内访问和修改，不能类外访问修改，一般在类内定义 get_xx 和set_xx 来分别进行获取私有属性和修改私有属性的操作

# 多态样例
# class Dog:
#     def work(self):
#         pass


# # 子类重写父类方法
# class ArmDog(Dog):
#     def work(self):
#         print("追击敌人")


# class DrugDog(Dog):
#     def work(self):
#         print("追查毒品")


# # 调用狗工作函数，通过传入对象不同调用不同的函数
# class Person():
#     def do_with_dog(self, dog):
#         dog.work()


# person = Person()
# person.do_with_dog(ArmDog())
# 类属性只能由类对象来修改，如果由实例对象修改类属性，那么相当于给实例添加了一个与类属性同名的实例属性（python的动态添加属性）
# 类属性为类对象和所有实例对象所共有，类属性一旦修改后，所有人共用的都会被修改，和Java中的静态变量一个意思
# class obj:
#     tooth = 100


# t1 = obj()
# t2 = obj()
# print(t1.tooth)
# print(t2.tooth)
# print(obj.tooth)
# t1.tooth = 10
# print(t1.tooth)  # 10
# print(t2.tooth)  # 100
# print(obj.tooth) # 100
# obj.tooth = 10
# print(t1.tooth)
# print(t2.tooth)
# print(obj.tooth)

# 类方法：用装饰器@classmethod修饰， 一般用于操作类属性
# class obj:
#     __tooth = 100   # 定义私有类属性

#     @classmethod   # 装饰器用于告诉解释器给该函数自动传参，参数为类对象本身。实例对象是会自动传递的，但是类对象不会，需要程序员手动告知
#     def get_tooth(cls):  # 类方法也需要传参，和self类似，但是一般习惯于使用cls 做参数 （class简写）
#         return cls.__tooth  # 获取私有类属性

#     def test1():
#         print("test1")

#     @staticmethod  # 静态方法装饰器，用于告诉解释器不要将实例对象自己传参给该方法
#     def test2():
#         print("test2")


# t1 = obj()
# print(t1.get_tooth())
# print(obj.get_tooth())

# 注意：类方法实例对象也可以调用，和类属性一样   同名的实例属性会覆盖类属性
# t1.test1()  如果不加静态方法装饰器，那么实例对象调用时由于会传参导致出错

# t1.test2()
# obj.test1()
# obj.test2()

# 异常：
# try:
#     可能会发生异常的语句
# except:
#     发生异常后执行的语句
# 捕获异常：如果发生的异常类型与我们设置的不同，则不会执行except中的代码
# try:
#     可能会发生异常的语句
# except 异常类型 :
#     捕获到该类型异常后才执行的代码

# 捕获多个异常
# try:
#     可能会发生异常的语句
# except （异常类型1，异常类型2） :
#     捕获到该类型异常后才执行的代码

# 捕获异常描述信息
# try:
#     可能会发生异常的语句
# except （异常类型1，异常类型2）as result :   # 这里会将捕获的异常的描述信息传给result,打印result即可得到异常描述信息了
#           print(result)

# 捕获所有异常  通过所有程序异常类的父类Exception来操作
# try:
#     可能会发生异常的语句
# except Exception as result :
#           print(result)  #即可打印所有异常描述信息了


# import os
# try:
#     f = open("123.txt", "r")  # 发现异常，直接跳转到except，从而不会执行下面那个有异常的语句了
#     print(num)
# except Exception as result:
#     print(result)

# try:
#     可能会发生异常的语句
# except:
#     发生异常后执行的语句
# else:
#     如果try中没有发生异常，则执行完try后会执行else中的代码

# finally 表示无论是否发生异常都要执行的代码
# try:
#     可能会发生异常的语句
# except:
#     发生异常后执行的语句
# else:
#     如果try中没有发生异常，则执行完try后会执行else中的代码
# finally：
#     上面三项结束后最后需要执行的代码   常用于关闭文件


# try:
#     a = 1/0
# except Exception as result:
#     print(result)
#     print(type(result))  # 注意： result是一个异常类
# finally:
#     print("异常捕获成功")

# 自定义异常  使用raise关键字抛出异常  样例目的：检测输入的密码长度是否大于三


# class ShortPassWordError(Exception):  # 注意要继承Exception父类才可
#     minlen = 3

#     def __init__(self, inLen):
#         self.len = inLen

#     def __str__(self) -> str:   # 异常描述原理就是采用打印异常类从而调用魔法方法__str__来显示异常说明， except Exception as result 中的result就是捕获到的异常类
#         return f"ShrotPassWordError:您输入的密码长度为{self.len}位,输入的密码长度不应小于{self.minlen}位"


# while True:
#     try:
#         pwd = input("请输入您的密码")
#         if len(pwd) < ShortPassWordError.minlen:
#             raise ShortPassWordError(len(pwd))
#     except Exception as result:
#         print(result)
#     else:
#         print("密码输入已完成")
#         break
# 导入模块的方法
# 1、import 模块名
# 2、from 模块 import 功能名   区别是如果用第二种方法导入，那么使用功能时就可以直接用，而不用像 模块名.功能名 这种样子使用了
# 实例
# import math
# print(math.sqrt(9))
# from math import sqrt
# print(sqrt(9))
# from math import *  # 导入模块中的所有功能，且调用时不再需要写“模块名.”了
# print(sqrt(9))
# 为导入的模块或者功能起别名 as关键字 注意：起别名后就只能使用别名了，原来的名字失效
# 语法：
# import 模块名 as 别名
# from 模块名 import 功能 as 别名
# from time import sleep as sl
# import time as t
# t.sleep(1)
# sl(1)
# import my_module_1
# 当你导入一个模块，Python解析器对模块位置的搜索顺序是：
# ● 当前目录
# ● 如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
# ● 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH是由安装过程决定的默认目录


# 每个模块都有一个属性 __all__ 这是一个列表，放置了该模块的功能名
# 使用from 模块名 import * 时导入的时__all__列表中的所有功能，也就是说如果修改__all__，那么就不能通过*来完全
# 导入模块中的所有功能了。但是__all__列表中默认放置了该模块的所有功能名
# # 一般的，我们可以通过打印__all__列表来查看一个模块的所有功能
# import os.path
# print(os.path.__all__)
# 注意： __name__属性  当当前模块自己运行时，__name__的值为__main__，当当前模块被别人调用时，__name__的值为模块名字
# 故在模块中可以使用
# if __name__ == "__main__":
#     语句来放置模块功能测试代码，以达到只有在主动运行模块时才会被执行，而模块被别人调用时不会执行这些测试代码
# python包的介绍
# 包：是多个功能相近的模块组成的文件夹，此文件夹中必须有一个__init__.py文件和多个模块
# 导入包的方法： 1、import 包名.模块名 (不推荐，调用功能时前缀太长)
#  2、from 包名 import * 可以导入包中的多个模块且调用时不需要"包名."前缀
#  3、from 包名 import 模块名  （推荐使用2 3 方法导入自定义包内的模块）
# 但是方法2必须要在__init__.py中设置__all__列表来控制*导入的模块名
# import my_package  # 单独书写无意义
# from my_package import *
# from my_package import my_module_2
# my_module_2.print_info()
# 不推荐的写法：
# import my_package.my_module_2
# my_package.my_module_2.print_info()


# python基础语法学习至此结束 今天是2022.8.3
