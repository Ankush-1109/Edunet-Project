import cv2
import os
import string

# Check if image exists
image_path = "mypic.jpg"
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

img = cv2.imread(image_path)  # Read the image

# Check if image is large enough to hold the message
msg = input("Enter secret message: ")
if img.shape[0] * img.shape[1] < len(msg):
    print("Error: Image too small to encode the message.")
    exit()

# Ask for passcode
password = input("Enter a passcode: ")

# Create a dictionary for encoding and decoding
valid_chars = string.ascii_letters + string.digits + string.punctuation + " "
d = {char: i for i, char in enumerate(valid_chars)}
c = {i: char for i, char in enumerate(valid_chars)}

m = 0
n = 0
z = 0

# XOR key for encryption
key = 123  # A simple key for XOR encryption

# Encode the message in the image
for i in range(len(msg)):
    encoded_value = d[msg[i]] ^ key  # XOR encryption
    img[n, m, z] = encoded_value
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encoded image
quality = int(input("Enter quality (1-100): "))
cv2.imwrite("encryptedImage.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
os.system("start encryptedImage.jpg")  # Open image on Windows
