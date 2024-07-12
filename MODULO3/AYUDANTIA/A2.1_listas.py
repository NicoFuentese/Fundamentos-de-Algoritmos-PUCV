from PIL import Image

img = Image.open("images.py/C3_A2.1.png")
img.show()

#resolucion
def decreciente(lista):
    for i in range (len(lista) - 1):
        if lista[i] < lista[i + 1]:
            return False
    return True
    
#main
n = int(input())
lista = []
for i in range(0, n):
    dato = int(input())
    lista.append(dato)

print(f"Lista = {lista}")

if (decreciente(lista) == True):
    print("Lista SI esta en orden decreciente")
else:
    print("Lista NO esta en orden decreciente")
