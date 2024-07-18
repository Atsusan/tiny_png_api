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

3. pipファイルを実行、pipファイルのpathを通す作業

    追記（get-pip.pyを予め用意したので下記コマンドの実行から続けて大丈夫です。）

    1) 下記のコマンドを入力
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


↑↑ 上記、わかりにくいところもあると思うので、下記ChatGPTに聞いてみた回答です。

Pythonのインストール:
まず、Pythonがインストールされていることを確認してください。インストールされていない場合は、Python公式サイトからダウンロードしてインストールしてください。
pipのインストール:
get-pip.pyファイルを使ってpipをインストールします。コマンドプロンプトやターミナルで以下のコマンドを実行してください：
Copypython get-pip.py

tinifyライブラリのインストール:
pipを使って、tinifyライブラリをインストールします：
Copypip install tinify

TinyPNG APIキーの設定:
compress_images.pyファイル内の以下の行を編集し、あなたのTinyPNG APIキーを設定してください：
pythonCopytinify.key = "YOUR_API_KEY ここを変える"
TinyPNGのウェブサイトでアカウントを作成し、APIキーを取得する必要があります。
フォルダ構造の準備:
スクリプトと同じディレクトリにoriginalフォルダを作成し、圧縮したい画像ファイルを配置してください。
スクリプトの実行:
準備が整ったら、以下のコマンドでスクリプトを実行します：
Copypython compress_images.py


スクリプトが正常に実行されると、originalフォルダ内の画像が圧縮され、imagesフォルダに保存されます。
