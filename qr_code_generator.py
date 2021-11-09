#              ***   QR Code generator  ***



import qrcode
import image

qr = qrcode.QRCode(
  version= 15, #15 means the version of the qr code high the number the bigger the code image and complicated picture
  box_size= 10, #size of the box where qr code will be displayed
  border=5  #it is the white part of image -- border in all 4 sides with white color

)

data = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"

# as i have given the path of despacito song like the same way you can give anything
# if you don't want to redirect and create for normal text that write text in the quotes

qr.add_data(data)

qr.make(fit=True)

img= qr.make_image(fill="black",black_color = "white")

img.save("test.png")

