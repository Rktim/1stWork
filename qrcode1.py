import qrcode


qr = qrcode.QRCode()
qr.add_data("HAHA!, APRIL FOOL")

qr.make(fit=True)

qr.make_image(fill_color="black", back_color="white").save("hi.png")
