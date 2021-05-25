import os
from PIL import Image

directory = r'E:\PROJECTS\ScreenShotts\shots\2021-05-25'
from fpdf import FPDF

pdf = FPDF('P','in','A4')
# pdf = FPDF()


def pixel_to_inch(px):
    factor = 0.0104166667
    return round(px * factor, 1)


for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(directory + "\\" + filename)
        img = Image.open(directory + "\\" + filename)
        width = img.width
        height = img.height
        print("width={} height={}".format(pixel_to_inch(width)
                                          , pixel_to_inch(height)))
        width = pixel_to_inch(width)
        height = pixel_to_inch(height)
        pdf.add_page()
        pdf.image(directory + "\\" + filename, 0, 0, width-2, height-2)


    else:
        continue
pdf.output("yourfile.pdf", "F")


# def demo_fun():
#     path = r'E:\Machine Learning A TO Z hands on python and R\PROJECTS\ScreenShotts\shots\2021-05-17\10_21_20.png'
#     pdf.add_page()
#     img = Image.open(path)
#     width = img.width
#     height = img.height
#     pdf.image(path, 0, 0, pixel_to_inch(width)-2, pixel_to_inch(height))
#     pdf.output("yourfile.pdf", "F")

