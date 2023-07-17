# 安装gpu版torch与torchvision
> 2023.6.26  

安装目的主要是为了能在有独立显卡（N卡）的电脑上运行代码和训练神经网络

**pip安装的torch与torchvision一般默认是cpu版本的，如果想要使用gpu加速，需要单独上官网下载对应版本的torch与torchvision**

1. 上官网选择好版本后，按照官网提供的命令下载即可。[pytorch官网](https://pytorch.org/get-started/locally/)
2. 分别下载版本相互匹配的torch与torchvision。见[网站](https://download.pytorch.org/whl)。值得注意的是torch与torchvision的命名方式。
    - torch-1.10.2+cpu-cp36-cp36m-win_amd64.whl  其中cpu表示cpu版本的torch，cp36表示python3.6,win表示windows版
    - torch-1.7.1+cu101-cp37-cp37m-win_amd64.whl  其中cu101表示cuda 10.1版本，为gpu版本的torch, cp37表示python3.7
    - torchvision的命名方式与torch类似，注意torch的cu101和cp37需要与torchvision匹配方可正常工作
3. 注意，下载的torchvision为`.whl`文件，该文件可以使用`pip3 install .whl`命令直接安装torchvision
