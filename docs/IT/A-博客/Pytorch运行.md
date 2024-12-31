# 我的环境
```
版本	Windows 10 专业版
版本号	22H2
安装日期	‎2023/‎12/‎19
操作系统内部版本	19045.4651
体验	Windows Feature Experience Pack 1000.19060.1000.0
```
```
设备名称	ZL-20231219TEWC
处理器	12th Gen Intel(R) Core(TM) i7-12700   2.10 GHz
机带 RAM	16.0 GB (15.7 GB 可用)
设备 ID	DAD38684-CCF4-42C7-AC51-9C39AC2C1C3E
产品 ID	00331-10000-00001-AA346
系统类型	64 位操作系统, 基于 x64 的处理器
笔和触控	没有可用于此显示器的笔或触控输入
```

# 安装anaconda
略

- 创建pytorch运行环境
```
# 需要指定3.9的版本，否则会报错dll的错：OSError: [WinError 126] 找不到指定的模块。 Error loading "C:\Users\zlzk\anaconda3\envs\myenv\Lib\site-packages\torch\lib\fbgemm.dll" or one of its dependencies.

打开Anaconda Prompt
$ conda create -n py39 python=3.9
$ conda activate py39
```

# main.py文件
```python
## https://gitee.com/kongfanhe/pytorch-tutorial/blob/master/test.py#
# torch==2.4.0
# torchvision==0.19.0
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt

class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 64)
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc3 = torch.nn.Linear(64, 64)
        self.fc4 = torch.nn.Linear(64, 10)

    def forward(self, x):
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1)
        return x

def get_data_loader(is_train):
    to_tensor = transforms.Compose([transforms.ToTensor()])
    data_set = MNIST("", is_train, transform=to_tensor, download=True)
    return DataLoader(data_set, batch_size=15, shuffle=True)

def evaluate(test_data, net):
    n_correct = 0
    n_total = 0
    with torch.no_grad():
        for (x, y) in test_data:
            outputs = net.forward(x.view(-1, 28*28))
            for i, output in enumerate(outputs):
                if torch.argmax(output) == y[i]:
                    n_correct += 1
                n_total += 1
    return n_correct / n_total

def main():
    train_data = get_data_loader(is_train=True)
    test_data = get_data_loader(is_train=False)
    net = Net()
    
    print("initial accuracy:", evaluate(test_data, net))
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    for epoch in range(2):
        for (x, y) in train_data:
            net.zero_grad()
            output = net.forward(x.view(-1, 28*28))
            loss = torch.nn.functional.nll_loss(output, y)
            loss.backward()
            optimizer.step()
        print("epoch", epoch, "accuracy:", evaluate(test_data, net))

    for (n, (x, _)) in enumerate(test_data):
        if n > 3:
            break
        predict = torch.argmax(net.forward(x[0].view(-1, 28*28)))
        plt.figure(n)
        plt.imshow(x[0].view(28, 28))
        plt.title("prediction: " + str(int(predict)))
    plt.show()

if __name__ == "__main__":
    main()
```

pip install torch==2.4.0
pip install torchvision==0.19.0
python main.py
即可


## 问题
- 过程能可视化吗？
    - torchviz

