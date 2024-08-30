import os
import time
from PIL import Image
import torch
import torchvision.transforms as transforms
from accelerate.utils import set_seed
from src import (FontDiffuserDPMPipeline,
                 FontDiffuserModelDPM,
                 build_ddpm_scheduler,
                 build_unet,
                 build_content_encoder,
                 build_style_encoder)
from configs.fontdiffuser import get_parser
from tqdm import tqdm


def save_single_image(save_dir, image, name=None):
    if name is None:
        save_path = f"{save_dir}/out_single.png"
    else:
        save_path = f"{save_dir}/{name}.png"
    image.save(save_path)


def arg_parse():
    parser = get_parser()
    parser.add_argument("--ckpt_dir", type=str, default=None)
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--controlnet", type=bool, default=False, help="If in demo mode, the controlnet can be added.")
    parser.add_argument("--content_image_dir", type=str, default=None, help="Directory containing content images.")
    parser.add_argument("--style_image_dir", type=str, default=None, help="Directory containing style images.")
    parser.add_argument("--save_image_dir", type=str, default=None, help="The saving directory.")
    parser.add_argument("--device", type=str, default="cuda:2")
    parser.add_argument("--ttf_path", type=str, default="ttf/LXGWWenKaiGB-Light.ttf")
    args = parser.parse_args()
    style_image_size = args.style_image_size
    content_image_size = args.content_image_size
    args.style_image_size = (style_image_size, style_image_size)
    args.content_image_size = (content_image_size, content_image_size)

    return args


def image_process_batch(args, content_images=None, style_images=None):
    # Load content and style images
    content_images_batch = []
    style_images_batch = []

    if not args.demo:
        content_images = [Image.open(os.path.join(args.content_image_dir, img_path)).convert('RGB') for img_path in
                          content_images]
        style_images = [Image.open(os.path.join(args.style_image_dir, img_path)).convert('RGB') for img_path in
                        style_images]

        content_inference_transforms = transforms.Compose(
            [transforms.Resize(args.content_image_size, interpolation=transforms.InterpolationMode.BILINEAR),
             transforms.ToTensor(),
             transforms.Normalize([0.5], [0.5])]
        )
        style_inference_transforms = transforms.Compose(
            [transforms.Resize(args.style_image_size, interpolation=transforms.InterpolationMode.BILINEAR),
             transforms.ToTensor(),
             transforms.Normalize([0.5], [0.5])]
        )

        for content_image in content_images:
            content_image_tensor = content_inference_transforms(content_image)[None, :]
            content_images_batch.append(content_image_tensor)

        for style_image in style_images:
            style_image_tensor = style_inference_transforms(style_image)[None, :]
            style_images_batch.append(style_image_tensor)

    content_images_batch = torch.cat(content_images_batch, dim=0)
    style_images_batch = torch.cat(style_images_batch, dim=0)

    return content_images_batch, style_images_batch


def load_fontdiffuer_pipeline(args):
    # Load the model state_dict
    unet = build_unet(args=args)
    unet.load_state_dict(torch.load(f"{args.ckpt_dir}/unet.pth"))
    style_encoder = build_style_encoder(args=args)
    style_encoder.load_state_dict(torch.load(f"{args.ckpt_dir}/style_encoder.pth"))
    content_encoder = build_content_encoder(args=args)
    content_encoder.load_state_dict(torch.load(f"{args.ckpt_dir}/content_encoder.pth"))
    model = FontDiffuserModelDPM(unet=unet, style_encoder=style_encoder, content_encoder=content_encoder)
    model.to(args.device)
    print("Loaded the model state_dict successfully!")

    # Load the training ddpm_scheduler.
    train_scheduler = build_ddpm_scheduler(args=args)
    print("Loaded training DDPM scheduler successfully!")

    # Load the DPM_Solver to generate the sample.
    pipe = FontDiffuserDPMPipeline(
        model=model,
        ddpm_train_scheduler=train_scheduler,
        model_type=args.model_type,
        guidance_type=args.guidance_type,
        guidance_scale=args.guidance_scale,
    )
    print("Loaded dpm_solver pipeline successfully!")

    return pipe


def sampling_batch(args, pipe, content_images=None, style_images=None):
    os.makedirs(args.save_image_dir, exist_ok=True)

    if args.seed:
        set_seed(seed=args.seed)
    old_content_images = content_images

    content_images, style_images = image_process_batch(args=args, content_images=content_images,
                                                       style_images=style_images)
    # content_images, style_images: torch.Size([7, 3, 96, 96]) torch.Size([4, 3, 96, 96])
    print("content_images:", content_images.shape, ", style_images:", style_images.shape)

    if content_images is None:
        print("No valid content images to process.")
        return None

    with torch.no_grad():
        content_images = content_images.to(args.device)
        style_images = style_images.to(args.device)
        batch_size = style_images.size(0)

        print(f"Sampling by DPM-Solver++ with batch size {batch_size} ......")
        start = time.time()

        output_images = []
        for i in tqdm(range(0, content_images.size(0), batch_size)):
            content_batch = content_images[i:i + batch_size]
            # 如果最后一个 batch 不足，将 batch_size 调整为 content_batch 的大小
            current_batch_size = content_batch.size(0)
            images = pipe.generate(
                content_images=content_batch,
                style_images=style_images[:current_batch_size],  # 调整 style_images 的 batch size
                batch_size=current_batch_size,
                order=args.order,
                num_inference_step=args.num_inference_steps,
                content_encoder_downsample_size=args.content_encoder_downsample_size,
                t_start=args.t_start,
                t_end=args.t_end,
                dm_size=args.content_image_size,
                algorithm_type=args.algorithm_type,
                skip_type=args.skip_type,
                method=args.method,
                correcting_x0_fn=args.correcting_x0_fn
            )
            output_images.extend(images)

            if images is not None:
                for image_name, out_image in zip(old_content_images[i:i + batch_size], images):
                    save_single_image(save_dir=args.save_image_dir, image=out_image,
                                      name=image_name.replace(".png", "").replace(".jpg", ""))
                    # print(f"Saved {args.save_image_dir}/{image_name}")

        end = time.time()

        print(f"Finished the sampling process, costing time {end - start}s")

    return output_images


def process_directory_batch(args, pipe):
    content_images = [f for f in os.listdir(args.content_image_dir) if
                      f.endswith(('.png', '.jpg', '.jpeg'))]
    style_images = [f for f in os.listdir(args.style_image_dir) if
                    f.endswith(('.png', '.jpg', '.jpeg'))]

    sampling_batch(args=args, pipe=pipe, content_images=content_images, style_images=style_images)


if __name__ == "__main__":
    """   
    nohup python batch_gen.py \
    --ckpt_dir="ckpt/" \
    --content_image_dir="data_examples/basic/LXGWWenKaiGB-Light/" \
    --style_image_dir="data_examples/test_style/cpp/" \
    --save_image_dir="outputs/cpp2/" \
    --device="cuda:0" \
    --algorithm_type="dpmsolver++" \
    --guidance_type="classifier-free" \
    --guidance_scale=7.5 \
    --num_inference_steps=20 \
    --method="multistep" &
    
    nohup python batch_gen.py \
    --ckpt_dir="ckpt/" \
    --content_image_dir="data_examples/basic/LXGWWenKaiGB-Light/" \
    --style_image_dir="data_examples/test_style/crh/" \
    --save_image_dir="outputs/crh2/" \
    --device="cuda:1" \
    --algorithm_type="dpmsolver++" \
    --guidance_type="classifier-free" \
    --guidance_scale=7.5 \
    --num_inference_steps=20 \
    --method="multistep" &
    
    nohup python batch_gen.py \
    --ckpt_dir="ckpt/" \
    --content_image_dir="data_examples/basic/LXGWWenKaiGB-Light/" \
    --style_image_dir="data_examples/test_style/fzfs/" \
    --save_image_dir="outputs/fzfs/" \
    --device="cuda:2" \
    --algorithm_type="dpmsolver++" \
    --guidance_type="classifier-free" \
    --guidance_scale=7.5 \
    --num_inference_steps=20 \
    --method="multistep" &
    
    nohup python batch_gen.py \
    --ckpt_dir="ckpt/" \
    --content_image_dir="data_examples/basic/LXGWWenKaiGB-Light/" \
    --style_image_dir="data_examples/test_style/FZZCHJW/" \
    --save_image_dir="outputs/FZZCHJW/" \
    --device="cuda:3" \
    --algorithm_type="dpmsolver++" \
    --guidance_type="classifier-free" \
    --guidance_scale=7.5 \
    --num_inference_steps=20 \
    --method="multistep" &
    
    algorithm_type: "dpmsolver" or "dpmsolver++".
    guidance_type: "uncond" or "classifier" or "classifier-free".
    guidance_scale: The scale for the guided sampling.
    method: 'singlestep' or 'multistep' or 'singlestep_fixed' or 'adaptive'.
    """
    args = arg_parse()
    pipe = load_fontdiffuer_pipeline(args=args)
    process_directory_batch(args, pipe)
