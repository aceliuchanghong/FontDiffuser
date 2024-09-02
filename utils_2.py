import shutil
import os


def duplicate_image(image_path, output_path, nums):
    """
    复制指定数量的图片，并为每个副本添加编号。

    :param image_path: 原始图片的路径
    :param output_path: 输出目录
    :param nums: 复制的数量
    duplicate_image('/mnt/data/llch/FontDiffuser/data_examples/test_style/依.png', '/mnt/data/llch/FontDiffuser/data_examples/test_style/cpp_ai', 24)
    """
    # 检查输出路径是否存在，如果不存在则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 获取原始图片的文件名和扩展名
    filename, ext = os.path.splitext(os.path.basename(image_path))

    # 复制图片并添加编号
    for i in range(1, nums + 1):
        new_filename = f"{filename}_{i}{ext}"
        new_file_path = os.path.join(output_path, new_filename)
        shutil.copy(image_path, new_file_path)
        print(f"已创建: {new_file_path}")


if __name__ == '__main__':
    """
    python utils_2.py
    """
    # 示例用法
    print("00")
