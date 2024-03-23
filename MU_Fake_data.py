def fakeusers():
    from faker import Faker
    import pandas as pd

    # Initialize Faker with default locale
    fake = Faker('it_IT')

    # Generating data for 30 records
    data = [{
        "uniqueID": fake.uuid4(),
        "progressiveID": fake.random_int(min=1, max=1000),  # "progressiveID": fake.random_int(min=1, max=100000, step=1),
        "username": fake.user_name(),
        "email": fake.email(),
        "name": fake.name(),
        "address": fake.address().replace('\n', ', '),
        "user_type": fake.random_element(elements=('Artist', 'Customer', 'Admin')),
        "password_hash": fake.sha256(),
        "creation_date": fake.date_between(start_date='-2y', end_date='today').isoformat()
    } for _ in range(200)]

    # Creating DataFrame without using append
    df = pd.DataFrame(data)

    print(df)
    export_csv = df.to_csv(r'fake_users.csv', index=None, header=True)

def grabimageas():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    import requests
    import os

    # Setup WebDriver (Make sure to have the WebDriver for your browser)
    driver = webdriver.Chrome('path/to/chromedriver')

    # Open Pinterest Page
    driver.get('https://www.pinterest.com/username/boardname')

    # Scroll to Load Images (Modify as needed)
    for i in range(10):  # Scrolls 10 times (adjust as necessary)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)  # Wait for page to load

    # Find All Images here
    images = driver.find_elements_by_tag_name('img')

    # Download Images from pc
    for idx, img in enumerate(images):
        try:
            url = img.get_attribute('src')
            response = requests.get(url)
            with open(os.path.join('download/path', f'image_{idx}.jpg'), 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(f"Error downloading image {idx}: {e}")

    driver.quit()



#fakeusers()
grabimageas()