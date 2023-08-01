'''
程序功能：使用MNIST手写数字数据集训练LetNet网络，获取相应权重文件
使用方法：运行时在命令行使用python3单独运行此文件即可
'''
import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision
from LetNet import LetNet5

# 加载数据
def data_loader(batch_size):

    # 将数据类型转换成tensor的函数
    transform = torchvision.transforms.ToTensor()

    train_set = torchvision.datasets.MNIST(root='./', train=True, transform=transform, download=True)
    train_loaders = torch.utils.data.DataLoader(dataset=train_set, batch_size=batch_size, shuffle=True, num_workers=16)

    test_set = torchvision.datasets.MNIST(root='./', train=False, transform=transform, download=True)
    test_loaders = torch.utils.data.DataLoader(dataset=test_set, batch_size=batch_size, shuffle=False, num_workers=16)

    return train_loaders, test_loaders

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 使用MNIST数据集训练
def train(model, learn_rate, train_loaders, epoch):

    # 优化器
    optimizer = torch.optim.Adam(model.parameters(), learn_rate)
    # 损失函数
    loss_fun = nn.CrossEntropyLoss()
    

    for i in range(epoch):
        running_loss = 0.0
        for j, (x, y) in enumerate(train_loaders):
            # 将训练数据转到GPU上
            x = x.to(device)
            y = y.to(device)

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
    path = '../weights/model_32_800.pth'
    torch.save(model.state_dict(), path)
    print(path)
    print("Finished training")

# 使用MNIST数据集的测试部分测试训练效果
def test(model, test_loaders):

    correct = 0
    total = 0
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # # 使用已训练好的权重
    # model_path = "./model/model.pth"
    # model.load_state_dict(torch.load(model_path,map_location=device))
    
    for datas in test_loaders:
        images, labels = datas
        labels = labels.to(device)
        images = images.to(device) # 将测试数据转到GPU上
        images = Variable(images)
        
        outputs = model(images)
        outputs = outputs.to(device)
        # predicted = torch.max(outputs, 1)[1].data.numpy().squeeze()
        predicted = torch.max(outputs.data, 1)[1]
        _, pred = torch.max(outputs,dim=1)
        print(pred)
        total += labels.size(0)
        correct += (predicted == labels).sum()

    # print(total, correct)
    print('Accuracy of the network on the 10000 test images: %.2f %%' % (
            100 * correct / total))

if __name__ == "__main__":
    let = LetNet5()
    let = let.to(device) # 将模型转到gpu上训练（如果没有，则使用cpu）
    # 训练时一次看几张图片
    batch_size = 32
    # 学习率（修正网络参数的快慢）
    learn_rate = 0.00001
    # 训练的轮数
    epoch = 800
    # 加载训练和测试使用的数据集
    train_loader, test_loader = data_loader(batch_size)
    # 训练
    train(let, learn_rate, train_loader, epoch)
    # 测试训练效果（10000张图片来测试）
    test(let, test_loader)