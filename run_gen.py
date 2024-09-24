import os
import subprocess
import argparse


def run(opt):
    input_style_path = opt.input_path
    gen_output_path = os.path.basename(os.path.normpath(input_style_path))
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
    subprocess.run(["node", "run_pico.js", f"./svg_separate_{gen_output_path}", f"./pico_{gen_output_path}"])
    print(f"pico路径:./pico_{gen_output_path}")
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
    conda activate fontdiffuser
    /mnt/data/llch/FontDiffuser
    python run_gen.py --input outputs/test_diff/ --name test_diff --v v1.1
    python run_gen.py --input outputs/cpp_ai/ --name 火炬_cpp1.0 --v v1.1
    python run_gen.py --input outputs/crh_ai/ --name 火炬_crh1.0 --v v1.1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_path', default='outputs/cpp_ai/',
                        help='生成的图片地址,一定要outputs/xxx/这种格式')
    parser.add_argument('--name', dest='ttf_name', default='cpp',
                        help='字体名字')
    parser.add_argument('--v', dest='version', default='v1.0', help='字体版本')

    opt = parser.parse_args()
    run(opt)
