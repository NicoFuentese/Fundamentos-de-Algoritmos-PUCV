from PIL import Image

img = Image.open("images.py/C3_A2.2.png")
img.show()

#resolucion
from math import sqrt

#main
n = int(input())
listaEdad = []
for i in range(0, n):
    edad = int(input())
    listaEdad.append(edad)
print(f"Lista de Edades = {listaEdad}")

prom = round(sum(listaEdad) / len(listaEdad), 1)
print(f"Promedio de Edades = {prom}")

suma = 0
for i in listaEdad:
    suma += (i - prom) ** 2
sd = round(sqrt(suma / (len(listaEdad) - 1)), 4)
    

print(f"Desviación Estándar de la muestra = {sd}")