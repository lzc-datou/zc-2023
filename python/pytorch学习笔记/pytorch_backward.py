import torch
import matplotlib.pyplot as plt
# x_data = [1, 3, 5, 8, 10, 20, 40, 60]
# y_data = [2, 3, 7, 9, 10, 20, 30, 50]
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.tensor([1.0])  # 初始化w为tensor 其中这里的张量就是一个向量 [1.0]
w.requires_grad = True

# 两个函数构建计算图,返回值均是一个tensor

torch.Tensor


def forward(x):
    return w*x


def loss(x, y):
    y_pre = forward(x)
    return (y-y_pre)**2


loss_list = []
times_list = []
for time in range(100):
    print("time=", time)
    for x, y in zip(x_data, y_data):
        ls = loss(x, y)
        ls.backward()
        print("\tgrad=", w.grad.item())
        w.data = w.data - 0.01*w.grad.data
        print("\tw=", w.data)
        w.grad.data.zero_()  # 清空梯度值

    loss_list.append(ls.data)
    times_list.append(time)
    print("\tloss=", ls)


print('w=', w)
plt.plot(times_list, loss_list)
plt.xlabel("time")
plt.ylabel("loss")
plt.show()
