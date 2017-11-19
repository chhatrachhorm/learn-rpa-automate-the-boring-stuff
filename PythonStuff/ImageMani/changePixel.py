from PIL import Image
from PIL import ImageColor

im = Image.new('RGBA', (100, 100))
# to get color from an individual pixel
print(im.getpixel((0, 0)))

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

print(im.getpixel((0, 0)))
im.save('files/putPixel.png')
