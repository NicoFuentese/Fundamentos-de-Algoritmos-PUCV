from PIL import Image

img = Image.open("images.py/C3_A2.4.png")
img.show()

#resolucion
def espaldaCamello(lista):
    contador = 0
    for i in range (1, len(lista) - 1):
        if ((lista[i] < lista[i - 1] and lista[i] < lista[i + 1]) or
            (lista[i] > lista[i - 1] and lista[i] > lista[i + 1])):
                contador += 1
    if (contador == len(lista) - 2):
        return True
    return False
        
#main
n = int(input())
lista = []
for i in range (n):
    dato = int(input())
    lista.append(dato)

print(f"Lista = {lista}")
if (espaldaCamello(lista) == True):
    print("La lista SI es espalda de camello")
else:
    print("La lista NO es espalda de camello")