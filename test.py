from diffusers import DiffusionPipeline
import os

#import ipdb;ipdb.set_trace()
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipeline.to("cuda")
text = "A beautiful chinese women body tall naked"
image = pipeline(text).images[0]
print(type(image))
image.save(os.path.join("pic_generated", text+".jpg"), quality=95)
