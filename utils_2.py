import shutil
import os
import cv2 
import numpy as np


def duplicate_image(image_path, output_path, nums):
    """
    复制指定数量的图片，并为每个副本添加编号。

    :param image_path: 原始图片的路径
    :param output_path: 输出目录
    :param nums: 复制的数量
    duplicate_image('/mnt/data/llch/FontDiffuser/data_examples/test_style/依.png', '/mnt/data/llch/FontDiffuser/data_examples/test_style/cpp_ai', 24)
    """
    # 检查输出路径是否存在，存在就删除原来文件,如果不存在则创建
    if os.path.exists(output_path):
        # 删除当前目录下的所有文件
        for file in os.listdir(output_path):
            file_path = os.path.join(output_path, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或符号链接
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # 删除空文件夹
    else:
        os.makedirs(output_path)

    # 获取原始图片的文件名和扩展名
    filename, ext = os.path.splitext(os.path.basename(image_path))

    # 复制图片并添加编号
    for i in range(1, nums + 1):
        new_filename = f"{filename}_{i}{ext}"
        new_file_path = os.path.join(output_path, new_filename)
        shutil.copy(image_path, new_file_path)
        print(f"已创建: {new_file_path}")


import os
import pygame


def fix_one_pic(font_name, chars='一'):
    pygame.init()
    pic_path = os.path.join('outputs', font_name)

    for char in chars:
        image_path = os.path.join(pic_path, char + '.png')
        if os.path.exists(image_path):
            print(image_path)
            # 使图像居中, 覆盖原始文件
            image = pygame.image.load(image_path)
            image_rect = image.get_rect()
            width, height = image_rect.size
            centered_surface = pygame.Surface((width, height))
            centered_surface.fill((255, 255, 255))  # 背景填充为白色
            center_pos = centered_surface.get_rect().center
            image_rect.center = center_pos  # 设置原图的rect居中
            centered_surface.blit(image, image.get_rect(center=center_pos))
            pygame.image.save(centered_surface, image_path)

            print(f"fix {char}.png suc")
    pygame.quit()


if __name__ == '__main__':
    """
    python utils_2.py
    """
    fix_one_pic('test')
