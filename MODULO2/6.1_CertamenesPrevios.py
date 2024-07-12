from PIL import Image

img = Image.open("images.py/C2_6.1.png")
img.show()

#resolucion
from math import sqrt
from math import trunc

def esPrimo(numero):
    if (numero == 1):
        return False
    else:
        contador = 0
        for i in range (1, numero + 1):
            if (numero % i == 0):
                contador +=1
        if (contador == 2):
            return True
        else:
            return False

def ALFA (n):
    suma = 0
    if (n == 1):
        suma = suma
    else:
        for i in range (1, n + 1):
            if (n % i == 0 and esPrimo (i) == True):
                suma += i
    return suma
    
def BETA (numero):
    cubo = numero ** 3
    contador = 0
    if (cubo == 0):
        contador = 1
    else:
        while (cubo > 0):
            digito = cubo % 10
            if ( digito % 2 == 0):
                contador += 1
            cubo = cubo // 10
    return contador

def GAMA (n, w):
    sumatoria = 0
    for i in range (2, w + 1):
        termino = n ** i / 2 ** i
        sumatoria += termino
    resultado = int(sqrt(sumatoria))
    return resultado

def poderPelea (CB, CRLM, AE, VPB):
    formula = (ALFA(CB) + BETA(CRLM)) * (GAMA(AE, VPB) + 1)
    return formula

#main
poderDePelea = 0
while (poderDePelea <= 100000):
    nombre = input()
    VPB = int(input())
    AE = int(input()) #anios
    CB = int(input())
    CRLM = int(input())
    poderDePelea = poderPelea(CB, CRLM, AE, VPB)
    print(f"El poder de pelea de {nombre} es {poderDePelea} Ki.")
    
print("Dispositivo Rastreador Estalló - FIN DEL PROCESO.")
