from PIL import Image

img = Image.open("images.py/C2_5.1.png")
img.show()

#resolucion
def sumaDivisores (numero):
    suma = 0
    for i in range (1, numero // 2 + 1):
        if (numero % i == 0):
            suma += i
    return suma

def sonAmigos (a, b):
    if (sumaDivisores(a) == b and sumaDivisores(b) == a):
        return True
    else:
        return False
        

#main



