import sys
# 杨辉三角的生成器


def triangles(line):
    if line <= 0:
        print("input wrong")
    if line >= 1:
        l = [1]
        # 首先确定每一行的长度
        for len in range(1, line+1):
            # 行数为1，2时直接产出结果
            if len == 1:
                l = [1]
                yield l
            elif len == 2:
                l = [1, 1]
                yield l
            # 行数大于三时，靠循环来生成
            elif len >= 3:
                # l存了上一行的数据，l1是待生成的这一行的数据，l1是一个临时变量
                l1 = []
                for n in range(1, len+1):
                    # 每行第一个数赋值为1
                    if n == 1:
                        l1.append(1)
                        n = n+1
                    # 每行第n个数等于上一行第n个数加上一行第n-1个数
                    elif n >= 2 and n != len:
                        number = l[n-1]+l[n-2]
                        l1.append(number)
                        n = n+1
                    # 每行最后一个数也赋值为1
                    elif n == len:
                        l1.append(1)

                l = l1
                yield l

# 杨辉三角打印函数


def printTri(line):
    # 标识打印的行数 从第0行开始
    n = line
    for tri in triangles(line):
        for i in range(0, n):
            print(" ", end='')

        for x in tri:
            print(x, end='')
            print(" ", end='')

        print('')
        n = n - 1


# 接收命令行输入参数进行打印
printTri(int(sys.argv[1]))
