### Environment Setup
**Step last-end**: 
```bash
npm install
rm -rf svg_separate/
rm -rf pico/
mkdir svg_separate
mkdir pico
# linux安装
apt-get install python3-fontforge

node potrace.js /mnt/data/llch/FontDiffuser/pic/cpp/ans
node run_pico.js
# 不同环境二选一 修改地址
/usr/bin/python3 to_ttf.py --name cpp --v v1.0
ffpython to_ttf.py  # windows
```

**Step 1**: Create a conda environment and activate it.
```bash
conda create -n fontdiffuser python=3.9 -y
conda activate fontdiffuser
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

## 🏋️ Training
### Data Construction
The training data files tree should be (The data examples are shown in directory `data_examples/train/`):
```
├──data_examples
│   └── train
│       ├── ContentImage
│       │   ├── char0.png
│       │   ├── char1.png
│       │   ├── char2.png
│       │   └── ...
│       └── TargetImage.png
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
Before running the training script (including the following three modes), you should set the training configuration, such as distributed training, through:
```bash
accelerate config
```

### Training - Pretraining of SCR
```bash
Coming Soon ...
```

### Training - Phase 1
```bash
sh train_phase_1.sh
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
After the phase 2 training, you should put the trained checkpoint files (`unet.pth`, `content_encoder.pth`, and `style_encoder.pth`) to the directory `phase_1_ckpt`. During phase 2, these parameters will be resumed.
```bash
sh train_phase_2.sh
```
- `phase_2`: Tag to phase 2 training.
- `phase_1_ckpt_dir`: The model checkpoints saving directory after phase 1 training.
- `scr_ckpt_path`: The ckpt path of pre-trained SCR module. You can download it from above 🔥Model Zoo.
- `sc_coefficient`: The coefficient of style contrastive loss for supervision.
- `num_neg`: The number of negative samples, default to be `16`.

## 📺 Sampling
### Step 1 => Prepare the checkpoint   
Option (1) Download the checkpoint following [GoogleDrive](https://drive.google.com/drive/folders/12hfuZ9MQvXqcteNuz7JQ2B_mUcTr-5jZ?usp=drive_link) / [BaiduYun:gexg](https://pan.baidu.com/s/19t1B7le8x8L2yFGaOvyyBQ), then put the `ckpt` to the root directory, including the files `unet.pth`, `content_encoder.pth`, and `style_encoder.pth`.  
Option (2) Put your re-training checkpoint folder `ckpt` to the root directory, including the files `unet.pth`, `content_encoder.pth`, and `style_encoder.pth`.

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
**Note** Maybe you need a ttf file that contains numerous Chinese characters, you can download it from [BaiduYun:wrth](https://pan.baidu.com/s/1LhcXG4tPcso9BLaUzU6KtQ).
```bash
sh script/sample_content_character.sh
```
- `character_input`: If set `True`, use character string as content/source input.
- `content_character`: The content/source content character string.
- The other parameters are the same as the above option (1).

## 📱 Run WebUI
### (1) Sampling by FontDiffuser
```bash
gradio gradio_app.py
```
**Example**:   
<p align="center">
<img src="figures/gradio_fontdiffuer_new.png" width="80%" height="auto">
</p>

```text
给出新的代码,使得风格特征只需要提取一次,然后应用到所有的内容图像上
需要预先计算的风格潜在表示,同时也需要修改 FontDiffuserDPMPipeline 类
```