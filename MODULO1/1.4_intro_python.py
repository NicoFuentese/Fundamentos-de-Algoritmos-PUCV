from PIL import Image

img = Image.open('images.py/C1.4.png')
img.show()

#resolucion
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

promedio = (nota1+nota2+nota3)/3

#salida
print(f"promedio de notas = {promedio}")
