from os import listdir
from fpdf import FPDF
from sys import argv


if len(argv) < 2:
    exit("usage: python imagetopdf.py <path>")

path = argv[1]

image_list = listdir(path)

image_list.sort()

pdf = FPDF('P', 'mm', 'A4')

x = 0
y = 0
w = 210
h = 270

for image in image_list:
    pdf.add_page()
    pdf.image(path+image, x, y, w, h)

pdf.output("imagetopdf.pdf", "F")


