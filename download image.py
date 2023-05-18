import time
import webbrowser
import requests
import os
import random
from bs4 import BeautifulSoup

# Countdown for 1 minute
for i in range(1, 61):
    print(f"{i} seconds passed")
    time.sleep(1)

# Open web browser and search for supercar images
webbrowser.open("https://www.google.com/search?q=supercar&source=lnms&tbm=isch")

# Get the HTML content of the search page
response = requests.get("https://www.google.com/search?q=supercar&source=lnms&tbm=isch")
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image URLs on the page
img_tags = soup.find_all('img')

# Create a folder to save the downloaded images
if not os.path.exists("supercar_images"):
    os.makedirs("supercar_images")

# Download 20 random images
for i in range(20):
    # Select a random image URL from the list
    img_url = random.choice(img_tags)['src']
    # Send a request to the image URL to get the image content
    img_response = requests.get(img_url)
    # Save the image content to a file in the folder
    with open(f"supercar_images/image_{i}.jpg", "wb") as f:
        f.write(img_response.content)
