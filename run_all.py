import subprocess
import argparse
import os

from utils_2 import fix_one_pic


def run(opt):
    input_style_path = opt.input_path
    gen_output_path = os.path.basename(os.path.normpath(input_style_path))
    subprocess.run([
        "python", "batch_gen.py",
        "--ckpt_dir=ckpt/",
        f"--content_image_dir={opt.basic_path}",
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

    fix_one_pic(opt.ttf_name)
    # 目标路径
    if not os.path.exists('svg_separate/'):
        os.makedirs(f'svg_separate/')
    if not os.path.exists(f'svg_separate_{gen_output_path}/'):
        os.makedirs(f'svg_separate_{gen_output_path}/')
    print(f"makedir:svg_separate,svg_separate_{gen_output_path}")

    subprocess.run(["rm", f"svg_separate_{gen_output_path}/*"])
    subprocess.run(["rm", f"pico_{gen_output_path}/*"])
    subprocess.run(["rm", "svg_separate/*"])
    subprocess.run(["rm", "pico/*"])

    subprocess.run(["node", "potrace.js", f"outputs/{gen_output_path}/", f"svg_separate_{gen_output_path}/"])
    print(f"svg_separate路径:svg_separate_{gen_output_path}")
    subprocess.run(["node", "run_pico.js", f"svg_separate_{gen_output_path}/", f"pico_{gen_output_path}/"])
    print(f"pico路径:pico_{gen_output_path}/")
    subprocess.run(
        ["/usr/bin/python3", "to_ttf.py", "--input", f"pico_{gen_output_path}/", "--name",
         f"{opt.ttf_name}_adjust_before", "--v", f"{opt.version}"])
    print(f"{opt.ttf_name}_adjust_before.ttf")
    subprocess.run(
        ["/usr/bin/python3", "adjust_ttf.py", "--input_ttf", f"{opt.ttf_name}_adjust_before.ttf", "--out_name",
         f"{opt.ttf_name}", "--version", f"{opt.version}", "--output_path", f"./"])
    print("\n\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n\n")
    print(f"输出图片路径:outputs/{gen_output_path}/")
    print(f"svg_separate路径:svg_separate_{gen_output_path}")
    print(f"pico路径:pico_{gen_output_path}/")
    print(f"初步字体:{opt.ttf_name}_adjust_before.ttf")
    print(f"结果字体:{opt.ttf_name}.ttf")


if __name__ == '__main__':
    """
    source activate fontdiffuser
    cd /mnt/data/llch/FontDiffuser
    python run_all.py --input data_examples/test_diff/ --name test --v v1.0 --cuda cuda:2
    python run_all.py --input data_examples/test_style/fzfs_ai/ --name fzfs --v v1.1 --cuda cuda:0
    python run_all.py --input data_examples/test_style/FZZCHJW_ai/ --name FZZCHJW --v v1.1 --cuda cuda:1
    python run_all.py --input data_examples/test_style/cpp_ai/ --name 火炬_cpp1.0 --v v1.1 --cuda cuda:2
    python run_all.py --input data_examples/test_style/crh_ai/ --name 火炬_crh1.0 --v v1.1 --cuda cuda:3
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_path', default='pic/cpp/ans',
                        help='风格图片地址')
    parser.add_argument('--name', dest='ttf_name', default='cpp',
                        help='字体名字')
    parser.add_argument('--v', dest='version', default='v1.0', help='字体版本')
    parser.add_argument('--cuda', dest='cuda', default='cuda:0', help='gpu指定')
    parser.add_argument('--basic_path', dest='basic_path', default='data_examples/basic/LXGWWenKaiGB-Light/',
                        help='basic图片地址')
    opt = parser.parse_args()
    run(opt)
