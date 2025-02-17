# Secure Data Hiding in Images Using Steganography

## Overview
This project demonstrates **steganography** combined with **XOR encryption** to securely hide secret messages inside images without noticeable distortion. The system ensures confidentiality by encoding and decoding messages using a passcode.

## Features
✅ **Steganography + Encryption** – Double-layer security using XOR encryption.  
✅ **Passcode Protection** – Only authorized users can decrypt messages.  
✅ **Minimal Distortion** – Image quality remains intact.  
✅ **Lightweight & Fast** – Efficient processing with OpenCV.  

## Technology Stack
- **Language:** Python
- **Libraries Used:**
  - OpenCV (`cv2`) – Image processing
  - OS – File handling
  - String – Encoding characters

## Installation Guide
### Prerequisites:
Ensure you have **Python 3+** installed. If not, download it from [Python's official website](https://www.python.org/downloads/).

### Steps to Run the Project:
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/secure-steganography.git
   cd secure-steganography
   ```
2. **Install dependencies:**
   ```bash
   pip install opencv-python
   ```
3. **Run the script:**
   ```bash
   python steganography.py
   ```
4. **Follow the on-screen instructions:**
   - Enter the secret message.
   - Set a passcode for encryption.
   - Enter the desired image quality.
   - An encrypted image (`encryptedImage.jpg`) will be generated.
   - Enter the correct passcode to retrieve the hidden message.

## Usage Instructions
### Encoding a Message:
1. Select an image (e.g., `mypic.jpg`).
2. Input the secret message.
3. Choose an encryption passcode.
4. The script modifies the image to store the message securely.

### Decoding a Message:
1. Enter the correct passcode.
2. The script retrieves and displays the hidden message.

## Example Output

### **Encrypted Message (Console Output):**
```bash
Encrypted message: Hello, this is a secret!
Enter passcode for encryption: *****
```

### **Original Image:**
*(Before encoding)*

### **Encrypted Image:**
*(Message hidden inside this image)*

### **Decrypted Message (Console Output):**
```bash
Enter passcode for decryption: *****
Decrypted message: Hello, this is a secret!
```

## Future Enhancements
🚀 **Support for stronger encryption** (AES, RSA).  
📂 **Add support for multiple image formats** (PNG, BMP).  
💻 **Develop a user-friendly GUI** for non-technical users.  
🖼️ **Improve data capacity** to store longer messages.  

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. **Fork the repository.**
2. **Create a new branch** (`feature-xyz`).
3. **Commit your changes and push.**
4. **Open a pull request** for review.

---
💡 *Feel free to give a ⭐ if you like this project!*

