import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as data
import torchvision
import os
import cv2
from PIL import Image
class CNN(nn.Module):

    def __init__(self):

        # 调用父类的构造函数
        super(CNN, self).__init__()
        # 第一层卷积池化， Sequential内的函数顺序执行
        # 原文中激活函数都是用的sigmoid，这里使用更好的ReLu
        self.conv_pool1 = nn.Sequential(
            nn.Conv2d(in_channels=1,        # input (1, 28, 28) padding to(1,32,32)
                                            # 这里的input和output的值都是针对一个样本来说的，而训练时是一次输入一个batch
                      out_channels=6,
                      kernel_size=(5, 5),
                      padding=2),           # output(6, 28, 28)
            nn.ReLU(),                      # 激活函数
            nn.MaxPool2d(2, stride=2)                 # output(6, 14, 14)
        )

        self.conv_pool2 = nn.Sequential(
            nn.Conv2d(in_channels=6,
                      out_channels=16,
                      kernel_size=(5, 5)
                      ),                            # output(16, 10, 10)
            nn.ReLU(),
            nn.MaxPool2d(2, stride=2)             # output(16, 5, 5)
        )

        # 全连接层
        self.fc1 = nn.Sequential(                   # 这里用全连接层代替原文的卷积层
            nn.Linear(16*5*5, 120),
            nn.ReLU()
        )

        # 全连接层
        self.fc2 = nn.Sequential(
            nn.Linear(120, 84),
            nn.ReLU()
        )
        # 输出层
        self.out = nn.Sequential(
            nn.Linear(84, 10),

        )

    # 前向传播
    def forward(self, x):

        x = self.conv_pool1(x)
        x = self.conv_pool2(x)
        x = x.view(-1, 16*5*5)       # resize to 2-dims(batch_size, 16*5*5) 展平成1维
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.out(x)
        return x

class MyDataSet():
    pass









# 加载数据
def data_loader(batch_size):

    # 将数据类型转换成tensor的函数
    transform = torchvision.transforms.ToTensor()

    train_set = torchvision.datasets.MNIST(root='minist', train=True, transform=transform, download=True)
    train_loaders = torch.utils.data.DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True, num_workers=2)

    test_set = torchvision.datasets.MNIST(root='minist', train=False, transform=transform, download=True)
    test_loaders = torch.utils.data.DataLoader(dataset=test_set, batch_size=batch_size, shuffle=False, num_workers=2)

    return train_loaders, test_loaders


def train(model, learn_rate, train_loaders, epoch):

    # 优化器
    optimizer = torch.optim.Adam(model.parameters(), learn_rate)
    # 损失函数
    loss_fun = nn.CrossEntropyLoss()
    

    for i in range(epoch):
        running_loss = 0.0
        for j, (x, y) in enumerate(train_loaders):

            x = Variable(x, requires_grad=True)     # x是一个batch_size个的样本
            y = Variable(y)
            optimizer.zero_grad()                   # 将前一次的梯度清0
            out = model(x)                          # 前向传播
            loss = loss_fun(out, y)                 # 计算误差
            loss.backward()                         # 反向传播计算梯度
            optimizer.step()                        # 更新参数

            running_loss += loss
            # print(loss[0])
            if (j+1) % 200 == 0:  # print every 200 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (i + 1, j + 1, running_loss/200))
                running_loss = 0.0

    torch.save(model.state_dict(), 'model/model_1.pth')
    print("Finished training")


def test(model, test_loaders):

    correct = 0
    total = 0
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # # 使用已训练好的权重
    # model_path = "./model/model.pth"
    # model.load_state_dict(torch.load(model_path,map_location=device))
    
    for datas in test_loaders:
        images, labels = datas

        images = Variable(images)

        outputs = model(images)
        # predicted = torch.max(outputs, 1)[1].data.numpy().squeeze()
        predicted = torch.max(outputs.data, 1)[1]
        _, pred = torch.max(outputs,dim=1)
        print(pred)
        total += labels.size(0)
        correct += (predicted == labels).sum()

    # print(total, correct)
    print('Accuracy of the network on the 10000 test images: %.2f %%' % (
            100 * correct / total))

def detect_num(model,num_img):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 使用已训练好的权重
    model_path = "./model/model_1.pth"
    model.load_state_dict(torch.load(model_path,map_location=device))
    transf = torchvision.transforms.ToTensor()
    num_img = transf(num_img)
    num_img = Variable(num_img)
    outputs = model(num_img)
    predicted = torch.max(outputs.data, 1)[1]
    num = int(predicted)
    return num
    

if __name__ == '__main__':
    # cnn = CNN()
    # # 遍历0-9共10个数据集，验证识别效果
    # for i in range(10):
    #     img_path = "./dataset/" + str(i) + "/"
    #     img_list = os.listdir(img_path)
    #     num_dict = dict()
    #     for img_name in img_list:
    #         img = cv2.imread(img_path+img_name,cv2.IMREAD_GRAYSCALE)
        
    #         img = cv2.resize(img,(28,28))
    #         num = detect_num(cnn,img)
    #         if  str(num) in num_dict:
    #             num_dict[str(num)] = num_dict[str(num)] + 1
    #         else:
    #             num_dict[str(num)] = 1
    #     max_value = max(num_dict.values())
    #     for key,value in num_dict.items():
    #         if value == max_value:
    #             print(key,value)


        
    

    cnn = CNN()
    # 加载模型
    # path = 'model/model.pth'
    # cnn.load_state_dict(torch.load(path))
    # print(cnn)
    batch_size = 4
    learn_rate = 0.001
    epoch = 20
    train_loader, test_loader = data_loader(batch_size)
    train(cnn, learn_rate, train_loader, epoch)
    test(cnn, test_loader)

