import subprocess
import argparse
import os


def run(opt):
    input_style_path = opt.input_path
    gen_output_path = os.path.basename(os.path.normpath(input_style_path))
    subprocess.run([
        "python", "batch_gen.py",
        "--ckpt_dir=ckpt/",
        "--content_image_dir=data_examples/basic/LXGWWenKaiGB-Light/",
        # "--content_image_dir=data_examples/basic/test/",
        f"--style_image_dir={opt.input_path}",
        f"--save_image_dir=outputs/{gen_output_path}/",
        f"--device={opt.cuda}",
        "--algorithm_type=dpmsolver++",
        "--guidance_type=classifier-free",
        "--guidance_scale=7.5",
        "--num_inference_steps=20",
        "--method=multistep"
    ])
    print(f"输出图片路径:outputs/{gen_output_path}/")
    # 目标路径
    path = 'svg_separate/'
    if not os.path.exists(path):
        os.makedirs(path)
    subprocess.run(["rm", "svg_separate/*"])
    subprocess.run(["rm", "pico/*"])
    subprocess.run(["node", "potrace.js", f"outputs/{gen_output_path}/"])
    print("potrace suc")
    subprocess.run(["node", "run_pico.js"])
    print("pico suc")
    subprocess.run(["/usr/bin/python3", "to_ttf.py", "--name", f"{opt.ttf_name}", "--v", f"{opt.version}"])
    print(f"{opt.ttf_name}.ttf")


if __name__ == '__main__':
    """
    source activate fontdiffuser
    cd /mnt/data/llch/FontDiffuser
    python run_all.py --input data_examples/test_diff/ --name test --v v1.0 --cuda cuda:2
    python run_all.py --input data_examples/test_style/fzfs_ai/ --name fzfs --v v1.1 --cuda cuda:0
    python run_all.py --input data_examples/test_style/FZZCHJW_ai/ --name FZZCHJW --v v1.1 --cuda cuda:1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_path', default='pic/cpp/ans',
                        help='图片地址')
    parser.add_argument('--name', dest='ttf_name', default='cpp',
                        help='字体名字')
    parser.add_argument('--v', dest='version', default='v1.0', help='字体版本')
    parser.add_argument('--cuda', dest='cuda', default='cuda:0', help='gpu')

    opt = parser.parse_args()
    run(opt)
