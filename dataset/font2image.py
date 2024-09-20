# -*- coding: utf-8 -*-
import argparse
from tqdm import tqdm
import sys
import os

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from dataset.ttf_utils import *

chinese_punctuations = [
    '。',  # 句号
    '，',  # 逗号
    '、',  # 顿号
    '；',  # 分号
    '：',  # 冒号
    '？',  # 问号
    '！',  # 感叹号
    '“',  # 左双引号
    '”',  # 右双引号
    '‘',  # 左单引号
    '’',  # 右单引号
    '（',  # 左括号
    '）',  # 右括号
    '《',  # 左书名号
    '》',  # 右书名号
    '〈',  # 左单书名号
    '〉',  # 右单书名号
    '「',  # 左引号（书名号）
    '」',  # 右引号（书名号）
    '—',  # 破折号
    '……',  # 省略号
    '·',  # 间隔号
    '／',  # 斜线
    '～',  # 波浪线
    '﹏',  # 下划线
    '【',  # 左书名号
    '】',  # 右书名号
    # '=',  # 等号
]  # 27
numbers_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

english_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chinese_punctuations.extend(numbers_str)
chinese_punctuations.extend(english_str)
char2img_list0 = ''.join(chinese_punctuations)

# char2img_list = char2img_list0 + char2img_list1
with open('char.txt', 'r', encoding='utf-8') as f:
    content = f.read()
char2img_list = content
print("char2img_list:", len(char2img_list))


def process_fonts(font_file_path, image_file_path, char2img_list=char2img_list):
    """
    Processes fonts by generating images for each font.

    :param font_file_path: Path to the directory containing font files
    :param image_file_path: Path to the directory where images will be saved
    :param char2img_list: List of characters to generate images for
    """
    if not os.path.exists(image_file_path):
        os.makedirs(image_file_path)
    fonts = os.listdir(font_file_path)

    for font in tqdm(fonts):
        font_path = os.path.join(font_file_path, font)
        try:
            font2image(font_path, image_file_path, char2img_list, 128)
            # 处理不知道为什么没在的字符
            input_file_name = font_path.split('/')[-1].split('.')[0]
            output_path = os.path.join(image_file_path, input_file_name)
            if os.path.exists(output_path):
                generated_images = os.listdir(output_path)
                print("outPath:", output_path)
                # print(generated_images[6695], len(generated_images), len(char2img_list))
                # 汇总 char2img_list 未出现在 generated_images 中的文件
                missing_chars = [char for char in char2img_list if
                                 char not in [img_name.split('.')[0] for img_name in generated_images]]
                print("missing_chars:", missing_chars)
                # 重新生成缺失字符的图像
                if missing_chars:
                    missing_chars_string = ''.join(missing_chars)
                    font2image(font_path, image_file_path, missing_chars_string, 128)
                    # for missing_char in missing_chars:
                    #     print(f"Regenerating image for missing character: {missing_char}")
                    #     font2image(font_path, image_file_path, missing_char, 128)

        except Exception as e:
            print(e)
    # remove_empty_floder(image_file_path)


if __name__ == '__main__':
    """
    conda activate fontdiffuser
    python dataset/font2image.py --font_in /mnt/data/llch/VQ-Font/z_using_files/content_font --image_out data_examples/basic
    python dataset/font2image.py --font_in ./ttf --image_out ./ttf_pics
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--font_in", default='../z_using_files/val_font/', help="font path")
    parser.add_argument("--image_out", default='../z_using_files/imgs/val_images/', help="image out path")
    args = parser.parse_args()
    process_fonts(args.font_in, args.image_out, char2img_list)
