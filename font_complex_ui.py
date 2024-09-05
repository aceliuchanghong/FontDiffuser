import random
import time
import os
from datetime import datetime
import gradio as gr
from font_easy_ui import run_fontdiffuer, example_list
from sample import (arg_parse,
                    load_fontdiffuer_pipeline)
import uvicorn
from fastapi import FastAPI
import subprocess
from utils_2 import duplicate_image


def get_latest_png_within_3_hours(directory):
    latest_time = None
    for file in os.listdir(directory):
        if file.endswith('.png') or file.endswith('.jpg'):
            full_path = os.path.join(directory, file)
            modification_time = os.path.getmtime(full_path)
            file_time = datetime.fromtimestamp(modification_time)

            if latest_time is None or file_time > latest_time:
                latest_time = file_time
            # 如果目录下没有png文件
    if latest_time is None:
        return False, None
        # 检查最近的png文件是否在3小时内修改过
    if (datetime.now() - latest_time).total_seconds() <= 3 * 3600:
        return True, "还在生成"
        # 如果没有png文件在3小时内修改过
    return False, None


def generate_font(upload_pic_style, font_name, font_version, test_font):
    if len(font_name) < 1 or font_name == 'try_name_it':
        return gr.update(value="字体名字没有取", visible=True)
    if not upload_pic_style or len(upload_pic_style) < 12:
        return gr.update(value="请上传至少12张相同风格图片", visible=True)
    gen_path = f'data_examples/test_style/{font_name}/'
    if not os.path.exists(gen_path):
        os.makedirs(gen_path)
    print(upload_pic_style)

    result, _ = get_latest_png_within_3_hours(gen_path)
    if result:
        return gr.update(value="字体已经在生成中,大约需要180分钟,请勿重复点击", visible=True)
    duplicate_image(upload_pic_style[0], gen_path, 24)
    free_gpu = str(get_most_idle_gpu())
    print(font_name)
    print(font_version)
    print(free_gpu)

    basic_path = 'data_examples/basic/test/' if test_font else 'data_examples/basic/LXGWWenKaiGB-Light/'
    command = [
        "nohup", "python", "run_all.py",
        "--input", gen_path,
        "--name", font_name,
        "--v", font_version,
        "--cuda", f"cuda:{free_gpu}",
        "--basic_path", basic_path
    ]
    with open(f'output_{font_name}.log', 'w') as outfile:
        subprocess.Popen(command, stdout=outfile, stderr=subprocess.STDOUT)

    time.sleep(10)

    return gr.update(value="开始字体生成！大约需要180分钟,请等待", visible=True)


def get_most_idle_gpu():
    # 运行 nvidia-smi 命令
    result = subprocess.run(
        ['nvidia-smi', '--query-gpu=index,memory.used,utilization.gpu', '--format=csv,noheader,nounits'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 检查是否有错误
    if result.stderr:
        print("Error running nvidia-smi:", result.stderr)
        return None
    # 处理输出
    gpu_data = result.stdout.strip().split('\n')
    min_utilization = 100  # 初始化最大可能的利用率 (100%)
    idle_gpu_index = -1
    for gpu in gpu_data[::-1]:
        index, memory_used, utilization = gpu.split(', ')
        utilization = int(utilization)
        index = int(index)
        # 找到具有最低利用率的GPU
        if utilization < min_utilization:
            min_utilization = utilization
            idle_gpu_index = index
    return idle_gpu_index


def download_font(name):
    # 获取当前工作目录路径
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, 'outputs', name)
    # 获取图片
    files = [f for f in os.listdir(output_dir) if f.endswith('.png')]
    if not files:
        print(f"No image files found in '{output_dir}'.")
        return None, None
    # 随机选择一张图片
    random_pic = random.choice(files)
    random_pic_path = os.path.join(output_dir, random_pic)
    print(f"Random pic file '{random_pic_path}' selected.")
    # 构建字体文件路径
    ttf_file = os.path.join(current_dir, f"{name}.ttf")

    # 检查文件是否存在
    if os.path.isfile(ttf_file):
        print(f"Font file '{ttf_file}' found.")
        return random_pic_path, ttf_file
    else:
        print(f"Font file '{ttf_file}' not found.")
        return random_pic_path, None


if __name__ == '__main__':
    """
    conda activate fontdiffuser
    python font_complex_ui.py
    nohup python font_complex_ui.py > s_words2.log &
    """
    # Initialize FastAPI
    app = FastAPI()
    args = arg_parse()
    args.demo = True
    args.ckpt_dir = 'ckpt'
    args.ttf_path = 'ttf/LXGWWenKaiGB-Light.ttf'
    args.ttf_pic_path = 'ttf_pics/LXGWWenKaiGB-Light/'

    upload_default_path = './upload_pic_default_dir'
    if not os.path.exists(upload_default_path):
        os.makedirs(upload_default_path)

    # load fontdiffuer pipeline
    pipe = load_fontdiffuer_pipeline(args=args)

    with gr.Blocks(title="🎉字体生成🎉") as demo:
        with gr.Row():
            with gr.Column(scale=2):
                gr.HTML("""
                <h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                    输入示例图片
                </h2>
                """)
                gr.Image('figures/input.png')
            with gr.Column(scale=1):
                gr.HTML("""<h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                                    <br><br>示例生成
                                </h2>
                        """)
                gr.Image('data_examples/using_files/arrow2.svg', label='')
            with gr.Column(scale=2):
                gr.HTML("""<h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                                    输出示例字体</h2>
                                """)
                gr.Image('figures/output.png')
        with gr.Row():
            gr.Markdown("---")
            gr.Markdown("---")
        with gr.Row():
            with gr.Column(scale=2):
                with gr.Row():
                    reference_image = gr.Image(width=320, label=' 1️⃣:上传风格文字', image_mode='RGB', type='pil',
                                               height=320)
                    gr.Examples(label=' 1️⃣:点击选择风格字体',
                                examples=example_list,
                                inputs=reference_image,
                                )
                with gr.Row():
                    character = gr.Textbox(value='道', label='2️⃣:输入要生成的文字')
            with gr.Column(scale=1):
                gr.HTML("""<h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                                    <br><br><br><br> 风格图片选择/测试
                                 </h2>
                         """)
                gr.Image('data_examples/using_files/arrow2.svg', label='')
            with gr.Column(scale=2):
                fontdiffuer_output_image = gr.Image(height=200, label="输出字体", image_mode='RGB',
                                                    type='filepath')

                sampling_step = gr.Slider(20, 50, value=20, step=10,
                                          label="推理步数", info="默认20,步数越多时间越久,效果越好")
                guidance_scale = gr.Slider(1, 12, value=7.5, step=0.5,
                                           label="分类器引导指数",
                                           info="默认7.5")

                FontDiffuser = gr.Button('3️⃣:点击生成图片', variant='primary')
        with gr.Row():
            gr.Markdown("---")
            gr.Markdown("---")
        with gr.Row():
            with gr.Column(scale=2):
                upload_pic_style = gr.File(label="🛠️上传字体图片(12-24张)", file_count="multiple",
                                           file_types=['.png', '.jpg'])
                upload_pic_style.GRADIO_CACHE = upload_default_path
                with gr.Row():
                    font_name = gr.Textbox(label='输入字体名称', value='try_name_it',
                                           info='字体取名,必输值',
                                           interactive=True,
                                           )
                    font_version = gr.Textbox(label='输入字体版本号', value='v1.0', placeholder='v1.0',
                                              interactive=True,
                                              info='字体附加版本号,非必选,一般默认v1.0即可')
                    test_font_checkbox = gr.Checkbox(label="是否选择测试字体生成", value=True,
                                                     info="仅测试-速度快")
            with gr.Column(scale=1):
                gr.HTML("""<h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                                                    字体文件生成
                                                 </h2>
                                         """)
                gr.Image('data_examples/using_files/arrow2.svg', label='')
                Generate_Font = gr.Button('点击生成字体', icon='data_examples/using_files/shoot.ico',
                                          variant='primary', size="lg")
                show = gr.Textbox(visible=False)
            with gr.Column(scale=2):
                with gr.Row():
                    preview_image = gr.Image(width=320, label='字体预览', image_mode='RGB', type='pil',
                                             height=320)
                    refreshing = gr.Button('📖刷新图片/字体-注意:\n名字需要填自己命名的字体名称(否则会报错)',
                                           variant='secondary')
                download = gr.File(label='字体下载')


        def dummy_function(image):
            return image


        Generate_Font.click(
            fn=generate_font,  # 当用户点击确认后调用的函数
            inputs=[upload_pic_style, font_name, font_version, test_font_checkbox],
            outputs=show
        )
        refreshing.click(fn=download_font, inputs=[font_name], outputs=[preview_image, download])

        reference_image.upload(dummy_function, inputs=reference_image, outputs=reference_image)
        FontDiffuser.click(
            fn=run_fontdiffuer,
            inputs=[
                character,
                reference_image,
                sampling_step,
                guidance_scale,
            ],
            outputs=fontdiffuer_output_image)

    # Add Gradio app as a FastAPI route
    app = gr.mount_gradio_app(app, demo, path="/")

    # Run the Uvicorn server
    # conda activate fontdiffuser
    # cd /mnt/data/llch/FontDiffuser
    uvicorn.run(app, host="0.0.0.0", port=909, log_level="info")
    # python font_complex_ui.py
    # nohup python font_complex_ui.py > v_complex.log &
