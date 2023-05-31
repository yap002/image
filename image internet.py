import requests
import json

# Azure Face API endpoint and subscription key
endpoint = "https://<your-azure-endpoint>.cognitiveservices.azure.com/"
subscription_key = "<your-azure-subscription-key>"

# Local image path
image_path = "<path-to-your-image>"

# Internet image URL
internet_image_url = "<internet-image-url>"

# Detect faces in the selected image
def detect_faces(image_path):
    face_api_url = endpoint + "face/v1.0/detect"

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/octet-stream",
    }

    with open(image_path, "rb") as image_file:
        response = requests.post(face_api_url, headers=headers, data=image_file)

    faces = json.loads(response.text)
    return faces

# Compare faces from the selected image and an internet image
def compare_faces(image_path, internet_image_url):
    faces = detect_faces(image_path)
    if len(faces) < 1:
        print("No faces detected in the selected image.")
        return

    face_id = faces[0]["faceId"]

    face_api_url = endpoint + "face/v1.0/identify"

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json",
    }

    payload = {
        "faceIds": [face_id],
        "personGroupId": "internet_faces",  # You can create a person group for internet faces
        "maxNumOfCandidatesReturned": 1,
        "confidenceThreshold": 0.5,
    }

    response = requests.post(face_api_url, headers=headers, json=payload)
    results = json.loads(response.text)

    if len(results) < 1 or len(results[0]["candidates"]) < 1:
        print("No matching faces found in the internet image.")
        return

    candidate = results[0]["candidates"][0]
    print("Matching face found in the internet image:")
    print("Person ID:", candidate["personId"])
    print("Confidence:", candidate["confidence"])

# Call the compare_faces function with the selected image and internet image URL
compare_faces(image_path, internet_image_url)
