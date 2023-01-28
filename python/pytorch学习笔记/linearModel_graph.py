import numpy as np
import matplotlib.pyplot as plt

x_data = [1, 3, 5, 8, 10, 20, 40, 60]
y_data = [2, 3, 7, 9, 10, 20, 30, 50]

# 期望值


def expect(w, x):
    return w*x


def loss(epY, y):
    return (epY-y)**2


w_list = []
mse_list = []

for w in np.arange(-4, 4, 0.1):
    print("w=", w)
    w_list.append(w)
    loss_sum = 0
    for x_val, y_val in zip(x_data, y_data):
        y_pre = expect(w, x_val)
        loss_val = loss(y_pre, y_val)
        print("\t", x_val, " ", y_val, " ", y_pre, " ", loss_val)
        loss_sum = loss_sum+loss_val
    mse = loss_sum / len(x_data)
    mse_list.append(mse)
    print("mse=", mse)
plt.plot(w_list, mse_list)
plt.xlabel("w")
plt.ylabel("mse")
plt.show()
