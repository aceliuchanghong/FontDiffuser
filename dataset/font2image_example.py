# -*- coding: utf-8 -*-
import argparse
from tqdm import tqdm
import sys
import os

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from dataset.ttf_utils import *


def process_fonts(font_file, image_file, char2img_list):
    """
    Processes fonts by generating images for each font.

    :param font_file: Path to the directory containing font files
    :param image_file: Path to the directory where images will be saved
    :param char2img_list: List of characters to generate images for
    """
    if not os.path.exists(image_file):
        os.makedirs(image_file)
    fonts = [font_file]

    for font in tqdm(fonts):
        try:
            font2image(font, image_file, char2img_list, 128)
            print(font)
        except Exception as e:
            print(e)
    remove_empty_floder(image_file)


if __name__ == "__main__":
    """
    conda activate fontdiffuser
    python dataset/font2image_example.py --font_in /mnt/data/llch/free-font/xx/FZZCHJW.ttf --image_out data_examples/test_style
    python dataset/font2image_example.py --font_in ttf/LXGWWenKaiGB-Light.ttf \
        --image_out data_examples/basic/test/
    python dataset/font2image_example.py --font_in ttf/LXGWWenKaiGB-Light.ttf \
        --image_out data_examples/basic/ \
        --char_file char.txt
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--font_in", default="", help="font path")
    parser.add_argument(
        "--image_out",
        default="../z_using_files/imgs/val_images/",
        help="image out path",
    )
    parser.add_argument("--char_file", default="char2000.txt")
    args = parser.parse_args()
    with open(args.char_file, "r", encoding="utf-8") as f:
        char2img_list = f.read()
        print(f"{len(char2img_list),char2img_list[:3]}")
    process_fonts(args.font_in, args.image_out, char2img_list)
