from PIL import Image

img = Image.open('images.py/C2.2.3.png')
img.show()

#resolucion
from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2= float(input())

distancia =round(sqrt(pow((x2-x1),2) + pow((y1-y2),2)),1)
print(f"La distancia total es de {distancia}")
