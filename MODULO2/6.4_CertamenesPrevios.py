from PIL import Image

img = Image.open("images.py/C2_6.4.png")
img.show()

#resolucion
def p1 (numero):
    suma = 0
    while (numero != 0):
        digito = numero % 10
        suma += digito
        numero = numero // 10
    if (suma % 2 == 0):
        return False
    else:
        return True

def cumpleP1 (numero):
    suma = 0
    while (numero != 0):
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

def p2 (numero):
    while (numero != 0):
        digito = numero % 10
        if (digito == 9):
            return True
        numero = numero // 10
    return False
    
def p3 (numero):
    if (numero % 2 != 0 and numero >= 3):
        return True
    else:
        return False

def cumpleP3 (numero):
    if (numero % 2 != 0 and numero >= 3):
        num1 = numero // 2 + 1
        num2 = numero // 2
    return num1, num2

def p4 (numero):
    contador = 2
    for i in range (2, int(numero ** 0.5) + 1):
        if (numero % i == 0):
            if (numero / i == i):
                contador += 1
            else:
                contador += 2
        
    if (contador == 4):
        return True
    return False

def lovalace (numero):
    if (p1(numero) == True and
    p2(numero) == True and
    p3(numero) == True and
    p4(numero) == True):
        return True
    else:
        return False
        

#main
contador = 0
while True:
    numero = int(input())
    if (numero <= 0):
        break
    print(f"""----------------------------
Análisis Número {numero}
----------------------------""")
    if (p1(numero) == True):
        print(f"SI Cumple Propiedad 1 : suma digitos {numero} = {cumpleP1(numero)} es impar.")
    else:
        print("NO Cumple Propiedad 1.")
    if (p2(numero) == True):
        print(f"SI Cumple Propiedad 2 : Tiene al menos un dígito igual a 9")
    else:
        print("NO Cumple Propiedad 2.")
    if (p3(numero) == True):
        resultado1, resultado2 = cumpleP3(numero)
        print(f"SI Cumple Propiedad 3 : {numero} = {resultado2} + {resultado1}")
    else:
        print("NO Cumple Propiedad 3.")
    if (p4(numero) == True):
        print(f"SI Cumple Propiedad 4 : {numero} tiene 4 divisores positivos diferentes.")
    else:
        print("NO Cumple Propiedad 4.")
    
    if (lovalace(numero) == True):
        print("Por lo tanto, SI es de Lovelace.")
        print()
        contador += 1
    else:
        print("Por lo tanto, NO es de Lovelace.")
        print()
if (contador == 1):
    print("Se encontró 1 número de Lovelace en el conjunto de datos.")
elif (contador != 0):
    print(f"Se encontraron {contador} números de Lovelace en el conjunto de datos.")
else:
    print("NO se encontraron números de Lovelace en el conjunto de datos.")