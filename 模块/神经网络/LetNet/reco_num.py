import sys
# # 新增包含路径
# sys.path.append()
import torch
from torch.autograd import Variable
import torchvision
import os
import cv2
from LetNet import LetNet5

# 识别数字 recognize number
def reco_num(model,num_img):
    
    # 训练好的权重路径
    model_path = "./model/best.pth"
    # 加载该权重到模型
    model.load_state_dict(torch.load(model_path,map_location=device))

    # 把图片变成可以在网络中传递的变量
    transf = torchvision.transforms.ToTensor() # 实例化类
    num_img = transf(num_img) # 变成张量
    num_img = Variable(num_img) # 使之可求梯度
    
    # 获得网络输出，注意：网络输出不直接是数字
    outputs = model(num_img)
    # 将网络输出变成具体数字
    predicted = torch.max(outputs.data, 1)[1]
    num = int(predicted)
    return num
    


if __name__ == '__main__':
    # 如果有cuda，就用cuda，否则使用cpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    let = LetNet5()
    # 遍历0-9共10个数据集，验证识别效果
    for i in range(10):
        img_path = "./dataset/" + str(i) + "/"
        img_list = os.listdir(img_path)
        num_dict = dict()
        for img_name in img_list:
            # 识别单张图片

            # 读取成灰度图
            img = cv2.imread(img_path+img_name,cv2.IMREAD_GRAYSCALE)
            # 调整大小为28*28 送入网络识别
            img = cv2.resize(img,(28,28))
            # 识别数字
            num = reco_num(let,img)

            #识别单张图片结束
            if  str(num) in num_dict:
                num_dict[str(num)] = num_dict[str(num)] + 1
            else:
                num_dict[str(num)] = 1
        max_value = max(num_dict.values())
        for key,value in num_dict.items():
            if value == max_value:
                print(key,value)
