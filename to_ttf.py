import fontforge, os, psMat
import argparse


def main():
    # 定义参数
    img_list = list()

    # 获取文件列表
    for file in os.listdir(img_dir):
        if os.path.splitext(file)[1].lower() in '.svg':
            img_list.append(file)
    print('当前总图片数量： %d' % len(img_list))

    # 循环处理图片
    # 创建字体
    font = fontforge.font()
    font.encoding = 'UnicodeFull'
    font.version = opt.version
    font.weight = 'Regular'
    if font_name:
        font.fontname = font_name
    else:
        font.fontname = 'test'
    for img_path in img_list:
        # 获取unicode
        codestr = os.path.splitext(img_path)[0]
        try:
            code = ord(codestr)
        except Exception as e:
            print("err:", codestr)
            print(e)
            continue
        # 创建字符
        glyph = font.createChar(code, "uni" + codestr)
        glyph.importOutlines(os.path.join(img_dir, img_path))

        # 位移调整
        base_matrix = psMat.translate(0, 0)
        glyph.transform(base_matrix)

        # 写入ttf
    font.generate(output)

    print('全部处理结束,svg文件若要删除自行处理')


if __name__ == "__main__":
    """
    cd /mnt/data/llch/FontDiffuser
    /usr/bin/python3 to_ttf.py --name cpp --v v1.0
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='img_dir', default='pico/', help='Please set the input path')
    parser.add_argument('--name', dest='name', default='cpp', help='Please set the output path')
    parser.add_argument('--v', dest='version', default='v1.0', help='Please set the output path')
    opt = parser.parse_args()
    img_dir = opt.img_dir
    output = f'{opt.name}.ttf'
    font_name = f'torch-{opt.name}'
    main()
