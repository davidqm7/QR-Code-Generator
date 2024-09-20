import qrcode

# Data to encode
data = "https://www.example.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction
    box_size=10,  # size of each box (pixel)
    border=4,  # thickness of the border
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")
