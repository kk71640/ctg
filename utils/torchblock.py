import torch
import torch.nn as nn

# ct: ConvTranspose2d
# cv: Conv2d
# ln: Linear
# bn2d: BatchNorm2d
# bn1d: BatchNorm1d
# rl: ReLU
# l_rl: LeakyReLU
# tn: Tanh

def Block(settings, in_channels, out_channels, kernel_size=1, stride=1, padding=0, dilation=1, bias=False):
    modules = {
        'ct': nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding),
        'cv': nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, bias=bias),
        'ln': nn.Linear(in_channels, out_channels),
        'bn': nn.BatchNorm2d(out_channels),
        'bn1d': nn.BatchNorm1d(out_channels),
        'rl': nn.ReLU(inplace = True),
        'l_rl': nn.LeakyReLU(0.1, inplace = True),
        'tn': nn.Tanh(),
        'sg': nn.Sigmoid(),
        'mp': nn.MaxPool2d(kernel_size, stride, padding)
          
    }

    return nn.Sequential(*list(map(lambda x: modules[x], settings)))
