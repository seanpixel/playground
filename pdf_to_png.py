from pdf2image import convert_from_path

pdf_dir = 'photography_text.pdf'

# Store Pdf with convert_from_path function
images = convert_from_path(pdf_dir)
 
for i in range(len(images)):
      # Save pages as images in the pdf
    images[i].save('pabge'+ str(i) +'.png', 'PNG')