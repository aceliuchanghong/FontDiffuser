# -*- coding: utf-8 -*-
import argparse
from ttf_utils import font2image
import os
from tqdm import tqdm
from pathlib import Path

with open("char7000.txt", "r", encoding="utf-8") as f:
    char2img_list = f.read()
    print(f"{len(char2img_list),char2img_list[:3]}")


def find_fonts(base_path):
    font_files = []
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".ttf") or file.endswith(".otf") or file.endswith(".ttc"):
                # 获取文件的绝对路径
                font_files.append(os.path.abspath(os.path.join(root, file)))
    return font_files


def process_font(font_file_list, image_out_path, char2img_list=char2img_list):
    if not os.path.exists(image_out_path):
        os.makedirs(image_out_path)

    for font in tqdm(font_file_list):
        print("Working on:", font)
        try:
            font2image(font, image_out_path, char2img_list, 96)
            print("Suc ending:", font)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    """
    conda activate fontdiffuser
    python ttf/font2image_new.py --base_path /mnt/data/llch/free-font/test
    python ttf/font2image_new.py --base_path ttf/LXGWWenKaiGB-Light.ttf \
        --out_path ttf_pics/LXGWWenKaiGB-Light/
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_path", required=True, help="font base path")
    parser.add_argument(
        "--out_path",
        default="data_examples/train/TargetImage",
        help="font pic out path",
    )
    opt = parser.parse_args()
    if not Path(opt.base_path).is_file():
        font_files = find_fonts(opt.base_path)  # 目录处理
    else:
        font_files = [opt.base_path]  # 单个文件处理

    font_out_path = opt.out_path

    process_font(font_files, font_out_path, char2img_list)
