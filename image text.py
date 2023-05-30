import requests
from bs4 import BeautifulSoup

def grab_image_and_introduction(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the image on the page (modify this according to the website structure)
        image_url = soup.find('img', class_='image-class')['src']
        image_name = image_url.split('/')[-1]

        # Download the image file
        with open(image_name, 'wb') as image_file:
            image_response = requests.get(image_url)
            image_file.write(image_response.content)

        # Find the brief introduction on the page (modify this according to the website structure)
        introduction = soup.find('p', class_='introduction-class').get_text()

        return image_name, introduction
    else:
        print(f"Failed to retrieve the URL. Error code: {response.status_code}")

    return None, None

# Example usage
url = 'https://www.example.com/image-and-introduction'
image_name, introduction = grab_image_and_introduction(url)

if image_name and introduction:
    print(f"Image Name: {image_name}")
    print(f"Brief Introduction: {introduction}")
