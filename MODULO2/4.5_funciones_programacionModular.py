from PIL import Image

img = Image.open("images.py/C2_4.5.png")
img.show()

#resolucion
def sumaDivisores (numero):
    suma = 0
    for i in range (1, numero):
        if (numero % i == 0):
            suma += i
    return suma

def esAbundante (numero):
    if (sumaDivisores(numero) > numero):
        return True
    else:
        return False
    
def mostrarAbundantes (a, b):
    print(f"Números Abundantes en [ {a} .. {b} ] = ", end = "")
    contador = 0
    for i in range (a, b + 1):
        if (esAbundante(i) == True):
            print(f"{i} ", end = "")
            contador += 1
    if (contador == 0):
        print("NO HAY")

#main
a = int(input())
b = int(input())
mostrarAbundantes(a, b)