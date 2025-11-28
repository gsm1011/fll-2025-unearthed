from PIL import Image
from pyzbar.pyzbar import decode

# Open the image file
img = Image.open('./my_qrcode.png')

# Decode the QR code(s) in the image
decoded_objects = decode(img)

# Print the decoded data
if decoded_objects:
    for obj in decoded_objects:
        # The data is in bytes, decode it to a string
        qr_data = obj.data.decode('utf-8')
        print(f"Decoded Data: {qr_data}")
else:
    print("No QR code found or could not be decoded.")

