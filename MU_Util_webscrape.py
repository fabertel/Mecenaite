import winsound
from bs4 import BeautifulSoup
import requests
import csv
from requests.exceptions import RequestException
from tqdm import tqdm
import time

def extract_data(url):
    try:
        response = requests.get(url)         # Send a GET request to the URL
        response.raise_for_status()         # Raise an exception if the request was unsuccessful
    except RequestException as e:
        print(f"An error occurred when trying to get {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.select('html > body > div:nth-of-type(4) > div:nth-of-type(1) > div')
    texts = [element.text for element in elements]
    texts = [" | ".join(text.split()) for text in texts]
    text = " | ".join(texts)
    return text

filename = 'bolognachildrensbookfair24.csv'
url = 'https://www.bolognachildrensbookfair.com/nqcontent.cfm?a_id=10793&illustrator='


def savedataintextfile(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')

def savedataintocsvfile(filename, data):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([suffix] + data.split(' | '))


# Iterate over the suffixes
for suffix in range(3000, 5000):
    # Construct the full URL
    full_url = url + str(suffix)
    savedataintocsvfile(filename,extract_data(full_url))  
    print(suffix)

print('Data has been saved into the file')

winsound.Beep(2500, 500)