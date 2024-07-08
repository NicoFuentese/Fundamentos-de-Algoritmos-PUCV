from PIL import Image

img = Image.open('images.py/C3.3.1.png')
img.show()

#resolucion
precio = int(input())
cantidad = int(input())
precio_final = cantidad * precio


if cantidad >= 10:
    precio = precio * 0.9
    precio_final = int(cantidad * precio)
    print(f"Precio final = $ {precio_final}")
else:
    print(f"Precio final = $ {precio_final}")