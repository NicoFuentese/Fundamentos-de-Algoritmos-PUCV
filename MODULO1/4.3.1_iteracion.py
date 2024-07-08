from PIL import Image

img = Image.open('images.py/C4.3.1.png')
img.show()

#resolucion
personas = int(input())

while personas <= 0:
    personas = int(input())
altura = 0
suma = 0

for i in range (1, personas + 1):
    altura = float(input())
    suma += altura

promedio = suma / personas
print(f"promedio de altura para el grupo = {promedio}")