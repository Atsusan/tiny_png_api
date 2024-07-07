Tiny PngのAPIキーと紐付けして、Pythonで画像を圧縮するプログラムです。


[Tiny Png](https://tinypng.com/)


画像圧縮スクリプトの使用手順

前提条件
・Python 3.x がインストールされていること
・TinyPNGのAPIキーを取得していること

手順
1. TinyPNGのAPIキーを取得
    1) TinyPNGの公式サイトにアクセスし、アカウントを作成します。
    2) APIキーを取得します。

2. 必要なファイルの準備

    1) 以下のスクリプトを compress_images.py という名前で保存します。
        compress_images.py

    2) YOUR_API_KEY を取得したAPIキーに置き換えます。

3. 必要なライブラリのインストール
    1) ターミナルを開き、以下のコマンドを実行して pip をインストールします。
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py

    2) pip がインストールされたディレクトリをパスに追加します。
     export PATH=$PATH:/Users/your_username/Library/Python/3.9/bin

    3) tinify ライブラリをインストールします。
    pip install tinify

4 スクリプトの実行

    1) ターミナルでスクリプトが保存されているディレクトリに移動します。
    cd /path/to/your/script
    2) スクリプトを実行します。

    python3 compress_images.py
これで、original フォルダ内の画像が圧縮され、images フォルダに保存されます。
