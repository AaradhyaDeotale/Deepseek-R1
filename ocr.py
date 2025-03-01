import requests
import json
from google.colab import files

from PIL import Image
from IPython.display import display

image_path = "/content/sample.png"

image = Image.open(image_path)
display(image)

# 🔑 Your OCR.Space API Key (Replace with your actual API key)
API_KEY = "f8cdd9f95288957"

# 🚀 OCR.Space API Endpoint
url = "https://api.ocr.space/parse/image"

with open(image_path, "rb") as image_file:
    response = requests.post(
        url,
        files={"image": image_file},
        data={"apikey": API_KEY, "language": "eng", "isOverlayRequired": False}
    )

# 📜 Parse the JSON response
result = response.json()
extracted_text = result["ParsedResults"][0]["ParsedText"] if "ParsedResults" in result else "No text found"

# 🖨 Print the extracted text
print("📝 Extracted Text:\n", extracted_text)
