import requests
from bs4 import BeautifulSoup

# Placeholder list to store suffixes after "country" in links
suffixes_after_country = []

for url in webpages:
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all hyperlinks in the webpage
        links = soup.find_all('a')
        # Filter links containing the word "country" and extract the suffix
        for link in links:
            href = link.get('href')
            if href and 'country' in href:
                # Extract part of the URL after "country"
                parts = href.split('country')
                if len(parts) > 1:
                    # Save the suffix, which is after "country"
                    suffixes_after_country.append(parts[1])
    except Exception as e:
        print(f"Error fetching or parsing {url}: {e}")


cleaned_suffixes = [suffix.replace('+', '') for suffix in suffixes_after_country if '.html' not in suffix]
final = [suffix.replace('=', '') for suffix in cleaned_suffixes]
print(final)
    

    
