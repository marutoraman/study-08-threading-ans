マルチスレッドサンプル
====
マルチスレッド処理を用いて、Chromeを並列で起動するサンプル。  
process関数を実際の処理に置き換えれば、並行で処理を行うことができる。

# 使い方
以下を実行して環境を構築
```
python -m venv venv
. venv/scripts/activate
pip install -r requirements.txt
```

以下のコマンドで実行
```
pyhon main.py
```