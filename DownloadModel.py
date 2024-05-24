from diffusers import DiffusionPipeline

# Download the model to the specified directory
pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
