import torch
from torch.nn import functional as F

import torch.nn as nn

class Conv_Block(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Conv_Block, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(in_channels, in_channels, kernel_size=15, stride=1, padding=7, bias=False),
            nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.Dropout(0.3),
            nn.ReLU(),
            nn.Conv2d(out_channels, out_channels, kernel_size=15, stride=1, padding=7, bias=False),
            nn.Conv2d(out_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.Dropout(0.3),
            nn.ReLU()
        )


    def forward(self, x):
        return self.layer(x)


class Down(nn.Module):
    def __init__(self, channel):
        super(Down, self).__init__()
        self.layer = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(channel),
            nn.ReLU()
        )
    def forward(self,x):
        return self.layer(x)


class Up(nn.Module):
    def __init__(self,channel):
        super(Up, self).__init__()
        self.layer=nn.Conv2d(channel,channel//2,kernel_size=1,stride=1)
    def forward(self,x,feature_map):
        up=F.interpolate(x,scale_factor=2,mode='nearest')
        out=self.layer(up)
        return torch.cat((out,feature_map),dim=1)
class Unet(nn.Module):
    def __init__(self):
        super(Unet, self).__init__()
        self.c1=Conv_Block(3,64)
        self.d1=Down(64)
        self.c2=Conv_Block(64,256)
        self.d2=Down(256)
        self.c3=Conv_Block(256,512)
        self.d3=Down(512)
        self.c4=Conv_Block(512,1024)
        self.d4=Down(1024)
        self.c5=Conv_Block(1024,1024)
        self.u1=Up(1024)
        self.c6=Conv_Block(1024,256)
        self.u2=Up(256)
        self.c7=Conv_Block(256,128)
        self.u3=Up(128)
        self.c8=Conv_Block(128,64)
        self.u4=Up(64)
        self.c9=Conv_Block(64,16)
        self.out=nn.Conv2d(16,3,kernel_size=3,stride=1,padding=1)
        self.Th=nn.Sigmoid()

    def forward(self,x):
        R1=self.c1(x)
        R2=self.c2(self.d1(R1))
        R3 = self.c3(self.d2(R2))
        R4 = self.c4(self.d3(R3))
        R5 = self.c5(self.d4(R4))
        O1=self.c6(self.u1(R5,R4))
        O2 = self.c7(self.u2(O1, R3))
        O3 = self.c8(self.u3(O2, R2))
        O4 = self.c9(self.u4(O3, R1))

        return self.Th(self.out(O4))

if __name__ == '__main__':
    x=torch.randn(2,3,256,256)
    net=Unet()
    print(net(x).shape)