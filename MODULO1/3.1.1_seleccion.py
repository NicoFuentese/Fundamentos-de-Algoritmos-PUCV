from PIL import Image

img = Image.open('')
img.show('images.py/C3.1.1.png')

#resolucion
Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())

Promedio = round((Nota1 + Nota2 + Nota3) / 3, 2)

print(f"Promedio = {Promedio}")
if Promedio >= 6.0:
    print("Felicitaciones Aprobaste con Distinción")
print("Felices vacaciones !!")
