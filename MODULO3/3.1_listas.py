from PIL import Image

img = Image.open("images.py/C3_3.1.png")
img.show()

#resolucion
def divisible (lista):
    for i in lista:
        contador = 0
        for j in lista:
            if (j % i == 0):
                contador += 1
            if (contador == len(lista)):
                return True
    return False

def NumeroDiv (lista):
    for i in lista:
        contador = 0
        for j in lista:
            if (j % i == 0):
                contador += 1
            if (contador == len(lista)):
                return i

#main
n = int(input())
lista = []
for i in range(n):
    dato = int(input())
    lista.append(dato)
    
print(f"Lista de números leídos = {lista}")

numeroDivisible = NumeroDiv(lista)

if (divisible(lista) == True):
    numeroDiv = NumeroDiv(lista)
    print(f"Sofía el número {numeroDiv} es divisor de todos los números en la lista.")
else:
    print("Sofía NO existe un número en la lista que los divida a todos.")