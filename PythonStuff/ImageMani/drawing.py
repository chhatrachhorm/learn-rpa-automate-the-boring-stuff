from PIL import Image, ImageDraw

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# line(xy, fill, width)
# xy = [(x, y), (x, y), ...] - represent the connecting points
# e.g. 4 close lines : [(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)]
# line 1: (0, 0), (199, 0)
# line 2: (199, 0), (199, 199)
# line 3: (199, 199), (0, 199)
# line 4: (0, 199), (0, 0)
draw.line(
    [(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)],
    fill='red'
)

# rectangle (xy, fill, outline)
# xy = (left, top, right, bottom)
# left and top values specify the x- and y-coordinates of the upper-left corner of the rectangle
# right and bottom specify the lower-right corner
# e.g. ABCD or a rectangle (20, 30, 60, 52)
# => A(20, 30)
# => D(60, 52)
draw.rectangle((20, 30, 60, 52), fill='blue')

# ellipse(xy, fill, outline)
# if width = right => circle
# xy if the dimension of the box that precisely contains the ellipse - like rectangle
# xy = (left, top, right, bottom)

draw.ellipse((102, 20, 160, 41), fill='green')

# polygon(xy, fill, outline)
# xy = [(x, y), (x, y), ...] - connecting points
# the last pair of xy will be connecting to the first pair
draw.polygon(
    [(57, 85), (15, 52), (125, 128), (103, 13)],
    fill='brown'
)

# random line
for i in range(100, 200, 10):
    draw.line(
        [(i, 0), (200, i-100)],
        fill='pink'
    )
im.save('files/awesomeDraw.png')

