# 概要
hydra + mlflow + optuna のサンプルコードです．

## 参考資料
[研究室輪講時資料 (2.6k view)](https://speakerdeck.com/supikiti/hydra-mlflow-optuna)

[Optuna Meetup #1 登壇時資料](https://speakerdeck.com/supikiti/hydra-mlflow-optunafalsezu-mihe-wasedeshou-qing-nishi-meruhaipaparametaguan-li-210b3f53-5c57-4468-b7c8-07ba5f1f05a4)

[medium/optuna への投稿資料 (1.8k view)](https://medium.com/optuna/easy-hyperparameter-management-with-hydra-mlflow-and-optuna-783730700e7d)

[上記の日本語版 (1.1k view)](https://supikiti22.medium.com/hydra-mlflow-optuna%E3%81%AE%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%81%A7%E6%89%8B%E8%BB%BD%E3%81%AB%E5%A7%8B%E3%82%81%E3%82%8B%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BC%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E7%AE%A1%E7%90%86-6b8e6d41b3da)

## 実行環境
Python 3.8.0

## 環境設定
```bash
git clone https://github.com/supikiti/hydra-mlflow-optuna-sample.git
cd hydra-mlflow-optuna-sample
pip install -r requirements.txt
```

## 実行例
### hydra + mlflow
```bash
python train.py -m model.node1=128,256 model.node2=256,512
```

### hydra + mlflow + optuna
```bash
python3 train.py -m 'optimizer.lr=choice(0.1, 0.01, 0.001, 0.0001)' 'model.node1=range(10, 500)'
```

## 参考にした実装
- https://ymym3412.hatenablog.com/entry/2020/02/09/034644
- https://cyberagent.ai/blog/research/12898/
