from PIL import Image

img = Image.open('images.py/C4.1.5.png')
img.show()

#resolucion
a = int(input())
b = int(input())

print(f"Números enteros en el rango de {a} a {b} :")
for i in range(a, b+1):
    print(i, end = " ")