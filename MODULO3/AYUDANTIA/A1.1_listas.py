from PIL import Image

img = Image.open("images.py/C3_A1.1.png")
img.show()

#resolucion
def mostrarLista (lista):
    largo = len(lista)
    for i in range (largo):
        print(lista[i], end = " ")

n = int(input())
lista = []
for i in range (1, n + 1):
    t = int(input())
    k = t + 273.15
    lista.append(k)
    
mostrarLista(lista)
