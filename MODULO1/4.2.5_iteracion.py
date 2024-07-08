from PIL import Image

img = Image.open('images.py/C4.2.5.png')
img.show()

#resolucion
e = int(input())
suma = 0

while e <= 0:
    e = int(input())

for i in range(1, e + 1):
    while True:
        nota = float(input())
        if nota >= 1 and nota <= 7:
            break
    suma += nota
    
promedio = suma / e

print(f"promedio general = {promedio}")