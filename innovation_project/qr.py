import qrcode

# Data you want to encode
data = "https://archaelogistic.base44.app/"

# Generate the QR code
img = qrcode.make(data)

# Save the image file
img.save("fll.png")

