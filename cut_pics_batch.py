import argparse
import os
import cv2
import shutil
import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def process_image(img, rect_size, ignore_min_size, ignore_max_size, offset_param, output_path, file_name):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (rect_size, rect_size))
    eroded = cv2.erode(thresh, kernel)
    contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    spacing = rect_size // 2 - 1

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w < ignore_min_size or h < ignore_min_size or w > ignore_max_size or h > ignore_max_size:
            continue

        font_w = w - spacing - spacing
        font_h = h - spacing - spacing
        frame_size = max(font_w, font_h)
        x_offset = int((frame_size - font_w) / 2)

        start_x = x + spacing - x_offset - offset_param
        # start_y = y + spacing - y_offset - offset_param
        start_y = 0
        end_x = x + w - spacing + x_offset + offset_param
        # end_y = y + h - spacing + y_offset + offset_param
        end_y = h

        temp = img[start_y:end_y, start_x:end_x]
        path = os.path.join(output_path, "result")
        if not os.path.exists(path):
            os.makedirs(path)
        random_integer1 = random.randint(10000, 200000)
        random_integer2 = random.randint(10, 2000)
        temp_file = os.path.join(path, f"{random_integer1}_{random_integer2}.png")
        cv2.imwrite(temp_file, temp)
        os.rename(temp_file, os.path.join(path, f"{file_name}.png"))
        # print(file_name, f"{file_name}.png")
        break


def process_image_wrapper(args):
    img, rect_size, ignore_min_size, ignore_max_size, offset_param, output_path, base_name = args
    process_image(img, rect_size, ignore_min_size, ignore_max_size, offset_param, output_path, base_name)


def main(opt):
    rect_size = opt.rect_size
    ignore_min_size = opt.ignore_min_size
    ignore_max_size = opt.ignore_max_size
    offset_param = opt.offset_param

    input_path = opt.input_path
    output_path = opt.output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    else:
        shutil.rmtree(output_path)
        os.makedirs(output_path)

    tasks = []
    file_list = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]

    with ThreadPoolExecutor() as executor:
        for file_name in file_list:
            file_path = os.path.join(input_path, file_name)
            # print("dealing:", file_path)
            img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
            base_name = file_name.split(".")[0]
            tasks.append(
                executor.submit(process_image_wrapper, (
                    img, rect_size, ignore_min_size, ignore_max_size, offset_param, output_path, base_name))
            )

        for _ in tqdm(as_completed(tasks), total=len(tasks), desc="Processing Images"):
            pass  # 只是等待任务完成，tqdm会自动更新进度条

    print("moving files")
    # 定义 ans 路径
    ans_path = os.path.join(output_path, "ans")
    # 创建或清空 ans 路径
    if not os.path.exists(ans_path):
        os.makedirs(ans_path)
    else:
        shutil.rmtree(ans_path)
        os.makedirs(ans_path)
    # 将input_path中的文件复制到 ans 路径
    for file_name in os.listdir(input_path):
        file_path = os.path.join(input_path, file_name)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, ans_path)
    # 再次将 result 路径中的文件复制到 ans_path，覆盖已有文件
    if not os.path.exists(os.path.join(output_path, "result")):
        os.makedirs(os.path.join(output_path, "result"))
    print("图片切割数量:", str(len(os.listdir(os.path.join(output_path, "result")))))
    for file_name in os.listdir(os.path.join(output_path, "result")):
        file_path = os.path.join(os.path.join(output_path, "result"), file_name)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, ans_path)
    print("Files moved successfully")


if __name__ == '__main__':
    """
    python cut_pics_batch.py --input 'input/test'
    python cut_pics_batch.py --input 'outputs/cpp2/' --output './pic/cpp'
    python cut_pics_batch.py --input 'outputs/crh2/' --output './pic/crh'
    python cut_pics_batch.py --input 'outputs/fzfs2/' --output './pic/fzfs'
    python cut_pics_batch.py --input 'outputs/FZZCHJW2/' --output './pic/FZZCHJW'
    python cut_pics_batch.py --input C:\\Users\\lawrence\\Pictures\\111\\cpp6838 --output ./pic/cpp --rect_size 85 --ignore_min_size 240 --ignore_max_size 280
    python cut_pics_batch.py --input C:\\Users\\lawrence\\Pictures\\111\\crh6838 --output ./pic/crh --rect_size 85 --ignore_min_size 240 --ignore_max_size 280
    python cut_pics_batch.py --input 'input/test' --rect_size 85 --ignore_min_size 240 --ignore_max_size 280
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_path', default='input/', help='Please set the input path')
    parser.add_argument('--output', dest='output_path', default='./pic', help='Please set the output path')
    parser.add_argument('--rect_size', dest='rect_size', default=20, type=int, help='膨胀腐蚀大小')
    parser.add_argument('--ignore_min_size', dest='ignore_min_size', default=85, type=int, help='字体小于该值忽略')
    parser.add_argument('--ignore_max_size', dest='ignore_max_size', default=100, type=int, help='字体大于该值忽略')
    parser.add_argument('--offset_param', dest='offset_param', default=0, type=int,
                        help='图片选取偏移,选取图片扩大范围')
    opt = parser.parse_args()
    main(opt)
