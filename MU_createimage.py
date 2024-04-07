
import os
import base64
import requests
from PIL import Image
from io import BytesIO
from openai import OpenAI
from openpyxl import load_workbook
import datetime
import pandas as pd

# DALL·E 3	Standard	1024×1024	$0.040 / image

api_key = os.environ.get('OPENAI_API_KEY')
backup_file = ("_Data/Scanned_images_database.xlsx")
IMG_path = "_ART"

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

# Assuming the response contains a URL to the generated image
image_url = response.data[0].url

# Download the image
image_response = requests.get(image_url)
image = Image.open(BytesIO(image_response.content))

# Prepare the filename based on the first 20 characters of the prompt (excluding spaces)
prompt = "a white siamese cat"
filename = prompt.replace(" ", "")[:20] + ".jpg"

# Save the image
image.save(filename, "JPEG")

print(f"Image saved as {filename}")