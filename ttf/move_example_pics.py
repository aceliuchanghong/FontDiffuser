import os
import random
import shutil

# 设置目录路径
# python ttf/move_example_pics.py
source_dir = "data_examples/train/TargetImage"
target_dir = "ckpt"

# 获取所有的子目录（pic_dirs）
pic_dirs = [
    d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))
]

# 遍历每一个目录，复制一个随机的图片
for pic_dir in pic_dirs:
    pic_dir_path = os.path.join(source_dir, pic_dir)

    # 获取当前目录下所有图片文件
    all_files = [f for f in os.listdir(pic_dir_path) if f.endswith(("png"))]

    if all_files:
        # 随机选择一个图片
        random_pic = random.choice(all_files)

        # 构建源文件和目标文件路径
        source_pic_path = os.path.join(pic_dir_path, random_pic)
        target_pic_dir = os.path.join(target_dir, pic_dir)

        # 如果目标目录不存在，则创建
        if not os.path.exists(target_pic_dir):
            os.makedirs(target_pic_dir)

        # 复制图片到目标目录，保持原文件名
        target_pic_path = os.path.join(target_pic_dir, random_pic)
        shutil.copy(source_pic_path, target_pic_path)
        print(f"复制 {source_pic_path} 到 {target_pic_path}")
