import fontforge
import math
import argparse
import os


def adjust_glyph_positions(input_ttf, out_name, version, output_path):
    # 打开字体文件
    font = fontforge.open(input_ttf)

    for glyph in font.glyphs():
        if glyph.isWorthOutputting():
            # 获取字形的边界框
            bbox = glyph.boundingBox()

            # 计算字形的宽度
            glyph_width = bbox[2] - bbox[0]

            # 计算字形在水平方向上的中心点
            center_x = (bbox[0] + bbox[2]) / 2

            # 计算需要移动的距离，使字形水平居中
            shift_x = (glyph.width / 2) - center_x

            # 移动字形
            glyph.transform((1, 0, 0, 1, shift_x, 0))

            # 设置左右侧承，使用 math.floor 向下取整
            left_bearing = math.floor((glyph.width - glyph_width) / 2)
            glyph.left_side_bearing = left_bearing
            glyph.right_side_bearing = left_bearing

    # 设置字体版本
    font.version = version
    # 构建输出文件路径
    output_file = os.path.join(output_path, f"{out_name}.ttf")
    # 保存修改后的字体
    font.generate(output_file)
    font.close()
    print(f"调整后的字体已保存为: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="调整字体文件的字形位置")
    parser.add_argument("input_ttf", help="输入TTF文件的路径")
    parser.add_argument("out_name", help="输出字体文件的名称（不包含扩展名）")
    parser.add_argument("version", help="字体版本")
    parser.add_argument("output_path", help="输出文件夹路径")

    args = parser.parse_args()

    adjust_glyph_positions(args.input_ttf, args.out_name, args.version, args.output_path)


if __name__ == "__main__":
    """
    ffpython C:\\Users\\lawrence\\PycharmProjects\\FontDiffuser\\to_ttf2.py --input_ttf --out_name --version --output_path
    """
    main()
