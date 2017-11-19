#! python3
# code to
# scale image down proportionally if wider|taller than 300 pixel
# add logo to the corner

from PIL import Image
import os

os.chdir('files/daisy')

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo = Image.open('../' + LOGO_FILENAME)
logo = logo.resize((50, 50))
logoWidth, logoHeight = logo.size

os.makedirs('withLogo', exist_ok=True)
for file in os.listdir('.'):
    if not (
                file.endswith('.png') or
                file.endswith('.jpg') or
                file == LOGO_FILENAME
    ):
        continue
    im = Image.open(file)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing: ', file)
        im = im.resize((width, height))
    print('Adding logo to:', file)
    # 'cause the logo is transparent
    # paste(logo-transparent, position, logo-actual)
    im.paste(logo, (width - logoWidth, height - logoHeight), logo)
    im.save(os.path.join('withLogo', file))
