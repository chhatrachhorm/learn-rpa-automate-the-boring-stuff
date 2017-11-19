from PIL import ImageFont, Image, ImageDraw
import os
# text(xy, text, fill, font)
# xy => two-int tuple to specify upper-let corner of the box
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

draw.text((20, 150), 'Hello', fill='purple')

# getting fonts folder
# vary based on os
# On Windows: C:\Windows\Fonts
# On OS X: /Library/Fonts and /System/Library/Fonts
# On Linux: /usr/share/fonts/truetype

# fontsFolder = 'C:\Windows\Fonts'
# or download .ttf file and paste to a folder
fontsFolder = 'fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Times New Roman.ttf'), 32)
draw.text((100, 150), 'New FOnt', fill='gray', font=arialFont)
im.save('files/drawText.png')
