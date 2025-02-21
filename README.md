### Environment Setup

**Step 1**: Create a conda environment and activate it.

```bash
conda create -n fontdiffuser python=3.9 -y
conda activate fontdiffuser
source activate fontdiffuser
```

**Step 2**: Install related version Pytorch following [here](https://pytorch.org/get-started/previous-versions/).(其他版本其实也可以,没必要一定)

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
gen:
python ttf/font2image_new.py --base_path ttf/LXGWWenKaiGB-Light.ttf \
        --out_path ttf_pics/LXGWWenKaiGB-Light/
python ttf/image_rename_with_dir.py

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
nohup sh scripts/train_phase_1.sh > outputs/train_phase_1.log 2>&1 &
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

After the phase 1 training, you should put the trained checkpoint files (`unet.pth`, `content_encoder.pth`,
and `style_encoder.pth`) to the directory `phase_1_ckpt`. During phase 2, these parameters will be resumed.

```bash
nohup sh scripts/train_phase_2.sh > outputs/train_phase_2.log 2>&1 &
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

### Sampling by FontDiffuser

```bash
python font_easy_ui.py
python font_complex_ui.py
```

### Prepare before start

```
data_examples/basic/test/ ==>测试字体图片的目录,2000字
data_examples/basic/LXGWWenKaiGB-Light/ ==>全图片路径
(python dataset/font2image_example.py --font_in ttf/LXGWWenKaiGB-Light.ttf \
        --image_out data_examples/basic/ \
        --char_file char7000.txt)
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


---
1.分析字体风格迁移有哪几个模块 2.模型架构帮我解释一下 3.给出每个模型的pytorch代码
---
### 1. 字体风格迁移的模块分析

字体风格迁移任务通常涉及以下几个关键模块：

1. **内容编码器（Content Encoder）**：
   - 负责从源图像中提取内容特征，通常使用卷积神经网络（CNN）来捕捉字符的结构和笔画信息。
   - 在FontDiffuser中，内容编码器提取多尺度的内容特征，以保留复杂字符的细节。

2. **风格编码器（Style Encoder）**：
   - 负责从参考图像中提取风格特征，通常使用CNN或VGG网络来捕捉字体的风格信息。
   - 在FontDiffuser中，风格编码器提取风格嵌入，并通过交叉注意力机制将其注入到生成过程中。

3. **生成器（Generator）**：
   - 负责将内容和风格特征结合起来，生成目标风格的字体图像。
   - 在FontDiffuser中，生成器基于扩散模型（Diffusion Model），通过逐步去噪的过程生成字体图像。

4. **多尺度内容聚合模块（Multi-scale Content Aggregation, MCA）**：
   - 该模块用于在不同尺度上聚合全局和局部内容特征，以保留复杂字符的细节。
   - 在FontDiffuser中，MCA模块通过通道注意力和交叉注意力机制，将多尺度内容特征注入到UNet中。

5. **风格对比精炼模块（Style Contrastive Refinement, SCR）**：
   - 该模块用于对比学习风格特征，确保生成的字体风格与目标风格一致。
   - 在FontDiffuser中，SCR模块通过对比损失来监督生成过程，确保生成的字体风格与参考风格一致。

6. **参考结构交互模块（Reference-Structure Interaction, RSI）**：
   - 该模块用于处理源图像和目标图像之间的结构差异（如字体大小）。
   - 在FontDiffuser中，RSI模块通过可变形卷积网络（DCN）和交叉注意力机制来处理结构变形。

### 2. 模型架构解释

FontDiffuser的模型架构主要包括以下几个部分：

1. **条件扩散模型（Conditional Diffusion Model）**：
   - 该模型基于去噪扩散概率模型（DDPM），通过逐步去噪的过程生成字体图像。
   - 模型输入包括源图像和参考图像，输出为生成的字体图像。
   - 模型的核心是一个UNet网络，包含内容编码器、风格编码器、MCA模块和RSI模块。

2. **UNet网络**：
   - UNet网络由多个卷积块、下采样块、上采样块、MCA块和风格插入块（SI）组成。
   - 内容编码器提取多尺度内容特征，风格编码器提取风格嵌入。
   - MCA模块通过通道注意力和交叉注意力机制，将多尺度内容特征注入到UNet中。
   - RSI模块通过可变形卷积网络（DCN）和交叉注意力机制处理结构变形。

3. **风格对比精炼模块（SCR）**：
   - SCR模块通过对比学习风格特征，确保生成的字体风格与目标风格一致。
   - SCR模块使用VGG网络提取风格特征，并通过对比损失来监督生成过程。

### 3. 每个模块的PyTorch代码实现

以下是FontDiffuser中各个模块的PyTorch代码实现示例：

#### 1. 内容编码器（Content Encoder）

```python
import torch
import torch.nn as nn

class ContentEncoder(nn.Module):
    def __init__(self):
        super(ContentEncoder, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)
        self.conv4 = nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        x1 = torch.relu(self.conv1(x))
        x2 = torch.relu(self.conv2(x1))
        x3 = torch.relu(self.conv3(x2))
        x4 = torch.relu(self.conv4(x3))
        return [x1, x2, x3, x4]
```

#### 2. 风格编码器（Style Encoder）

```python
class StyleEncoder(nn.Module):
    def __init__(self):
        super(StyleEncoder, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)
        self.conv4 = nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1)
        self.fc = nn.Linear(512 * 8 * 8, 512)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = torch.relu(self.conv4(x))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
```

#### 3. 多尺度内容聚合模块（MCA）

```python
class MCA(nn.Module):
    def __init__(self, channels):
        super(MCA, self).__init__()
        self.conv = nn.Conv2d(channels, channels, kernel_size=1)
        self.attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(channels, channels // 8, kernel_size=1),
            nn.ReLU(),
            nn.Conv2d(channels // 8, channels, kernel_size=1),
            nn.Sigmoid()
        )

    def forward(self, x, style_embedding):
        x = self.conv(x)
        attention = self.attention(x)
        x = x * attention
        return x
```

#### 4. 风格对比精炼模块（SCR）

```python
class SCR(nn.Module):
    def __init__(self):
        super(SCR, self).__init__()
        self.vgg = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 512, kernel_size=3, stride=2, padding=1),
            nn.ReLU()
        )
        self.fc = nn.Linear(512 * 8 * 8, 512)

    def forward(self, x):
        x = self.vgg(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
```

#### 5. 参考结构交互模块（RSI）

```python
class RSI(nn.Module):
    def __init__(self, channels):
        super(RSI, self).__init__()
        self.conv = nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.dcn = DeformConv2d(channels, channels, kernel_size=3, padding=1)

    def forward(self, x, reference_feature):
        offset = self.conv(reference_feature)
        x = self.dcn(x, offset)
        return x
```

#### 6. UNet网络

```python
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.down1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.down2 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.down3 = nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)
        self.up1 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.up2 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.up3 = nn.ConvTranspose2d(64, 3, kernel_size=2, stride=2)

    def forward(self, x):
        x1 = torch.relu(self.down1(x))
        x2 = torch.relu(self.down2(x1))
        x3 = torch.relu(self.down3(x2))
        x = torch.relu(self.up1(x3))
        x = torch.relu(self.up2(x))
        x = torch.relu(self.up3(x))
        return x
```

### 总结
FontDiffuser通过引入多尺度内容聚合模块（MCA）、风格对比精炼模块（SCR）和参考结构交互模块（RSI）
---

给出每个模块的论文的原始描述,公式之类

---

分析字体风格迁移主要包括以下几个模块：

1. **多尺度内容聚合（MCA）块**
2. **参考结构交互（RSI）块**
3. **风格对比细化（SCR）模块**

### 1. 多尺度内容聚合（MCA）块

**论文原始描述：**
为了增强复杂字符的保存，我们采用一个多尺度内容聚合（MCA）块来将全局和局部内容线索注入到UNet模型中。

**公式：**
内容特征 fci 与先前的 UNet 块特征 ri 连接，形成一个通道信息特征 Ic。然后应用通道注意力机制，通过平均池化、两个 1×1 卷积和激活函数得到全局通道感知向量 Wc，用于加权通道信息特征 Ic。之后通过残差连接和 1×1 卷积减少 Ic′ 的通道数，得到输出 Ico。最后应用交叉注意力模块插入风格嵌入 es。

### 2. 参考结构交互（RSI）块

**论文原始描述：**
为了解决源图像和目标图像之间的结构性差异（如字体大小），我们提出了一种参考结构交互（RSI）块，该块采用可变形卷积网络（DCN）在UNet的跳跃连接上进行结构变形。

**公式：**
参考图像 xs 首先通过内容编码器 Ec 获得结构图 F s={fs1, fs2}，每个 fsi 分别作为 RSI 模块的输入。引入交叉注意力以实现长距离交互，其过程可以总结如下：
\[ \text{Ss} \in R^{C_i}, \text{Sr} \in R^{C_i} \]
\[ Q = \Phi_q(Ss), K = \Phi_k(Sr), V = \Phi_v(Sr) \]
\[ F_{\text{attn}} = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \]
\[ \delta_{\text{offset}} = \text{FFN}(F_{\text{attn}}) \]
\[ I_R = \text{DCN}(r_i, \delta_{\text{offset}}) \]

### 3. 风格对比细化（SCR）模块

**论文原始描述：**
我们提出一种风格对比细化（SCR）模块，这是一个字体风格表示学习模块，从一组样本图像中解耦风格，并结合风格对比损失监督扩散模型，确保生成的风格在全局和局部层面与目标一致。

**公式：**
\[ L_{\text{sc}} = -\sum_{l=0}^{N-1} \log \frac{\exp(v_0^l \cdot v_p^l / \tau)}{\exp(v_0^l \cdot v_p^l / \tau) + \sum_{i=1}^K \exp(v_0^l \cdot v_{ni}^l / \tau)} \]
其中 Extrac 表示风格提取器，K 是负样本的数量，V0、Vp 和 Vn 分别表示生成、正样本和负样本的风格向量，v0l、vpl、vnli 分别表示第 l 层生成、正样本和负样本的层向量，τ 是温度超参数，设置为 0.07。

---

`MCA` `RSI`  `SCR`
给出pytorch模型架构代码,并且给出损失函数代码

---

以下是基于描述的 `MCA`、`RSI` 和 `SCR` 模块的 PyTorch 实现代码，以及损失函数的实现代码。


### **1. MCA (Multi-scale Content Aggregation) 模块**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MCA(nn.Module):
    def __init__(self, in_channels, reduction=16):
        super(MCA, self).__init__()
        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels, in_channels // reduction, kernel_size=1, bias=False),
            nn.ReLU(),
            nn.Conv2d(in_channels // reduction, in_channels, kernel_size=1, bias=False),
            nn.Sigmoid()
        )
        self.conv1x1 = nn.Conv2d(in_channels * 2, in_channels, kernel_size=1)

    def forward(self, content_feature, unet_feature):
        # Concatenate content feature and UNet feature
        concat_feature = torch.cat([content_feature, unet_feature], dim=1)
        
        # Apply channel attention
        attention_weights = self.channel_attention(concat_feature)
        weighted_feature = concat_feature * attention_weights
        
        # Reduce channel dimension
        output = self.conv1x1(weighted_feature)
        return output
```


### **2. RSI (Reference-Structure Interaction) 模块**

```python
class CrossAttention(nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super(CrossAttention, self).__init__()
        self.multihead_attn = nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, query, key, value):
        attn_output, _ = self.multihead_attn(query, key, value)
        return attn_output

class RSI(nn.Module):
    def __init__(self, in_channels, embed_dim=256, num_heads=8):
        super(RSI, self).__init__()
        self.cross_attention = CrossAttention(embed_dim, num_heads)
        self.offset_predictor = nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Linear(embed_dim, 2)  # Predict offsets for deformable convolution
        )
        self.deform_conv = DeformConv2d(in_channels, in_channels, kernel_size=3, padding=1)

    def forward(self, unet_feature, structure_map):
        B, C, H, W = unet_feature.shape
        
        # Flatten features for cross-attention
        query = unet_feature.flatten(2).permute(2, 0, 1)  # [H*W, B, C]
        key = value = structure_map.flatten(2).permute(2, 0, 1)  # [H*W, B, C]
        
        # Cross-attention interaction
        attn_output = self.cross_attention(query, key, value)  # [H*W, B, C]
        attn_output = attn_output.permute(1, 2, 0).view(B, C, H, W)
        
        # Predict offsets for deformable convolution
        offset = self.offset_predictor(attn_output.permute(0, 2, 3, 1).reshape(-1, C))
        offset = offset.view(B, H, W, 2).permute(0, 3, 1, 2)
        
        # Apply deformable convolution
        output = self.deform_conv(unet_feature, offset)
        return output
```


### **3. SCR (Style Contrastive Refinement) 模块**

```python
class StyleExtractor(nn.Module):
    def __init__(self):
        super(StyleExtractor, self).__init__()
        self.vgg = torchvision.models.vgg19(pretrained=True).features[:30]  # Use first 30 layers of VGG19
        for param in self.vgg.parameters():
            param.requires_grad = False  # Freeze VGG weights

    def forward(self, x):
        features = []
        for layer in self.vgg:
            x = layer(x)
            if isinstance(layer, nn.ReLU):  # Extract after ReLU activation
                features.append(x)
        return features

class SCR(nn.Module):
    def __init__(self, num_layers=6, embed_dim=512):
        super(SCR, self).__init__()
        self.style_extractor = StyleExtractor()
        self.projectors = nn.ModuleList([nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(embed_dim, embed_dim, kernel_size=1),
            nn.ReLU()
        ) for _ in range(num_layers)])

    def forward(self, x):
        style_features = self.style_extractor(x)
        projected_features = [projector(feat) for projector, feat in zip(self.projectors, style_features)]
        return projected_features
```
### **4. 损失函数**

#### **(1) 风格对比损失 (Style Contrastive Loss)**

```python
def style_contrastive_loss(style_vectors, target_style, negative_styles, temperature=0.07):
    """
    Args:
        style_vectors: List of style vectors from different layers.
        target_style: Target style vector (positive sample).
        negative_styles: List of negative style vectors.
        temperature: Temperature hyperparameter.
    Returns:
        Contrastive loss.
    """
    loss = 0
    for l in range(len(style_vectors)):
        v_gen = style_vectors[l]  # Generated style vector
        v_pos = target_style[l]   # Positive style vector
        v_neg = torch.stack([neg[l] for neg in negative_styles])  # Negative style vectors
        
        # Compute similarity scores
        pos_sim = torch.exp(torch.cosine_similarity(v_gen, v_pos) / temperature)
        neg_sim = torch.sum(torch.exp(torch.cosine_similarity(v_gen.unsqueeze(0), v_neg, dim=-1)) / temperature)
        
        # Contrastive loss for this layer
        loss += -torch.log(pos_sim / (pos_sim + neg_sim))
    
    return loss.mean()
```

#### **(2) 扩散模型的噪声预测损失**

```python
def diffusion_loss(predicted_noise, true_noise):
    """
    Args:
        predicted_noise: Noise predicted by the model.
        true_noise: Actual noise added to the input.
    Returns:
        MSE loss between predicted and true noise.
    """
    return F.mse_loss(predicted_noise, true_noise)
```

### **5. 整体模型架构**

```python
class FontDiffuser(nn.Module):
    def __init__(self):
        super(FontDiffuser, self).__init__()
        self.content_encoder = nn.Sequential(...)  # Define content encoder
        self.style_encoder = nn.Sequential(...)    # Define style encoder
        self.unet = UNet()                        # Define UNet with MCA and RSI blocks
        self.scr = SCR()                          # Style Contrastive Refinement module

    def forward(self, source_image, reference_image, xt, t):
        # Encode content and style
        content_features = self.content_encoder(source_image)
        style_embedding = self.style_encoder(reference_image)
        
        # Inject multi-scale content features into UNet
        unet_output = self.unet(xt, content_features, style_embedding, t)
        
        # Predict noise
        predicted_noise = unet_output
        
        return predicted_noise
```

### **6. 训练过程中的总损失**

```python
def total_loss(predicted_noise, true_noise, generated_image, target_image, style_vectors, target_style, negative_styles):
    # Diffusion loss
    diff_loss = diffusion_loss(predicted_noise, true_noise)
    
    # Style contrastive loss
    scr_loss = style_contrastive_loss(style_vectors, target_style, negative_styles)
    
    # Total loss
    total_loss = diff_loss + 0.01 * scr_loss
    return total_loss
```


以上代码实现了 `MCA`、`RSI` 和 `SCR` 模块的核心逻辑，并定义了相应的损失函数。你可以根据具体需求进一步调整和优化这些模块。

---

---

---

---

---

---

---

---

---

---

---

---
