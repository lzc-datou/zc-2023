from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt

x_data = [1, 3, 5, 8, 10, 20, 40, 60]
y_data = [2, 1, 3, 9, 0, -1, 30, 0]

# 线性模型


def expect(w, x):
    return w*x


# 获取平均误差值(针对每一个w值，都算一遍它的误差值)
def cost(w):
    cost = 0

    for x, y in zip(x_data, y_data):
        y_pre = w*x
        loss = (y-y_pre)**2
        cost += loss

    return cost/len(x_data)

# 计算误差函数的梯度值，找到梯度最小点，即是最优点


def grad(w):
    grad_sum = 0
    for x, y in zip(x_data, y_data):
        grad = 2*x*(w*x - y)
        grad_sum += grad
    return grad_sum/len(x_data)


# 画出平均误差和训练次数的函数图
times_list = []
cost_list = []
w_list = []

# 先设置w初值（猜测的）
w = 2
# 先训练一百次
for time in range(100):
    # 注意：函数名不要和变量名一致，不然会出错，我这里吃亏在这个上面了
    w_list.append(w)
    print("(before)w=", w)
    cost_val = cost(w)  # 计算误差值
    grad_val = grad(w)
    times_list.append(time)
    cost_list.append(cost_val)
    w = w - 0.0001*grad_val  # 通过梯度调整w值

    # 打印日志信息
    print("time=", time)
    print("\t", 'w=', w, '  ', 'grad=', grad_val)
    print("\t", 'cost=', cost_val)

# 获取最小误差值，及其对应的w值和训练次数
min_cost = min(cost_list)
pos = cost_list.index(min_cost)
# convergent：收敛
cvg_time = times_list[pos]
best_w = w_list[pos]
print("cvb_time=", cvg_time)
print("min_cost=", min_cost)
print("best_w=", best_w)
plt.plot(times_list, cost_list)
plt.xlabel("times")
plt.ylabel("cost")
plt.show()
