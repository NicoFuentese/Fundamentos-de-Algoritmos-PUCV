from PIL import Image

img = Image.open('images.py/C4.2.2.png')
img.show()

#resolucion
estudiantes = int(input())

#contador
aprobados = 0
reprobados = 0

for control in range (1, estudiantes + 1):
    notafinal = float(input())
    if notafinal >= 4:
        aprobados += 1
    else:
        reprobados += 1
        
porcAprobados = aprobados / estudiantes * 100
porcReprobados = reprobados / estudiantes * 100
print(f"porcentaje de aprobados = {porcAprobados} %")
print(f"porcentaje de reprobados = {porcReprobados} %")