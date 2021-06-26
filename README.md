# 概要
hydra + mlflow + optuna のサンプルコードです．

## 発表資料
[研究室輪講時資料](https://speakerdeck.com/supikiti/hydra-mlflow-optuna)
[Optuna Meetup #1 登壇時資料](https://speakerdeck.com/supikiti/hydra-mlflow-optunafalsezu-mihe-wasedeshou-qing-nishi-meruhaipaparametaguan-li-210b3f53-5c57-4468-b7c8-07ba5f1f05a4)

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
