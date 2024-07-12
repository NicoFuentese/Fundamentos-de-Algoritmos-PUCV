from PIL import Image

img = Image.open("images.py/C2_10.2.png")
img.show()

#resolucion
def totalCuadrados (n):
    suma = 0
    for i in range (1, n + 1):
        termino = i ** 2
        suma += termino
    return suma

def validar ():
    n = int(input())
    while n <1 or n >1500:
        n = int(input())
    return n
    """
    while True:
        n = int(input())
        if ( 1 <= n >= 1500):
            break
    return n
"""
numero = validar()
cuadrados = totalCuadrados(numero)

print(f"En tablero de {numero} x {numero} total de cuadrados es {cuadrados}")