# -*- coding: utf-8 -*-
import os
from tqdm import tqdm


if __name__ == "__main__":
    """
    python ttf/image_rename_with_dir.py
    """
    default_path = "data_examples/train/TargetImage/"
    x_list = [
        d
        for d in os.listdir(default_path)
        if os.path.isdir(os.path.join(default_path, d))
    ]

    # 遍历每个目录并处理.png文件，添加进度条
    for directory in tqdm(x_list, desc="Processing Directories"):
        dir_path = os.path.join(default_path, directory)
        png_files = [f for f in os.listdir(dir_path) if f.endswith(".png")]

        for png_file in tqdm(png_files, desc=f"Renaming in {directory}", leave=False):
            # 生成新的文件名
            new_name = f"{directory}+{png_file}"
            old_file_path = os.path.join(dir_path, png_file)
            new_file_path = os.path.join(dir_path, new_name)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
