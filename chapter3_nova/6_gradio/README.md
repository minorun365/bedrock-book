# 3.7.2 Gradio (p.180)

> [!NOTE]
> 💡 本ディレクトリーはAmazon Novaへ対応したソースを配置しています。

Cloud9のPython3.9の環境ではライブラリーの依存関係の解決ができないため、Python3.11をインストールします。

### Cloud9環境の場合

以下のコマンドを実行して、Python3.11をインストールします。

```shell
sudo dnf install -y python3.11 python3.11-pip
```

以下のコマンドを実行して、必要なライブラリをインストールします。

```shell
pip3.11 install -r requirements.txt
```

### SageMaker Studio環境の場合

[こちら](https://qiita.com/minorun365/items/f5289163795d5d7b21e2)に記載の方法でSageMaker Studio環境を構築している場合は、以下のコマンドを実行して、Python3.11をインストールします。

```shell
conda create -n handson311 python=3.11 --yes
conda activate handson311
```

以下のコマンドを実行して、必要なライブラリをインストールします。

```shell
pip install -r requirements.txt
```

もとのPython環境に戻す際は、ターミナルを`exit`で抜け、再度新しいターミナルを起動してください。


## 2_multi-modal.py

以下のコマンドを実行してPythonファイルを実行します。

```shell
python3.11 2_multi-modal.py
```
