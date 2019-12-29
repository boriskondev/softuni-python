from cImage import *
import random

# works only for gif images

image_width = int(input("Image width: "))
image_height = int(input("Image height: "))

image_object = EmptyImage(image_width, image_height)
rgb_range = range(0, 256)

scope = image_object.getHeight()


for column in range(image_object.getWidth()):
    x = random.randint(0, scope - 10)
    for row in range(image_object.getHeight()):
        if row > x:
            break
        else:
            new_red = 0
            new_green = random.choice(rgb_range)
            new_blue = 0
            new_pixel = Pixel(new_red, new_green, new_blue)
            image_object.setPixel(column, row, new_pixel)

image_object.save(fname="matrix", ftype="gif")

