import subprocess
import argparse


def run(opt):
    subprocess.run(["node", "potrace.js", f"{opt.input_path}"])
    print("potrace suc")
    subprocess.run(["node", "run_pico.js"])
    print("pico suc")
    subprocess.run(["/usr/bin/python3", "to_ttf.py", "--name", f"{opt.ttf_name}", "--v", f"{opt.version}"])
    print(f"{opt.ttf_name}.ttf")


if __name__ == '__main__':
    """
    conda activate fontdiffuser
    /mnt/data/llch/FontDiffuser
    python run_gen.py --input outputs/cpp3/ --name cpp --v v1.1
    python run_gen.py --input outputs/crh3/ --name crh --v v1.1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_path', default='pic/cpp/ans',
                        help='图片地址')
    parser.add_argument('--name', dest='ttf_name', default='cpp',
                        help='字体名字')
    parser.add_argument('--v', dest='version', default='v1.0', help='字体版本')

    opt = parser.parse_args()
    run(opt)
