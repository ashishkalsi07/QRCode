import qrcode
myqr = qrcode.make("https://www.linkedin.com/in/ashishkalsi07/")  # you can paste any link here . A png image will appear here after running code in terminal which is your QR code 
myqr.save("mqr.png")
