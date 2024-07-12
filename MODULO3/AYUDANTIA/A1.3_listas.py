from PIL import Image

img = Image.open("images.py/C3_A1.3.png")
img.show()

#resolucion
def valorAbs (numero):
    if (numero < 0):
        numero *= -1
    elif (numero >= 0):
        numero = numero
    return numero

#main
n = int(input())
lista = []
for i in range(1, n + 1):
    dato = int(input())
    lista.append(dato)
print("Lista =", lista)

contador = 0
for i in range (len(lista)-2):
    d1 = valorAbs(lista[i] - lista[i + 1])
    d2 = valorAbs(lista[i + 1] - lista[i + 2])
    if (valorAbs(d1 - d2) == 0):
        contador += 1
    
if (contador == len(lista) - 2):
    print("Los elementos de la lista tienen una distancia constante")
else:
    print("Los elementos de la lista NO tienen una distancia constante")