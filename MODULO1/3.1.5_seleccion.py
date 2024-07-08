from PIL import Image

img = Image.open('')
img.show('images.py/C3.1.5.png')

#resolucion
a = float(input())
b = float(input())
c = float(input())

promedio = round((a + b + c)/ 3, 2)

print(f"Promedio = {promedio}")
if promedio < 3.0:
    print("Reprobaste la asignatura")
elif promedio >= 6.5:
    print("Aprobaste la asignatura")
else:
    print("Debes rendir examen final en esta asignatura")
    