from PIL import Image

img = Image.open("images.py/C2_8.2.png")
img.show()

#resolucion
def leerValidar():
    num = int(input())
    while num < 1:
        num = int(input())
    return num

def calcularLargo (numero):
    contador = 0
    if numero == 0:
        largo = 1
    else:
        while numero != 0:
            contador += 1
            numero //= 10
    return contador

def esPlusCuamPerfecto (numero):
    copia = numero
    largo = calcularLargo(numero)
    sumaDigitos = 0
    while numero != 0:
        digito = numero % 10
        sumaDigitos += (digito ** largo)
        numero //= 10
    return sumaDigitos == copia

#main
numero = leerValidar()
if esPlusCuamPerfecto (numero):
    print(f"{numero} ES PLUSCUAMPERFECTO")
else:
    print(f"{numero} NO ES PLUSCUAMPERFECTO")
