from PIL import Image

img = Image.open('images.py/C3.5.6.png')
img.show()

#resolucion
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
suma = nota1 + nota2 + nota3
promedio = suma / 3
print("El promedio de notas es",round(promedio,1))
