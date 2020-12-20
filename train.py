import os
import sys
from omegaconf import DictConfig, ListConfig

import hydra
from hydra import utils
import mlflow
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader, random_split

from model import SAMPLE_DNN


def log_params_from_omegaconf_dict(params):
    for param_name, element in params.items():
        _explore_recursive(param_name, element)

def _explore_recursive(parent_name, element):
    if isinstance(element, DictConfig):
        for k, v in element.items():
            if isinstance(v, DictConfig) or isinstance(v, ListConfig):
                _explore_recursive(f'{parent_name}.{k}', v)
            else:
                mlflow.log_param(f'{parent_name}.{k}', v)
    elif isinstance(element, ListConfig):
        for i, v in enumerate(element):
            mlflow.log_param(f'{parent_name}.{i}', v)


@hydra.main(config_path='config.yaml')
def main(cfg):
    dataset = MNIST(os.getcwd(), download=True, transform=transforms.ToTensor())
    train, val = random_split(dataset, [55000, 5000])

    trainloader = DataLoader(train, batch_size=cfg.train.batch_size, shuffle=True)
    testloader = DataLoader(val, batch_size=cfg.test.batch_size, shuffle=False)

    model = SAMPLE_DNN(cfg)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=cfg.optimizer.lr,
                          momentum=cfg.optimizer.momentum)

    mlflow.set_tracking_uri('file://' + utils.get_original_cwd() + '/mlruns')
    mlflow.set_experiment(cfg.mlflow.runname)
    with mlflow.start_run():
        for epoch in range(cfg.train.epoch):
            running_loss = 0.0
            log_params_from_omegaconf_dict(cfg)
            for i, (x, y) in enumerate(trainloader):
                optimizer.zero_grad()

                outputs = model(x)
                loss = criterion(outputs, y)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()
        
                mlflow.log_metric("loss", running_loss)

            correct = 0
            total = 0
            with torch.no_grad():
                for (x, y) in testloader:
                    outputs = model(x)
                    _, predicted = torch.max(outputs.data, 1)
                    total += y.size(0)
                    correct += (predicted == y).sum().item()

            accuracy = float(correct / total)
            mlflow.log_metric("acc", accuracy)

if __name__ == '__main__':
    main()