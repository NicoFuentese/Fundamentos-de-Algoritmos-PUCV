from PIL import Image

img = Image.open("images.py/C4.6.4.png")
img.show()

#resolucion
from math import factorial

x = float(input())
n = int(input())

sumatoria = 0
for i in range (0, n + 1):
    termino = (-1)**i * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    sumatoria += termino

print(f"sen ( {x} ) = {sumatoria}")