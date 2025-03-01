# Step 1: Install required libraries
!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install pillow

# Step 2: Import libraries
from PIL import Image
import pytesseract
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image_path="/content/sample.png"
# Load the image
image = cv2.imread(image_path)

# Display the image
print("Uploaded Image:")
cv2_imshow(image)

# Continue with OCR
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
extracted_text = pytesseract.image_to_string(gray_image)
print("\nExtracted Text:")
print(extracted_text)

import requests
from PIL import Image
from io import BytesIO

# URL of the image
image_url = "/content/sample.png"

# Download the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Convert to OpenCV format (if needed)
image = np.array(image)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Display the image
print("Uploaded Image:")
cv2_imshow(image)

# Continue with OCR
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
extracted_text = pytesseract.image_to_string(gray_image)
print("\nExtracted Text:")
print(extracted_text)
