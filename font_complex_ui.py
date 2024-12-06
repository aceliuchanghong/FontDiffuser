import random
import shutil
import time
import os
import re
from datetime import datetime
import gradio as gr
from font_easy_ui import run_fontdiffuer, example_list
import uvicorn
from fastapi import FastAPI
import subprocess
from utils_2 import duplicate_image, fix_one_pic
from dataset.font2image import process_fonts
from PIL import Image
from sample import arg_parse, sampling, load_fontdiffuer_pipeline


def get_latest_png_within_3_hours(directory):
    latest_time = None
    for file in os.listdir(directory):
        if file.endswith(".png") or file.endswith(".jpg"):
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
    if len(font_name) < 1 or font_name == "try_name_it":
        return gr.update(value="字体名字没有取", visible=True)
    if not upload_pic_style or len(upload_pic_style) < 12:
        return gr.update(value="请上传至少12张相同风格图片", visible=True)
    gen_path = f"data_examples/test_style/{font_name}/"
    if not os.path.exists(gen_path):
        os.makedirs(gen_path)
    print(upload_pic_style)

    result, _ = get_latest_png_within_3_hours(gen_path)
    if result:
        return gr.update(
            value="字体已经在生成中,大约需要180分钟,请勿重复点击", visible=True
        )
    duplicate_image(upload_pic_style[0], gen_path, 24)
    free_gpu = str(get_most_idle_gpu())
    print(font_name)
    print(font_version)
    print(free_gpu)

    basic_path = (
        "data_examples/basic/test/"
        if test_font
        else "data_examples/basic/LXGWWenKaiGB-Light/"
    )
    command = [
        "nohup",
        "python",
        "run_all.py",
        "--input",
        gen_path,
        "--name",
        font_name,
        "--v",
        font_version,
        "--cuda",
        f"cuda:{free_gpu}",
        "--basic_path",
        basic_path,
    ]
    with open(f"output_{font_name}.log", "w") as outfile:
        subprocess.Popen(command, stdout=outfile, stderr=subprocess.STDOUT)

    time.sleep(10)

    return gr.update(value="开始字体生成！大约需要180分钟,请等待", visible=True)


def generate_font_pics(
    font_name_input,
    font_not_exists,
    wrong_character_input,
    sampling_step2,
    guidance_scale2,
):
    if font_not_exists == "该名称字体不存在":
        return [], gr.update(value="请先确认字体名称")
    style_pic_path_list = os.path.join("data_examples/test_style", font_name_input)
    style_pic = os.path.join(style_pic_path_list, os.listdir(style_pic_path_list)[0])
    style_pic = Image.open(style_pic).convert("RGB")
    generated_images = []
    result = re.sub(r"[^\u4e00-\u9fff]", "", wrong_character_input)
    result = "".join(sorted(set(result), key=result.index))
    print(result, sampling_step2, guidance_scale2)
    for char in result.strip():
        temp = {}
        source_image = args.ttf_pic_path + "/" + char + ".png"
        if not os.path.exists(source_image):
            try:
                process_fonts("ttf", "ttf_pics", char)
            except Exception as e:
                print(e)
        source_image = Image.open(source_image).convert("RGB")
        args.character_input = False if source_image is not None else True
        args.content_character = char
        args.sampling_step = sampling_step2
        args.guidance_scale = guidance_scale2
        args.seed = random.randint(0, 10000)
        out_image = sampling(
            args=args, pipe=pipe, content_image=source_image, style_image=style_pic
        )

        output_dir = "data_examples/test/lch"
        os.makedirs(output_dir, exist_ok=True)
        new_filename = f"{char}.png"
        new_file_path = os.path.join(output_dir, new_filename)
        if char == "一":
            fix_one_pic("QAQ", "一", output_dir)
        out_image.save(new_file_path)
        temp["render"] = False
        temp["path_pic"] = new_file_path
        random_number = datetime.now().strftime("%H%M%S")
        temp["current_time"] = random_number
        generated_images.append(temp)

    return generated_images, gr.update(value="字体图片如下,请逐一确认")


def get_most_idle_gpu():
    # 运行 nvidia-smi 命令
    result = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=index,memory.used,utilization.gpu",
            "--format=csv,noheader,nounits",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # 检查是否有错误
    if result.stderr:
        print("Error running nvidia-smi:", result.stderr)
        return None
    # 处理输出
    gpu_data = result.stdout.strip().split("\n")
    min_utilization = 100  # 初始化最大可能的利用率 (100%)
    idle_gpu_index = -1
    for gpu in gpu_data[::-1]:
        index, memory_used, utilization = gpu.split(", ")
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
    output_dir = os.path.join(current_dir, "outputs", name)
    # 构建字体文件路径
    ttf_file = os.path.join(current_dir, f"{name}.ttf")
    os.makedirs(output_dir, exist_ok=True)
    # 获取图片
    files = [f for f in os.listdir(output_dir) if f.endswith(".png")]
    if not files:
        print(f"No image files found in '{output_dir}'.")
        if os.path.isfile(ttf_file):
            return None, ttf_file
        return None, None
    # 随机选择一张图片
    random_pic = random.choice(files)
    random_pic_path = os.path.join(output_dir, random_pic)
    print(f"Random pic file '{random_pic_path}' selected.")

    # 检查文件是否存在
    if os.path.isfile(ttf_file):
        print(f"Font file '{ttf_file}' found.")
        return random_pic_path, ttf_file
    else:
        print(f"Font file '{ttf_file}' not found.")
        return random_pic_path, None


def re_gen_font(old_name, new_name):
    # 如果没有输入old_name，则不会报错，直接返回初始值
    if len(old_name) < 1:
        return gr.update(value="请输入字体名称"), gr.update(visible=True), "no_file.txt"

    # 如果new_name为空，则使用old_name作为new_name
    if len(new_name) < 1:
        new_name = old_name

    new_font_path = new_name + ".ttf"
    old_font_pic_dir = os.path.join("outputs", old_name)

    # 检查路径是否存在
    if not os.path.isdir(old_font_pic_dir):
        return (
            gr.update(value="旧字体目录不存在"),
            gr.update(visible=True),
            new_font_path,
        )

    subprocess.run(
        [
            "python",
            "run_gen.py",
            "--input",
            f"{old_font_pic_dir}",
            "--name",
            f"{new_name}",
            "--v",
            f"v1.1",
        ]
    )

    print(f"生成字体路径: {old_font_pic_dir}, 新字体名称: {new_name}")
    return (
        gr.update(value="已生成,点击下载"),
        gr.update(value="已生成,点击下载", visible=False),
        new_font_path,
    )


if __name__ == "__main__":
    """
    conda activate fontdiffuser
    python font_complex_ui.py
    nohup python font_complex_ui.py > s_words2.log &
    """
    # Initialize FastAPI
    app = FastAPI()
    args = arg_parse()
    args.demo = True
    args.ckpt_dir = "ckpt"
    args.ttf_path = "ttf/LXGWWenKaiGB-Light.ttf"
    args.ttf_pic_path = "ttf_pics/LXGWWenKaiGB-Light/"

    upload_default_path = "./upload_pic_default_dir"
    if not os.path.exists(upload_default_path):
        os.makedirs(upload_default_path)

    # load fontdiffuer pipeline
    pipe = load_fontdiffuer_pipeline(args=args)

    with gr.Blocks(title="🎉字体生成🎉") as demo:
        with gr.Tab(label="📙风格测试选择"):
            gr.Markdown("---")
            with gr.Row():
                with gr.Column(scale=2):
                    with gr.Row():
                        reference_image = gr.Image(
                            width=320,
                            label=" 1️⃣:上传风格文字",
                            image_mode="RGB",
                            type="pil",
                            height=320,
                        )
                        gr.Examples(
                            label=" 1️⃣:点击选择风格字体",
                            examples=example_list,
                            inputs=reference_image,
                        )
                    with gr.Row():
                        character = gr.Textbox(value="道", label="2️⃣:输入要生成的文字")
                with gr.Column(scale=2):
                    fontdiffuer_output_image = gr.Image(
                        height=200, label="输出字体", image_mode="RGB", type="filepath"
                    )
                    sampling_step = gr.Slider(
                        20, 50, value=20, step=10, label="推理步数", info="默认20"
                    )
                    guidance_scale = gr.Slider(
                        1,
                        12,
                        value=7.5,
                        step=0.5,
                        label="分类器引导指数",
                        info="默认7.5",
                    )

                    FontDiffuser = gr.Button("3️⃣:点击生成图片", variant="primary")
        with gr.Tab(label="👉字体生成"):
            with gr.Row():
                with gr.Column(scale=2):
                    upload_pic_style = gr.File(
                        label="🛠️上传字体图片(12-24张)",
                        file_count="multiple",
                        file_types=[".png", ".jpg"],
                    )
                    upload_pic_style.GRADIO_CACHE = upload_default_path
                    with gr.Row():
                        font_name = gr.Textbox(
                            label="输入字体名称",
                            value="try_name_it",
                            info="字体取名,必输值",
                            interactive=True,
                        )
                        font_version = gr.Textbox(
                            label="输入字体版本号",
                            value="v1.0",
                            placeholder="v1.0",
                            interactive=True,
                            info="字体附加版本号,非必选,一般默认v1.0即可",
                        )
                        test_font_checkbox = gr.Checkbox(
                            label="仅选择测试字体生成-五于天末开下理事画现玫珠表...",
                            value=True,
                            info="仅测试-约20分钟",
                        )
                    with gr.Row():
                        Generate_Font = gr.Button(
                            "点击生成字体",
                            icon="data_examples/using_files/shoot.ico",
                            variant="primary",
                            size="lg",
                        )
                        show = gr.Textbox(visible=False)
                with gr.Column(scale=2):
                    with gr.Row():
                        preview_image = gr.Image(
                            width=200,
                            label="字体预览",
                            image_mode="RGB",
                            type="pil",
                            height=200,
                        )
                        refreshing = gr.Button(
                            "📖刷新图片/字体-注意:\n名字需要填自己命名的字体名称(否则会报错)",
                            variant="secondary",
                        )
                    download = gr.File(label="字体下载")
        with gr.Tab(label="🔧字体样式修改"):
            tasks = gr.State([])
            with gr.Row():
                with gr.Column() as column1:
                    with gr.Row():
                        font_name_input = gr.Textbox(
                            label="字体修改",
                            placeholder="输入字体名称",
                            interactive=True,
                        )
                        make_sure_font_name = gr.Button("确认字体名称", variant="stop")
                        font_not_exists = gr.Textbox(
                            value="该名称字体不存在", visible=False, interactive=False
                        )
                    wrong_character_input = gr.Textbox(
                        label="不满意文字", placeholder="输入需要修改的文字"
                    )
                    with gr.Row():
                        upload_wrong_char_img = gr.File(
                            label='手动修改文字上传(尺寸严格96*96,仅上传"道.png"格式文字图片,可多图)',
                            file_count="multiple",
                            file_types=[".png"],
                        )
                        upload_button = gr.Button("点击确认上传")
                    upload_wrong_char = gr.Textbox(
                        value="上传完成", visible=False, interactive=False
                    )

                    def sure_name(font_name):
                        if len(font_name.strip()) < 1:
                            return gr.update(value="再次确认字体名称"), gr.update(
                                visible=True
                            )
                        if not os.path.exists(
                            os.path.join("data_examples/test_style", font_name)
                        ):
                            return gr.update(value="再次确认字体名称"), gr.update(
                                visible=True
                            )
                        else:
                            return gr.update(visible=False), gr.update(
                                value="字体存在", visible=True
                            )

                    def upload_wrong_func(image_list, font_name, font_exists):
                        if font_exists != "字体存在":
                            return gr.update(
                                value="该名称字体不存在,再次确认字体名称", visible=True
                            )

                        destination_path = os.path.join("outputs", font_name)
                        if not os.path.exists(destination_path):
                            return gr.update(
                                value="该名称字体不存在,再次确认字体名称", visible=True
                            )
                        # print(image_list)
                        for image in image_list:
                            # print(os.path.basename(image))
                            if not re.match(
                                r"^[\u4e00-\u9fff]\.png$", os.path.basename(image)
                            ):
                                return gr.update(
                                    value="图片格式有问题，文件名应为单个中文字符且以.png结尾",
                                    visible=True,
                                )
                            img = Image.open(image)
                            if img.size != (96, 96):
                                return gr.update(
                                    value="图片尺寸不为96x96", visible=True
                                )
                            shutil.copy2(
                                image,
                                os.path.join(destination_path, os.path.basename(image)),
                            )

                        return gr.update(visible=True)

                    upload_button.click(
                        upload_wrong_func,
                        inputs=[
                            upload_wrong_char_img,
                            font_name_input,
                            font_not_exists,
                        ],
                        outputs=[upload_wrong_char],
                    )
                    make_sure_font_name.click(
                        sure_name,
                        inputs=[font_name_input],
                        outputs=[make_sure_font_name, font_not_exists],
                    )
                with gr.Column() as column2:
                    sampling_step2 = gr.Slider(
                        20, 60, value=40, step=5, label="推理步数"
                    )
                    guidance_scale2 = gr.Slider(
                        1,
                        12,
                        value=7.5,
                        step=0.5,
                        label="分类器引导指数",
                        info="默认7.5",
                    )
                    re_gen = gr.Button("点击生成图片", variant="stop")
                    re_gen_before_name_sure = gr.Textbox(value="", interactive=False)
                    # 需要有一个一键复制的剩余的有问题的字的框
                    # show_left_character_input = gr.Textbox(label='不满意文字剩余', interactive=False, value='', visible=False)

            @gr.render(inputs=tasks)
            def render_add_rules(task_list):
                incomplete = [
                    task for task in task_list if not task["render"]
                ]  # 过滤出渲染未完成的任务
                if len(incomplete) < 1:
                    return
                for task in incomplete:
                    with gr.Row():
                        sure_images = gr.Image(task["path_pic"])
                        sure_button = gr.Button("确认", variant="secondary")

                        def sure_ok_image(sure_images_path, font_name_input, task=task):
                            task["render"] = True
                            shutil.copy2(
                                task["path_pic"],
                                os.path.join("outputs", font_name_input),
                            )
                            return task_list

                        sure_button.click(
                            sure_ok_image,
                            inputs=[sure_images, font_name_input],
                            outputs=tasks,
                        )

            re_gen.click(
                generate_font_pics,
                inputs=[
                    font_name_input,
                    font_not_exists,
                    wrong_character_input,
                    sampling_step2,
                    guidance_scale2,
                ],
                outputs=[tasks, re_gen_before_name_sure],
            )
        with gr.Tab(label="🛠️字体再生成"):
            with gr.Column():
                with gr.Row():
                    old_name = gr.Textbox(
                        label="旧字体名称", placeholder="请输入需要重新生成的旧字体名称"
                    )
                    new_name = gr.Textbox(
                        label="新字体名称",
                        placeholder="请输入需要重新生成的新字体名称,如果为空.则默认旧名称不变",
                    )
                    alert = gr.Textbox(
                        interactive=False,
                        visible=False,
                        value="请再确认一下旧字体名称,其不存在",
                    )

                gen_new_font_button = gr.Button(
                    "🎢重新生成,约5分钟", variant="secondary"
                )
                progress = gr.Textbox(interactive=False, value="")
                download_button = gr.DownloadButton(label="🎁点击下载", variant="stop")

            gen_new_font_button.click(
                fn=re_gen_font,
                inputs=[old_name, new_name],
                outputs=[progress, alert, download_button],
            )

        def dummy_function(image):
            return image

        Generate_Font.click(
            fn=generate_font,  # 当用户点击确认后调用的函数
            inputs=[upload_pic_style, font_name, font_version, test_font_checkbox],
            outputs=show,
        )
        refreshing.click(
            fn=download_font, inputs=[font_name], outputs=[preview_image, download]
        )

        reference_image.upload(
            dummy_function, inputs=reference_image, outputs=reference_image
        )
        FontDiffuser.click(
            fn=run_fontdiffuer,
            inputs=[
                character,
                reference_image,
                sampling_step,
                guidance_scale,
            ],
            outputs=fontdiffuer_output_image,
        )

    # Add Gradio app as a FastAPI route
    app = gr.mount_gradio_app(app, demo, path="/")

    uvicorn.run(app, host="0.0.0.0", port=813, log_level="info")
    # python font_complex_ui.py
    # nohup python font_complex_ui.py > v_complex.log &
