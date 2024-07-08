from PIL import Image

img = Image.open('images.py/C4.2.3.png')
img.show()

#resolucion
estudiantes = int(input())
suma_notas = 0 #acumulador de notas
for control in range(1, estudiantes+1):
    nota = float(input())
    suma_notas = suma_notas + nota

promedio = suma_notas / estudiantes
print(f"promedio general = {promedio}")