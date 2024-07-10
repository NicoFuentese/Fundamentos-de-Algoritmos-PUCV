from PIL import Image

img = Image.ope('images.py/p5.6.png')
img.show()

#resolucion
from math import factorial

n = int(input())

if (n == 0):
    print("0 no es factorial exacto")
elif (n == 1):
    print("1 es factorial exacto de 1 y 0")
elif (n > 1):
    for i in range (2, n + 1):
        productoria = factorial(i)
        if (productoria == n):
            print(f"{n} es factorial exacto de {i}")
            break
        elif (productoria > n):
            print(f"{n} no es factorial exacto")
            break