import qrcode
link=input("Enter the Link or the Text ")
name=input("Enter the Name For Saving the file ")
name=name+".png"

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=50,border=2)
qr.add_data(link)
qr.make(fit=True)
img=qr.make_image()
img.save(name)
