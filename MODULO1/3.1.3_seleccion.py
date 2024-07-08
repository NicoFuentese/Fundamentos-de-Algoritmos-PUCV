from PIL import Image

img = Image.open('')
img.show('MODULO1/3.1.3_seleccion.py')

#resolucion
a = float(input())
b = float(input())
c = float(input())

promedio = round((a + b + c)/ 3, 2)

print(f"Promedio = {promedio}")
if promedio >= 4.0:
    print("Aprobaste la Asignatura")
else:
    print("Reprobaste la Asignatura")

