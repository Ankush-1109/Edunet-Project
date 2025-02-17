import cv2
import os
import string

# Check if encoded image exists
image_path = "encryptedImage.jpg"
if not os.path.exists(image_path):
    print("Error: Encoded image file not found!")
    exit()

img = cv2.imread(image_path)  # Read the encoded image

# Create a dictionary for encoding and decoding
valid_chars = string.ascii_letters + string.digits + string.punctuation + " "
d = {char: i for i, char in enumerate(valid_chars)}
c = {i: char for i, char in enumerate(valid_chars)}

m = 0
n = 0
z = 0

# XOR key for decryption (same key as used in encoding)
key = 159  # The key used in encoding

# Ask for passcode to decrypt
password = input("Enter passcode for Decryption: ")

# Validate passcode
if password == "your_passcode_here":  # Replace this with the passcode you set in the encoding script
    message = ""

    # Decode the message from the image
    for i in range(len(message)):
        decoded_value = img[n, m, z] ^ key  # XOR decryption
        message += c[decoded_value]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
