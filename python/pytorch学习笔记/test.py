# import torch
# x_data = torch.tensor([[1.0], [2.0], [3.0]])
# y_data = torch.tensor([[2.0], [4.0], [6.0]])


# class LinearModel(torch.nn.Module):
#     def __init__(self) -> None:
#         super().__init__()
#         self.linear = torch.nn.Linear(1, 1)

#     def forward(self, x):
#         y_pre = self.linear(x)
#         return y_pre


# model = LinearModel()
# criterion = torch.nn.MSELoss(size_average=True)
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# for time in range(1000):
#     y_pre = model(x_data)
#     loss = criterion(y_pre, y_data)
#     print("time = ", time, "loss=", loss.data)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
# print("w=", model.linear.weight.item())
# print("b=", model.linear.bias.item())

# x_test = torch.tensor([4.0])
# y_pre = model(x_test)
# print("y_pre = ", y_pre.data)
# import numpy as np
# xy = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# xy = np.array(xy)
# print(xy)
# print(xy[:, [-1]])
# x = range(100)

# for i, data in enumerate(x, 1):
#     print('i = ', i)
#     print("data = ", data)

from numpy import random
a = random.rand(3, 3, 3)
print(a)
