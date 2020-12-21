# 概要
研究室輪講用に作成した，hydra + mlflow + optuna のサンプルコードです．

## 発表資料
https://speakerdeck.com/supikiti/hydra-mlflow-optuna

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
