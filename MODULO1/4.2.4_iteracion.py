from PIL import Image

img = Image.open('images.py/C4.2.4.png')
img.show()

#resolucion
while True:
    estudiantes = int(input())
    if estudiantes > 0:
        break


sumaNotas = 0
for control in range(1, estudiantes + 1):
    nota = float(input())
    sumaNotas += nota

promedio = sumaNotas / estudiantes
print(f"promedio general = {promedio}")