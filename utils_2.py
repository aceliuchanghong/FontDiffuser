import shutil
import os
import pygame


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


def fix_one_pic(font_name, chars='一'):
    pygame.init()
    pic_path = os.path.join('outputs', font_name)

    for char in chars:
        image_path = os.path.join(pic_path, char + '.png')

        if os.path.exists(image_path):
            # 加载图片
            image = pygame.image.load(image_path)
            image_rect = image.get_rect()
            width, height = image_rect.size
            print(f"Original image size: {width}x{height}")

            # 使用mask来获取非透明部分的边界
            mask = pygame.mask.from_surface(image)
            mask_outline = mask.outline()

            if mask_outline:
                min_x = 1
                max_x = 95
                min_y = 1
                max_y = 80

                # 计算文字的中心点
                text_center_x = (min_x + max_x) // 2
                text_center_y = (min_y + max_y) // 2
                print(f"Text bounding box: left={min_x}, right={max_x}, top={min_y}, bottom={max_y}")
                print(f"Text center: ({text_center_x}, {text_center_y})")

                # 创建一个新的白色背景的Surface，并将文字居中
                centered_surface = pygame.Surface((width, height))
                centered_surface.fill((255, 255, 255))  # 背景填充为白色

                # 计算新的位置，使文字居中
                center_pos = centered_surface.get_rect().center
                offset_x = center_pos[0] - text_center_x
                offset_y = center_pos[1] - text_center_y
                image_rect.topleft = (offset_x, offset_y)

                # 将图片绘制到新surface上
                centered_surface.blit(image, image_rect)
                pygame.image.save(centered_surface, image_path)

                print(f"fix {char}.png success")

    pygame.quit()


if __name__ == '__main__':
    """
    python utils_2.py
    """
    fix_one_pic('test')
