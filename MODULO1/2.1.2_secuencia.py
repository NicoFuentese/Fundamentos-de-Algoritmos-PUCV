from PIL import Image

img = Image.ope('images.py/C2.2.png')
img.show()

#resolucion
hombre = int(input())
mujer = int(input())

total = hombre + mujer
pm = (mujer/total)*100
ph = (hombre/total)*100

print(f"Porcentaje de Niñas en el curso = {ph}%")
print(f"Porcentaje de Niños en el curso = {pm}%")