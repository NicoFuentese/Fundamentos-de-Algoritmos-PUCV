from PIL import Image

img = Image.open("images.py/C2_8.3.png")
img.show()

#resolucion
def palindromo (numero):
    if (numero == inverso(numero)):
        return True
    else:
        return False

def inverso(numero):
    copy = numero
    contador = 0
    while (numero != 0):
        digito = numero % 10
        contador += 1
        numero //= 10
    inverso = 0
    for i in range(contador, 0, -1):
        inverso += (copy % 10) * (10 ** (i - 1))
        copy //= 10
    return inverso

#main
x = int(input())
if (palindromo(x) == True):
    print(f"{x} ES PALINDROMO")
else:
    contador = 0
    copia = x
    while (palindromo(x) != True):
        x += inverso(x)
        contador += 1
    if (contador == 1):
        print(f"{copia} NO ES PALINDROMO, SE REALIZO {contador} SUMA PARA OBTENER EL PALINDROMO {x}")
    else:
        print(f"{copia} NO ES PALINDROMO, SE REALIZARON {contador} SUMAS PARA OBTENER EL PALINDROMO {x}")
