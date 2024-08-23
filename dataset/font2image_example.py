# -*- coding: utf-8 -*-
import argparse
from tqdm import tqdm
import sys
import os

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from dataset.ttf_utils import *

char2img_list = '永潮亮酴酿吝怜饶玩捂评晤魉绝抛航当鸟唐弭罚晓示羽差豚牧'
print("char2img_list:", len(char2img_list))


def process_fonts(font_file, image_file, char2img_list=char2img_list):
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


if __name__ == '__main__':
    """
    conda activate fontdiffuser
    python dataset/font2image_example.py --font_in /mnt/data/llch/free-font/xx/FZZCHJW.ttf --image_out data_examples/test_style
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--font_in", default='', help="font path")
    parser.add_argument("--image_out", default='../z_using_files/imgs/val_images/', help="image out path")
    args = parser.parse_args()
    process_fonts(args.font_in, args.image_out, char2img_list)
