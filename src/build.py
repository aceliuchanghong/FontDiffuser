from diffusers.schedulers.scheduling_ddpm import DDPMScheduler
from src import (ContentEncoder,
                 StyleEncoder,
                 UNet,
                 SCR)


def build_unet(args):
    unet = UNet(
        sample_size=args.resolution,  # # 输入图像的分辨率，通常为图像的宽或高
        in_channels=3,
        out_channels=3,
        flip_sin_to_cos=True,  # 是否将sin函数转换为cos函数，用于调制频率的平移
        freq_shift=0,  # 频率偏移，通常用于调整正弦/余弦波频率
        down_block_types=('DownBlock2D',
                          'MCADownBlock2D',
                          'MCADownBlock2D',
                          'DownBlock2D'),  # UNet中的下采样块类型列表
        up_block_types=('UpBlock2D',
                        'StyleRSIUpBlock2D',
                        'StyleRSIUpBlock2D',
                        'UpBlock2D'),
        block_out_channels=args.unet_channels,  # 每个块的输出通道数
        layers_per_block=2,  # 每个块的层数
        downsample_padding=1,  # 下采样时的填充数量
        mid_block_scale_factor=1,  # 中间块的缩放因子，通常控制块的特征图缩放
        act_fn='silu',
        norm_num_groups=32,  # 分组归一化中的组数
        norm_eps=1e-05,  # 归一化层中的epsilon值，防止除零错误
        cross_attention_dim=args.style_start_channel * 16,  # 交叉注意力机制的维度
        attention_head_dim=1,
        channel_attn=args.channel_attn,  # 是否启用通道注意力机制
        content_encoder_downsample_size=args.content_encoder_downsample_size,
        content_start_channel=args.content_start_channel,
        reduction=32,  # 通道缩减率，用于控制参数和计算量
    )

    return unet


def build_style_encoder(args):
    style_image_encoder = StyleEncoder(
        G_ch=args.style_start_channel,
        resolution=args.style_image_size[0])
    print("Get CG-GAN Style Encoder!")
    return style_image_encoder


def build_content_encoder(args):
    content_image_encoder = ContentEncoder(
        G_ch=args.content_start_channel,
        resolution=args.content_image_size[0])
    print("Get CG-GAN Content Encoder!")
    return content_image_encoder


def build_scr(args):
    scr = SCR(
        temperature=args.temperature,
        mode=args.mode,
        image_size=args.scr_image_size)
    print("Loaded SCR module for supervision successfully!")
    return scr


def build_ddpm_scheduler(args):
    ddpm_scheduler = DDPMScheduler(
        num_train_timesteps=1000,
        beta_start=0.0001,
        beta_end=0.02,
        beta_schedule=args.beta_scheduler,
        trained_betas=None,
        variance_type="fixed_small",
        clip_sample=True)
    return ddpm_scheduler
