from PIL import ImageColor
from PIL import Image


# color
print(ImageColor.getcolor('red', 'RGBA'))

# image pixel are addressed in (x, y) follow javascript approach
# top-left(0, 0)
catIm = Image.open('files/zophie.png')
print(catIm.size)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
# catIm.save('files/new.png')

# crop image
# crop() will not modify its img object
# it returns a new image obj
croppedIm = catIm.crop((355, 125, 526, 526))
# save new image
croppedIm.save('files/newCropCat.png')

# to copy image
copyCat = catIm.copy()
# paste another image
# nota bene: paste() will modify its image object
# make sure to copy the original one image's object for backup
faceIm = copyCat.crop((335, 345, 565, 560))
copyCat.paste(faceIm, (2, 2))
copyCat.paste(faceIm, (255, 352))
copyCat.save('files/pasted.png')


# griding image
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
anotherCopy = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        anotherCopy.paste(faceIm, (left, top))
anotherCopy.save('files/griding.png')

# resize image
# resize will not modify its image object
# it returns a new image obj
quarterSizedIm = catIm.resize((
    int(catImWidth/2),
    int(catImHeight/2)
))
quarterSizedIm.save('files/quarterImg.png')

svelteIm = catIm.resize((catImWidth, catImHeight + 250))
svelteIm.save('files/svelte.png')

# rotate/flipping img
# return a new image obj
catIm.rotate(90).save('files/rotated.png')
# to expand
catIm.rotate(6, expand=True).save('files/rotated_expand.png')
# mirror flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('files/horizontalFlip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('files/verticalFlip.png')

