from PIL import Image

img = Image.open('images.py/C3.2.1.png')
img.show()

#resolucion
from math import sqrt

a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c


if a == 0:
    print("No es una ecuación de segundo grado")
elif d > 0:
    x1 = round((-b + sqrt(d)) / (2 * a),1)
    x2 = round((-b - sqrt(d)) / (2 * a),1)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif d == 0:
    x = round(-b / (2 * a),1)
    print(f"x = {x}")
else:
    print("La ecuación tiene raíces complejas")