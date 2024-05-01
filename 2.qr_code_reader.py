import qrcode
import cv2  # pip install opencv-python
import webbrowser

# Encode QR code
make_qr = qrcode.make('9c9c1f134cf4')
make_qr.save('id.png')

# Decode QR code
qr = cv2.imread("code.png")
read_qr = cv2.QRCodeDetector().detectAndDecode(qr)
print(read_qr[0])

# Open link
#webbrowser.open(read_qr[0])
