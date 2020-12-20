import os

import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import transforms


class SAMPLE_DNN(nn.Module):
    def __init__(self, cfg):
        super(SAMPLE_DNN, self).__init__()
        self.model = nn.Sequential(nn.Linear(28 * 28, cfg.model.node1),
                               nn.ReLU(),
                               nn.Linear(cfg.model.node1, cfg.model.node2),
                               nn.ReLU(),
                               nn.Linear(cfg.model.node2, 10))

    def forward(self, x):
        return self.model(x.view(x.size(0), -1))