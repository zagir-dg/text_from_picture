import pytesseract
from PIL import Image
#enter your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = Image.open(r"img\images.jpg")

file_name = img.filename
file_name = file_name.split(".")[0].split('\\')[1]


custom_config = r'--oem 3 --psm 13'
# custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang="eng", config=custom_config)

with open(f'text\{file_name}.txt', 'w') as text_file:
    text_file.write(text)