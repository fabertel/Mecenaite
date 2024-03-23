# img2text working 2024/03/13 
# DOCS https://platform.openai.com/docs/guides/vision
# COST : INPUT $0.01 / 1K tokens | OUTPUT $0.03 / 1K tokens |


import os
import base64
import requests
import openai
from openai import OpenAI
import json
from openpyxl import load_workbook
import datetime
import pandas as pd


api_key = os.environ.get('OPENAI_API_KEY')
backup_file = ("_Data/Scanned_images_database.xlsx")
IMG_path = "_ART"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def readimage(image_path):
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {"role": "system", "content": "You are an art lover."},
            {"role": "user", "content": [
                {"type": "text", "text": "analyze this image and describe ,be syntetic, seaprately CONTENTS TECHNIQUE and COLORS. separate answers with apipe character | "},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]}
        ],
        "max_tokens": 400
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return(response)

def compute_cost(response, prompt_token_price=0.01, completion_token_price=0.03):
    prompt_tokens = (response.json().get('usage').get('prompt_tokens'))
    completion_tokens = (response.json().get('usage').get('completion_tokens'))
    cost = (prompt_tokens / 1000) * prompt_token_price + (completion_tokens / 1000) * completion_token_price
    return (cost)

def add_to_database(file_path,response,backup_file):
    # cut answer in 3 parts using | as separator and print them
    answer = response.json().get('choices')[0].get('message').get('content')
    parts = answer.split("|")

    # Check the length of parts and append None if necessary
    while len(parts) < 3:
        parts.append(None)

    answer_dict = {}
    answer_dict['scan_timestamp'] = datetime.datetime.now().isoformat()
    answer_dict['cost'] = compute_cost(response)
    answer_dict['scan_file'] = file_path
    answer_dict['content'] = parts[0]
    answer_dict['technique'] = parts[1]
    answer_dict['colors'] = parts[2]

    # SAVE TO XLS
    if os.path.isfile(backup_file):
        df_existing = pd.read_excel(backup_file)
    df_new = pd.DataFrame([answer_dict])
    df = pd.concat([df_existing, df_new], ignore_index=True)
    with pd.ExcelWriter(backup_file, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False)


# Iterate over all files in the directory
for filename in os.listdir(IMG_path):
    # Construct the full file path
    file_path = os.path.join(IMG_path, filename)
    
    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):

        # Apply the functions to the file
        print(file_path)
        response = readimage(file_path)
        add_to_database(file_path,response, backup_file)
        #move processed file to _DONE folder
        os.rename(file_path, os.path.join("_ART\SCANNED", filename))

print("completed") 
