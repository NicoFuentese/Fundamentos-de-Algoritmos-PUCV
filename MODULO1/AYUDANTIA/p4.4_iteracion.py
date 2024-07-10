from PIL import Image

img = Image.open('images.py/p4.4.png')
img.show()

#resolucion
altura = int(input())
ancho = int(input())

for i in range(1, altura + 1):
    print("*" * ancho)