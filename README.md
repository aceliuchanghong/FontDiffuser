### Environment Setup

**Step 1**: Create a conda environment and activate it.

```bash
conda create -n fontdiffuser python=3.9 -y
conda activate fontdiffuser
source activate fontdiffuser
```

**Step 2**: Install related version Pytorch following [here](https://pytorch.org/get-started/previous-versions/).

```bash
# Suggested
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

**Step 3**: Install the required packages.

```bash
pip install -r requirements.txt
```

**Step last-end**:

```bash
# 字体生成
npm install
apt-get install python3-fontforge

# 全流程生成 打开文件查看用法
run_all.py
# 半流程
run_gen.py
## 🏋️ Training
### Data Construction
The training data files tree should be ( The data examples are shown in directory `data_examples/train/`):
```

```
├──data_examples
│   └── train
│       ├── ContentImage
│       │   ├── char0.png
│       │   ├── char1.png
│       │   ├── char2.png
│       │   └── ...
│       └── TargetImage
│           ├── style0
│           │     ├──style0+char0.png
│           │     ├──style0+char1.png
│           │     └── ...
│           ├── style1
│           │     ├──style1+char0.png
│           │     ├──style1+char1.png
│           │     └── ...
│           ├── style2
│           │     ├──style2+char0.png
│           │     ├──style2+char1.png
│           │     └── ...
│           └── ...
```

### Training Configuration

Before running the training script (including the following three modes), you should set the training configuration,
such as distributed training, through:

```bash
accelerate config
```

### Training - Pretraining of SCR

```bash
Coming Soon ...
```

### Training - Phase 1

```bash
sh scripts/train_phase_1.sh
```

- `data_root`: The data root, as `./data_examples`
- `output_dir`: The training output logs and checkpoints saving directory.
- `resolution`: The resolution of the UNet in our diffusion model.
- `style_image_size`: The resolution of the style image, can be different with `resolution`.
- `content_image_size`: The resolution of the content image, should be the same as the `resolution`.
- `channel_attn`: Whether to use the channel attention in the MCA block.
- `train_batch_size`: The batch size in the training.
- `max_train_steps`: The maximum of the training steps.
- `learning_rate`: The learning rate when training.
- `ckpt_interval`: The checkpoint saving interval when training.
- `drop_prob`: The classifier-free guidance training probability.

### Training - Phase 2

After the phase 2 training, you should put the trained checkpoint files (`unet.pth`, `content_encoder.pth`,
and `style_encoder.pth`) to the directory `phase_1_ckpt`. During phase 2, these parameters will be resumed.

```bash
sh scripts/train_phase_2.sh
```

- `phase_2`: Tag to phase 2 training.
- `phase_1_ckpt_dir`: The model checkpoints saving directory after phase 1 training.
- `scr_ckpt_path`: The ckpt path of pre-trained SCR module. You can download it from above 🔥Model Zoo.
- `sc_coefficient`: The coefficient of style contrastive loss for supervision.
- `num_neg`: The number of negative samples, default to be `16`.

## 📺 Sampling

### Step 1 => Prepare the checkpoint

Option (1) put the `ckpt` to the root directory, including the files `unet.pth`, `content_encoder.pth`,
and `style_encoder.pth`.  
Option (2) Put your re-training checkpoint folder `ckpt` to the root directory, including the
files `unet.pth`, `content_encoder.pth`, and `style_encoder.pth`.

### Step 2 => Run the script

**(1) Sampling image from content image and reference image.**

```bash
sh script/sample_content_image.sh
```

- `ckpt_dir`: The model checkpoints saving directory.
- `content_image_path`: The content/source image path.
- `style_image_path`: The style/reference image path.
- `save_image`: set `True` if saving as images.
- `save_image_dir`: The image saving directory, the saving files including an `out_single.png` and an `out_with_cs.png`.
- `device`: The sampling device, recommended GPU acceleration.
- `guidance_scale`: The classifier-free sampling guidance scale.
- `num_inference_steps`: The inference step by DPM-Solver++.

**(2) Sampling image from content character.**  
**Note** Maybe you need a ttf file that contains numerous Chinese characters

```bash
sh script/sample_content_character.sh
```

- `character_input`: If set `True`, use character string as content/source input.
- `content_character`: The content/source content character string.
- The other parameters are the same as the above option (1).

## 📱 Run WebUI

### (1) Sampling by FontDiffuser

```bash
python font_easy_ui.py
python font_complex_ui.py
```

```text
给出新的代码,使得风格特征只需要提取一次,然后应用到所有的内容图像上,需要预先计算的风格潜在表示,同时也需要修改 FontDiffuserDPMPipeline 类

1.帮我解释一下整体字体风格迁移的架构 2.给出每个类和一些关键函数的左右 3.给出代码执行流向

```

```text
整体架构:
系统采用了扩散模型(Diffusion Model)的架构,主要包含以下几个关键组件:
UNet: 核心网络,用于生成噪声预测。
内容编码器(Content Encoder): 提取内容特征。
风格编码器(Style Encoder): 提取风格特征。
DPM Solver: 用于从噪声中采样生成图像。
classifier-free:使得模型能够在无监督的情况下进行更灵活的生成，提升了整体的生成能力和效果。

FontDiffuserModelDPM (src/model.py):
这是整个模型的核心类,整合了UNet、内容编码器和风格编码器。其forward方法处理输入,提取特征,并通过UNet生成噪声预测。
StyleEncoder (src/modules/style_encoder.py):
负责提取风格图像的特征。
FontDiffuserDPMPipeline (batch_gen.py):
这是整个生成过程的pipeline,包括加载模型、处理输入、运行扩散过程和保存结果。
使用DPM_Solver调度器实现图像生成的完整流程。generate方法实现从高斯噪声到最终图像的转化
train.py 训练:
训练过程包括数据加载、模型构建、优化器设置和训练循环。使用了Accelerator来支持分布式训练。


FontDiffuserModel
- 负责使用UNet、风格编码器和内容编码器进行正向推理。
- `forward`方法执行图像的噪声预测并返回噪声预测和偏移输出总和。
NoiseScheduleVP
- 定义正向SDE（如离散噪声计划）所需的系数计算。
DPM_Solver
- 实现DPM-Solver和DPM-Solver++算法以解决SDE。
- singlestep_dpm_solver_update和multistep_dpm_solver_update等方法用于解算具体的更新步骤。
```
