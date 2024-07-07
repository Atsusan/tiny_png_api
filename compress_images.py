import os
import tinify

# TinyPNGのAPIキーを設定
tinify.key = "YOUR_API_KEY ここを変える"

# フォルダのパス
original_folder = 'original'
images_folder = 'images'

# imagesフォルダが存在しない場合は作成
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

# originalフォルダ内の全てのファイルを取得
for filename in os.listdir(original_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        source_path = os.path.join(original_folder, filename)
        target_path = os.path.join(images_folder, filename)
        
        # TinyPNGを使用して画像を圧縮
        source = tinify.from_file(source_path)
        source.to_file(target_path)

print("画像の圧縮と保存が完了しました。")