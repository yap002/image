import datetime
import os
import requests
from google_images_search import GoogleImagesSearch

# Set up the Google Images Search API
GCS_DEVELOPER_KEY = "YOUR_API_KEY"
GCS_CX = "YOUR_CX"
gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)

# Set the desired search query
search_query = "landscape"  # Modify this to your desired search query

# Define the target directory to save the downloaded images
target_directory = "image_directory"  # Modify this to your desired target directory

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Get the current day of the week (0 = Monday, 6 = Sunday)
current_day = datetime.datetime.now().weekday()

# Check if it's Sunday (day 6) to perform the image search
if current_day == 6:
    # Perform the image search
    gis.search(search_params=GoogleImagesSearch.construct_search_params(
        q=search_query,  # search query
        num=10,  # number of images to grab
        safe_search=True,  # enable safe search filter
        file_type='jpg',  # filter images by file type (optional)
    ))

    # Download and save the images
    for image in gis.results():
        url = image.url
        image_name = image.image_name
        file_path = os.path.join(target_directory, image_name)

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Image '{image_name}' downloaded successfully.")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download image '{image_name}'. Error: {str(e)}")

    print("Image download completed.")

else:
    print("Today is not Sunday. Skipping image download.")
