import qrcode
import image


qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10, # size of the box where qr code will be displayed
    border = 4 # it is the white part of image -- border in all 4 sides with white color
)

data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"

# as i have give the path of the channel like the same way can give anyting

#if you dn't want ot redirect and create for nornal text that write ext in the quotes

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")
