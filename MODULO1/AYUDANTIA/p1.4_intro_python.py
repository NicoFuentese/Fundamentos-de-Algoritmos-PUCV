from PIL import Image

img = Image.open('images.py/p1.4.png')
img.show()

#resolucion
import math

a = float(input())
b = float(input())

c = math.sqrt(pow(a,2) + pow(b,2))

print(round(c,1))