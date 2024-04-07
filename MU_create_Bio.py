from openai import OpenAI
import os 
import pandas as pd

def create_bio(text):
    client = OpenAI()
    api_key = os.environ.get('OPENAI_API_KEY')


    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are an art expert and amazing writer."},
            {"role": "user", "content": f"write a 30-word biography highlighting the artist’s distinctive style, using the description of these operas :\n\n{text}"}
        ]
    )
    print(response.choices[0].message.content)



def load_xls_to_dataframe(file_path):
    # Try to load the Excel file
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        df['merge'] = df['content'] + df['technique'] + df['colors']
        first_five_values = df['merge'].head(5)
        first_five_values_string = ' '.join(first_five_values.astype(str))

        return first_five_values_string
    except Exception as e:
        # If an exception occurred, print it out
        print(f"An error occurred: {e}")
        return None


first5 = load_xls_to_dataframe('_Data/Scanned_images_database.xlsx')

create_bio(first5)