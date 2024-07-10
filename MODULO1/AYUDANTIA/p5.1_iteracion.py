from PIL import Image

img = Image.ope('images.py/p5.1.png')
img.show()

#resolucion
n = int(input())

for i in range (0, n + 1):
    termino = 5 ** i
    print(termino, end = " ")