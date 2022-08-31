from PIL import Image
from pdf2image import convert_from_path

pdf_dir = 'text1.pdf'
page_num = 20

#CROP PARAMETERS
TOP = 120
BOTTOM = 200
LEFT = 50
RIGHT = 30

# Store Pdf with convert_from_path function
images = convert_from_path(pdf_dir)

images[page_num].save('noncropped.png', 'PNG')
im = images[page_num]

img_width, img_height = im.size
im_crop = im.crop((LEFT, TOP, img_width-RIGHT, img_height - BOTTOM))
im_crop.save('cropped.png', quality=95)