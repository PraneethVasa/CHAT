import streamlit as st
import requests
from PIL import Image
import io
from diffusers import StableDiffusionPipeline
import torch

st.title("Dreamlike Image Generator")

model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Create an input text box for the prompt
prompt = st.text_input("Enter your prompt", "")

if st.button("Generate Image"):
    image = pipe(prompt).images[0]

    # Display the generated image
    st.image(image, caption="Generated Image")

    # Save the image to a BytesIO object
    image_io = io.BytesIO()
    image.save(image_io, format='PNG')

    # Send the image as a download link
    st.download_button("Download Image", data=image_io, file_name='generated_image.png')
