from PIL import Image

img = Image.open('')
img.show('images.py/C3.1.6.png')

#resolucion
a = float(input())

if a > 0:
    print(f"El número {a} es positivo")
elif a < 0:
    print(f"El número {a} es negativo")
else:
    print(f"El número {a} es igual a cero")