import qrcode
import image

qr = qrcode.QRCode(
    version = 15 ,
    box_size= 5, #size of box
    border = 5 #white part of image
)

data = "https://github.com/ShivaBollam07"

qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill = "balck" , back_color = "white")
image.save("Qrcode.png")


#To get Output
#Run python file in terminal
