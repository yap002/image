import requests
import os

# Google Images API endpoint
url = "https://www.googleapis.com/customsearch/v1"

# Your API key and search engine ID
api_key = "YOUR_API_KEY"
cx = "YOUR_SEARCH_ENGINE_ID"

# Directory to save the downloaded images
save_dir = "phone_images"

# Create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Parameters for the API request
params = {
    "key": api_key,
    "cx": cx,
    "q": "phone",
    "searchType": "image",
    "num": 100,
    "safe": "high"
}

# Send the API request
response = requests.get(url, params=params)
data = response.json()

# Process the response
for item in data.get("items", []):
    image_url = item.get("link")
    
    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        # Extract the image file name from the URL
        file_name = os.path.join(save_dir, os.path.basename(image_url))
        
        # Save the image file
        with open(file_name, "wb") as f:
            f.write(response.content)
        
        print(f"Downloaded: {file_name}")
