from pytesseract import pytesseract
from PIL import Image
import time
import config

pytesseract.tesseract_cmd = config.tesseract_cmd

tentativa = 0

while True:
    image = Image.open("data/"+config.imagem)
    result = pytesseract.image_to_string(image)
    print('tentativa {}'.format(tentativa))
    print('captcha -> {}'.format(result))
    print('----------------------------')
    tentativa += 1
    time.sleep(1)
