import qrcode
import qrcode as qr
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border= 4,
                   )
print("Enter the link or text for which you want to create a QR-Code")
a = input()

qr.add_data(a)
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
print("Enter the name of your Qr-Code")
b = input()

img.save(b+".png")