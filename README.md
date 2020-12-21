# 概要
輪講用に作成した hydra, mlflow, optuna 用のチュートリアルコードを載せています．

# 資料
https://speakerdeck.com/supikiti/hydradeshi-meruhaiparaguan-li

# 環境
Python 3.8.0

# 環境設定
git clone https://github.com/supikiti/hydra-mlflow-optuna-sample.git
cd hydra-mlflow-optuna-sample
pip install -r requirement.txt

# 実行
## Hydra チュートリアル
python3 train.py -m model.node1=512,256,128,64 model.node2=32,16

## Optuna チュートリアル
python3 train.py -m 'optimizer.lr=choice(0.1, 0.01, 0.001, 0.0001)' 'model.node1=range(10, 500)'

# 参考にした実装
- https://ymym3412.hatenablog.com/entry/2020/02/09/034644
- https://cyberagent.ai/blog/research/12898/
- https://zerebom.hatenablog.com/#Hydra