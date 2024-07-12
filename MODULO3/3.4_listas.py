from PIL import Image

img = Image.open("images.py/C3_3.4.png")
img.show()

#resolucion
#main
n = int(input())
lista = []
for i in range(n):
    altura = int(input())
    lista.append(altura)
print(f"Lista Alturas = {lista}")

listaEW = list(reversed(lista))
masAlta = listaEW[0]
contador = 1
for i in range(len(listaEW) - 1):
    if (listaEW[i] < listaEW[i + 1]) and (listaEW[i + 1] > masAlta):
        masAlta = listaEW[i + 1]
        contador += 1
print(f"Número máximo de abadías que se pueden construir en la cadena montañosa = {contador}")
    