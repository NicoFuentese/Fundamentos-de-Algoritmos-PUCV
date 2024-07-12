from PIL import Image

img = Image.open("images.py/C2_6.3.png")
img.show()

#resolucion
from math import trunc

def largo (numero):
    contador = 0
    while (numero != 0):
        contador += 1
        numero = numero // 10
    return contador

def esPalindromo (numero):
    cadena = str(numero)
    j = 1
    k = len(cadena)
    contador = 0
    for i in range (1, len(cadena) // 2 + 1):
        num1 = (numero % (10 ** j)) // (10 ** (j - 1))
        num2 = (numero % (10 ** k)) // (10 ** (k - 1))
        if (num1 == num2):
          contador += 1
        j += 1
        k -= 1
    if (contador == len(cadena) // 2):
        return True
    else:
        return False

def contieneAlSiete (numero):
    while (numero != 0):
        if (numero % 10 == 7):
            return True
        numero = numero // 10
    return False

def sumaDigitos12o30 (numero):
    suma = 0
    while (numero != 0):
        digito = numero % 10
        suma += digito
        numero = numero // 10
    if (suma == 30 or suma == 12):
        return True
    else:
        return False

def noContieneAl13 (numero):
    cadena = str(numero)
    for i in range (1, len(cadena)):
        if (i == 1):
            num = numero % (10 ** (i + 1))
        else:
            num = numero % (10 ** (i + 1))
            num = num // (10 ** (i - 1))
        if (num == 13):
            return True
    return False

def esPanchita (numero):
    if (esPalindromo(numero) == True and
    contieneAlSiete(numero) == True and
    sumaDigitos12o30(numero) == True and
    noContieneAl13(numero) == False):
        return True
    else:
        return False

def mostrarNumerosPanchita (a, b):
    print(f"Número(s) panchita en el intervalo [ {a} .. {b} ] = ", end = "")
    contador = 0
    for i in range (a, b + 1):
        if (esPanchita(i) == True and contador == 0):
            print(i, end = "")
            contador += 1
        elif (esPanchita(i) == True and contador != 0):
            print(", ", end = "")
            print(i, end = "")
            contador += 1
    if (contador == 0):
        print("NO HAY NÚMEROS PANCHITA", end = "")
    print()
    print(f"En total hay {contador} número(s) panchita en el intervalo [ {a} .. {b} ]")
            

#main

liminf = int(input())
limsup = int(input())
mostrarNumerosPanchita(liminf, limsup)
