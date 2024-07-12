from PIL import Image

img = Image.open("images.py/C2_3.3.png")
img.show()

#resolucion
from math import pi

def calculaPeriodo (w):
    p = (2 * pi) / w
    return p