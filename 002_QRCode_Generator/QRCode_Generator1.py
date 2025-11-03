import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://www.langchain.com/")
qr.make(fit=True)
img = qr.make_image(fill_color = "red",
                    back_color = "black")
img.save("C:/Sneh[WorkDirectory]/Learning_Project/Python_Project/002_QRCode_Generator/langchain_1.png")