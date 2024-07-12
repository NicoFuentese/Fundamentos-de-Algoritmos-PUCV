from PIL import Image

img = Image.open("images.py/C3_5.3.png")
img.show()

#resolucion
def leerValidar(n):
    lista = []
    for i in range (n):
        dato = int(input())
        lista.append(dato)
    return lista

def esSincronizada (lista):
    largo = len(lista)
    for i in range (largo - 1):
        if (lista[i] % lista[i + 1] != 0 and lista[i + 1] % lista[i] != 0):
            return False
    return True

#main
n = int(input())
lista = leerValidar(n)
print(f"Lista = {lista}")

if (esSincronizada(lista) == True):
    print("Lista SI esta sincronizada")
else:
    print("Lista NO esta sincronizada")