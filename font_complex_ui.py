import random
import gradio as gr

from dataset.font2image import process_fonts
from sample import (arg_parse,
                    sampling,
                    load_fontdiffuer_pipeline)
import uvicorn
from fastapi import FastAPI
from PIL import Image
import os


def run_fontdiffuer(
        character,
        reference_image,
        sampling_step,
        guidance_scale,
):
    source_image = args.ttf_pic_path + "/" + character[0] + ".png"
    if not os.path.exists(source_image):
        try:
            process_fonts('ttf', 'ttf_pics', character[0])
        except Exception as e:
            print(e)
    source_image = Image.open(source_image).convert('RGB')
    args.character_input = False if source_image is not None else True
    args.content_character = character
    args.sampling_step = sampling_step
    args.guidance_scale = guidance_scale
    args.seed = random.randint(0, 10000)
    out_image = sampling(
        args=args,
        pipe=pipe,
        content_image=source_image,
        style_image=reference_image)
    return out_image


# Initialize FastAPI
app = FastAPI()

if __name__ == '__main__':
    """
    conda activate fontdiffuser
    python font_complex_ui.py
    nohup python font_complex_ui.py > s_words2.log &
    """
    args = arg_parse()
    args.demo = True
    args.ckpt_dir = 'ckpt'
    args.ttf_path = 'ttf/LXGWWenKaiGB-Light.ttf'
    args.ttf_pic_path = 'ttf_pics/LXGWWenKaiGB-Light/'

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
                                examples=[
                                    "data_examples/sampling/crh.png",
                                    "data_examples/sampling/依.png",
                                    "data_examples/train/ContentImage/氮.jpg",
                                    "data_examples/sampling/哀.png",
                                    "data_examples/train/TargetImage/FZGuanJKSJW/FZGuanJKSJW+氮.jpg",
                                    "data_examples/train/TargetImage/FZOuYHGXSJW/FZOuYHGXSJW+舶.jpg",
                                    "data_examples/sampling/9_802_1790.jpg",
                                    "data_examples/sampling/example_style.jpg",
                                    "data_examples/train/TargetImage/FZZCHJW/FZZCHJW+潮.jpg",
                                    "data_examples/just_show/hanrui_50W/潮.png",
                                    "data_examples/just_show/HYAoDeSaiU/潮.png",
                                    "data_examples/just_show/HYChaoCuSongJ/潮.png",
                                    "data_examples/just_show/HYChenMeiZiJ/潮.png",
                                    "data_examples/just_show/HYCuSongJF/潮.png",
                                    "data_examples/just_show/HYDiShengXiLeTiW/潮.png",
                                    "data_examples/just_show/HYDiShengYingXiongTiW/潮.png",
                                    "data_examples/just_show/HYDongHaiMoXingW/潮.png",
                                    "data_examples/just_show/HYDongMeiRenW/潮.png",
                                    "data_examples/just_show/HYJiangJun-85W/潮.png",
                                    "data_examples/just_show/HYJinLingMeiSongW/潮.png",
                                    "data_examples/just_show/HYJiuWeiW/潮.png",
                                    "data_examples/just_show/HYLingXinClassic105W/潮.png",
                                    "data_examples/just_show/HYPaiBianSongW/潮.png",
                                    "data_examples/just_show/HYQinChuanFeiYingW/潮.png",
                                    "data_examples/just_show/HYQingZhouXingW/潮.png",
                                    "data_examples/just_show/HYShangWeiMoYouW/潮.png",
                                    "data_examples/just_show/HYXiaoMaiTiJ/潮.png",
                                    "data_examples/just_show/HYYongZiLongHuBangW/潮.png",
                                    "data_examples/just_show/HYYongZiWuShiW/潮.png",
                                    "data_examples/just_show/HYZhuoKaiW/潮.png",
                                    "data_examples/just_show/HYZhuZiBanKeSiW/潮.png",
                                    "data_examples/just_show/HYZhuZiHaiDiShiJieW/潮.png",
                                    "data_examples/just_show/HYZhuZiHeiMoFaW/潮.png",
                                ],
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
                                                    type='pil')

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
                upload_pic_style = gr.File(label="🛠️上传字体图片(24-36张)", file_count="multiple", file_types=["image"])
                with gr.Row():
                    font_name = gr.Textbox(label='输入字体名称', value='torch', placeholder='torch', interactive=True,
                                           info='给自己的字体取个名字')
                    font_version = gr.Textbox(label='输入字体版本', value='v1.0', placeholder='v1.0', interactive=True,
                                              info='给自己的字体附加版本号')
            with gr.Column(scale=1):
                gr.HTML("""<h2 style="text-align: left; font-weight: 600; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
                                                    字体文件生成
                                                 </h2>
                                         """)
                gr.Image('data_examples/using_files/arrow2.svg', label='')
                Generate_Font = gr.Button('点击生成字体', icon='data_examples/using_files/shoot.ico',
                                          variant='primary', size="lg")
            with gr.Column(scale=2):
                with gr.Row():
                    preview_image = gr.Image(width=320, label='字体预览', image_mode='RGB', type='pil',
                                             height=320)
                    refreshing = gr.Button('📖刷新图片', variant='primary', size="lg")


        def dummy_function(image):
            return image


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
    uvicorn.run(app, host="0.0.0.0", port=813, log_level="info")
