from PIL import Image

img = Image.open("images.py/C3_A1.4.png")
img.show()

#resolucion
def mostrarLista (lista):
    print("Lista = [", end = "")
    for i in range (len(lista)):
        if (i != len(lista) - 1):
            print(lista[i], end = ", ")
        else:
            print(lista[i], end = "")
    print("]")

def esAlternada (lista):
    contador = 0
    for i in range (len(lista) - 1):
        if (lista[i] % 2 == 0):
            if (lista[i + 1] % 2 != 0):
                contador += 1
        else:
            if (lista[i + 1] % 2 == 0):
                contador += 1
                
    if (contador == len(lista) - 1):
        return True
    else:
        return False

#main
n = int(input())
lista = []
for i in range (1, n + 1):
    dato = int(input())
    lista.append(dato)
mostrarLista(lista)

if (esAlternada(lista) == True):
    print("La lista SI es alternada par-impar")
else:
    print("La lista NO es alternada par-impar")