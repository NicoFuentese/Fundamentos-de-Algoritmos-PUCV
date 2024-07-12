from PIL import Image

img = Image.open("images.py/C3_5.2.png")
img.show()

#resolucion
def leerDatos (n):
    lista = []
    for i in range(n):
        dato = int(input())
        lista.append(dato)
    return lista
    
def esMC(lista):
    largo = len(lista)
    for i in range(1, largo):
        if lista[i] % lista[i - 1] != 0:
            return False
    return True

#main

n = int(input())
lista = leerDatos(n)
print("Lista =", lista)

if esMC(lista):
    print("Todos los elementos adyacentes de la lista SI son múltiplos consecutivos")
else:
    print("Todos los elementos adyacentes de la lista NO son múltiplos consecutivos")
    
