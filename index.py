import re
import openai
import os
import PyPDF2 
from PIL import Image
from pytesseract import pytesseract
from pdf2image import convert_from_path

openai.api_key = "APIKEY"

gpt_prompt_stem = "Summarize this paragraph:\n\n"

#get pdf and convert them to images
pdf_dir = 'text1.pdf'
images = convert_from_path(pdf_dir)

#CROP PARAMETERS
TOP = 120
BOTTOM = 200
LEFT = 50
RIGHT = 30


#START AND END
start_page = 12
end_page = 14

def get_summary(paragraph):
    gpt_prompt = gpt_prompt_stem + paragraph

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    return response['choices'][0]['text']



def extract_text(page_num):
    #get image from pdf page
    img = images[page_num]
    #Open image with PIL and crop to get rid of page #s
    img = crop_image(img)
    #Extract text from image
    text = pytesseract.image_to_string(img)
    return text


def get_page_num(pdf_dir):
    # creating a pdf file object 
    pdfFileObj = open(pdf_dir, 'rb') 
        
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # getting page number
    page_num = pdfReader.numPages
        
    # closing the pdf file object 
    pdfFileObj.close() 

    return page_num



def crop_image(im):
    img_width, img_height = im.size
    im_crop = im.crop((LEFT, TOP, img_width-RIGHT, img_height - BOTTOM))
    return im_crop

def get_paragraphs(start_page_num, end_page_num):
    paragraphs = []
    corpus = ''

    for page in range(start_page_num, end_page_num):
        corpus += extract_text(page)

    paragraphs = corpus.split('.\n')

    for par in paragraphs:
        par += '.'
        print(par)

    return paragraphs

def get_results(start_page_num, end_page_num):
    paragraphs = get_paragraphs(start_page_num, end_page_num)
    result = ''

    num = 0
    for par in paragraphs:
        num += 1
        result += "paragraph " + str(num) + '\n'
        result += get_summary(par) + "\n\n"

    with open('summary3.txt', 'w') as f:
        f.write(result)

get_results(start_page, end_page)
