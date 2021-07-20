import qrcode



id = "1ee7c3b6-4dfb-41e9-9e32-ef38fce0083e"
print(id)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(id)
qr.make(True)
img = qr.make_image(fill_color = "black", back_color = "white")

img.save("qr.jpg")