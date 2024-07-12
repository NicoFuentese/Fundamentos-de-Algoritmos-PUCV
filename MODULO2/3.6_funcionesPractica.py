from PIL import Image

img = Image.open("images.py/C2_3.6.png")
img.show()

#resolucion
from math import factorial

def taylorCos (x, n):
    sumatoria = 0
    for i in range ( 0, n + 1):
        termino = ((-1) ** i) * ( x ** (2 * i) / factorial(2 * i) )
        sumatoria += termino
        
    return sumatoria