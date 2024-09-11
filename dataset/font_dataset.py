import os
import random
from PIL import Image

import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms


def get_nonorm_transform(resolution):
    nonorm_transform = transforms.Compose(
        [transforms.Resize((resolution, resolution),
                           interpolation=transforms.InterpolationMode.BILINEAR),
         transforms.ToTensor()])
    return nonorm_transform


class FontDataset(Dataset):
    """
    The dataset of font generation
    类的核心功能：加载特定格式的字体图像数据集，结合内容图像、风格图像，并在需要时生成负样本用于对比学习。
    图像处理：通过 PIL 读取图像，并使用 transforms 进行预处理。
    灵活性：支持根据输入的参数选择是否生成负样本，并通过 transforms 进行自定义图像处理。
    """

    def __init__(self, args, phase, transforms=None, scr=False):
        super().__init__()
        self.root = args.data_root  # 数据集的根目录
        self.phase = phase  # 训练或测试阶段
        self.scr = scr  # 是否使用负样本对比学习
        if self.scr:
            self.num_neg = args.num_neg  # 负样本的数量
        self.get_path()  # 初始化数据路径
        self.transforms = transforms  # 图像变换（可能为None）
        self.nonorm_transforms = get_nonorm_transform(args.resolution)  # 不进行归一化的图像变换

    def get_path(self):
        """
        该方法遍历目标图像文件夹，将所有图像路径存储在 target_images 列表中，同时按照字体风格将图像分类到 style_to_images 字典中。
        """
        self.target_images = []  # 存储所有目标图像的路径
        # images with related style  
        self.style_to_images = {}  # 以风格为键，存储对应的目标图像路径
        target_image_dir = f"{self.root}/{self.phase}/TargetImage"
        for style in os.listdir(target_image_dir):
            images_related_style = []
            for img in os.listdir(f"{target_image_dir}/{style}"):
                img_path = f"{target_image_dir}/{style}/{img}"
                self.target_images.append(img_path)
                images_related_style.append(img_path)
            self.style_to_images[style] = images_related_style  # 每种风格对应的图像路径

    def __getitem__(self, index):
        target_image_path = self.target_images[index]
        target_image_name = target_image_path.split('/')[-1]
        style, content = target_image_name.split('.')[0].split('+')

        # Read content image
        content_image_path = f"{self.root}/{self.phase}/ContentImage/{content}.jpg"
        content_image = Image.open(content_image_path).convert('RGB')

        # Random sample used for style image
        images_related_style = self.style_to_images[style].copy()
        images_related_style.remove(target_image_path)
        style_image_path = random.choice(images_related_style)
        style_image = Image.open(style_image_path).convert("RGB")

        # Read target image
        target_image = Image.open(target_image_path).convert("RGB")
        nonorm_target_image = self.nonorm_transforms(target_image)

        if self.transforms is not None:
            content_image = self.transforms[0](content_image)
            style_image = self.transforms[1](style_image)
            target_image = self.transforms[2](target_image)

        """
        通过给定的索引，加载目标图像、内容图像和随机选取的风格图像，
        并对它们进行相应的转换。self.transforms 是一个可选的变换操作列表，分别应用于内容图像、风格图像和目标图像。
        """
        sample = {
            "content_image": content_image,
            "style_image": style_image,
            "target_image": target_image,
            "target_image_path": target_image_path,
            "nonorm_target_image": nonorm_target_image}

        if self.scr:
            """
            在 scr=True 时，从不同风格的图像中随机选择负样本，
            并将它们加载到 sample 中。负样本图像的处理和目标图像类似，应用相应的变换后通过 torch.cat 拼接。
            """
            # Get neg image from the different style of the same content
            style_list = list(self.style_to_images.keys())
            style_index = style_list.index(style)
            style_list.pop(style_index)
            choose_neg_names = []
            for i in range(self.num_neg):
                choose_style = random.choice(style_list)
                choose_index = style_list.index(choose_style)
                style_list.pop(choose_index)
                choose_neg_name = f"{self.root}/train/TargetImage/{choose_style}/{choose_style}+{content}.jpg"
                choose_neg_names.append(choose_neg_name)

            # Load neg_images
            for i, neg_name in enumerate(choose_neg_names):
                neg_image = Image.open(neg_name).convert("RGB")
                if self.transforms is not None:
                    neg_image = self.transforms[2](neg_image)
                if i == 0:
                    neg_images = neg_image[None, :, :, :]
                else:
                    neg_images = torch.cat([neg_images, neg_image[None, :, :, :]], dim=0)
            sample["neg_images"] = neg_images

        return sample

    def __len__(self):
        return len(self.target_images)
