import qrcode
import barcode
import cv2  # pip install opencv-python
import webbrowser

# Encode QR code
make_qr = qrcode.make('maxxi-abcde1-12345')
barcode = barcode.Code128('maxxi-abc123-12345')
make_qr.save('id.png')
barcode.save('bar_code.png')

# Decode QR code
qr = cv2.imread("code.png")
read_qr = cv2.QRCodeDetector().detectAndDecode(qr)
print(read_qr[0])

# Open link
#webbrowser.open(read_qr[0])
