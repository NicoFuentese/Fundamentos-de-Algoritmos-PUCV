from PIL import Image

img = Image.open("images.py/C2_9.2.png")
img.show()

#resolucion
from math import pi

def calculaPeriodo (w):
    periodo = (2 * pi) / w
    return periodo
    