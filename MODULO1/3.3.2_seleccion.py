from PIL import Image

img = Image.open('images.py/C3.3.2.png')
img.show()

#resolucion
n = int(input())

jabas = int(n / 12)

if n % 12 == 0:
    print(f"Cantidad de jabas = {jabas}")
    print(f"todas las bebidas fueron trasladadas")
else:
    print(f"Cantidad de jabas = {jabas}")
    print(f"quedan {n%12} sin trasladar")

