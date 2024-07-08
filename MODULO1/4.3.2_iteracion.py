from PIL import Image

img = Image.open('images.py/C4.3.2.png')
img.show()

#resolucion
suma = 0
contador = 0

while True:
    altura = float(input())
    if (altura <= 0):
        break
    else: 
        suma += altura
        contador += 1

if (contador == 0):
    print("No se ingresaron alturas")
else:
    promedio = suma / contador
    print(f"Promedio de altura para el grupo = {promedio}")
    