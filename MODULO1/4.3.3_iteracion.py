from PIL import Image

img = Image.open('images.py/C4.3.3.png')
img.show()

#resolucion
suma = 0
contador = 0
contador_mas_2m = 0

while True:
    altura = float(input())
    if (altura <= 0):
        break
    else:
        suma += altura
        contador += 1
    if (altura >= 2):
        contador_mas_2m += 1
    else:
        contador_mas_2m = contador_mas_2m

promedio = suma / contador
print(f"promedio de altura para el grupo = {promedio}")

if (contador_mas_2m > 0):
    print(f"Al menos una persona mide 2mt o más")