from PIL import Image

img = Image.open("images.py/C2_10.1.png")
img.show()

#resolucion
def factorial (n):
    productoria = 1
    if n == 0:
        productoria = 1
    else:
        for i in range (1, n + 1):
            productoria *= i
    return productoria

def sumatoria (n):
    suma = 0
    for i in range (0, 31 - n):
        termino = (n + i) / factorial (i + 1)
        suma += termino
    return suma


#main
while True:
    n = int(input())
    if (1 < n <= 29):
        break

print(sumatoria(n))