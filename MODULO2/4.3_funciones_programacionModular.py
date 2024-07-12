from PIL import Image

img = Image.open("images.py/C2_4.3.png")
img.show()

#resolucion
def esPrimo (numero):
    if ( numero == 1):
        return False
    else:
        contador = 0
        for i in range (1, numero + 1):
            if (numero % i == 0):
                contador += 1
        if ( contador == 2):
            return True
        else:
            return False

def primosSexys (a, b):
    if ( esPrimo(a) == True and esPrimo(b) == True):
        if (b == a + 6):
            return True
        else:
            return False
    else:
        return False

def validar():
    while True:
        n = int(input())
        if (20 <= n <= 500):
            break
    return n

#main
numero = validar()
print(f"LOS PRIMOS SEXY MENORES A {numero} SON :")
for i in range (1, numero):
    for j in range (1, numero):
        if (primosSexys(i, j) == True):
            print(f"{i} Y {j}")