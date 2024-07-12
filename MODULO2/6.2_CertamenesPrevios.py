from PIL import Image

img = Image.open("images.py/C2_6.2.png")
img.show()

#resolucion
from math import trunc
from math import sqrt

def esPrimo (numero):
    if (numero <= 1):
        return False
    for i in range (2, int(numero ** 0.5) + 1):
        if (numero % i == 0):
            return False
    return True

def primoTruncable (numero):
    while (esPrimo(numero) == True):
        numero = numero // 10
    if (numero == 0):
        return True
    else:
        return False
        

def largo (numero):
    contador = 0
    if (numero == 0):
        contador = 1
    else:
        while (numero != 0):
            contador += 1
            numero = numero // 10
    return contador

def esImpar (numero):
    if (numero % 2 == 0):
        return False
    else:
        return True

def serieArmonica (m):
    n = trunc(sqrt(m))
    sumatoria = 0
    if (m == 0):
        valor = sumatoria
    else:
        for i in range (1, n + 1):
            termino = 1 / i
            sumatoria += termino
        valor = trunc(sumatoria) * m
    if (esImpar(largo(valor)) == True):
        return True
    else:
        return False

#main
while True:
    nombre = input()
    if (nombre == "FIN"):
        break
    midiclorianos = int(input())
    if primoTruncable(midiclorianos) == True and serieArmonica(midiclorianos) == True:
        print(f"{nombre} tiene {midiclorianos} midiclorianos *** ALERTA *** --> SI ES PROPENSO AL LADO OSCURO.")
    else:
        print(f"{nombre} tiene {midiclorianos} midiclorianos --> NO ES PROPENSO AL LADO OSCURO.")
    print()
print("--- MAY THE FORCE WITH YOU ---")
#-----------------------------------------------
#                PROGRAMA PRINCIPAL
#-----------------------------------------------
