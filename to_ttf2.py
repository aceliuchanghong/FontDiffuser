import fontforge
import math


def adjust_glyph_positions(font_path):
    # 打开字体文件
    font = fontforge.open(font_path)

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

    # 保存修改后的字体
    output_path = font_path.replace('.ttf', '_adjusted.ttf')
    font.generate(output_path)
    font.close()

    print(f"调整后的字体已保存为: {output_path}")


# 使用示例
font_path = r"C:\Users\lawrence\Documents\WeChat Files\wxid_yamvaf39vkqm22\FileStorage\File\2024-09\crh.ttf"
adjust_glyph_positions(font_path)