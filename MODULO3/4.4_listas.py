from PIL import Image

img = Image.open("images.py/C3_4.4.png")
img.show()

#resolucion
from math import ceil

def leerEdades():
    lista = []
    while True:
        dato = int(input())
        if (dato < 0):
            break
        lista.append(dato)
    return lista

def mediana (lista):
    largo = len(lista)
    if (largo % 2 != 0):
        med = lista[largo // 2]
    else:
        med = (lista[largo // 2 - 1] + lista[largo // 2]) / 2
    return med
#main
lista = leerEdades()
listaOrd = sorted(lista)
largo = len(lista)
print(f"Lista Original = {lista}")
print(f"Lista Ordenada = {listaOrd}")
print(f"Largo de Lista = {largo}")
med = mediana(listaOrd)
print(f"La mediana de edades es = {round(med, 1)}")