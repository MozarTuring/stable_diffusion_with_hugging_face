import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

pipe = StableDiffusionPipeline.from_pretrained("lambdalabs/sd-pokemon-diffusers", torch_dtype=torch.float16)
pipe = pipe.to("cuda")




"""shell_start_mjw
source /home/maojingwei/project/stable_diffusion_with_hugging_face/myRequirements.sh run
python /home/maojingwei/project/stable_diffusion_with_hugging_face/pokerman.py

shell_end_mjw"""
