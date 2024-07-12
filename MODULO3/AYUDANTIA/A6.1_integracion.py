from PIL import Image

img = Image.open("images.py/C3_A6.1.png")
img.show()

#resolucion
def leerDatosSinRepeticiones():
    lista = []
    while True:
        numero = int(input())
        if (numero == 0):
            return lista
        if (numero in lista):
            continue
        lista.append(numero)

def sumarDigitosCuadrados (numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += (digito) ** 2
        numero //= 10
    return suma

def esFeliz (numero):
    temp = numero
    while True:
        if (temp == 1):
            return True
        if (temp ==89):
            return False
        temp = sumarDigitosCuadrados(temp)

def obtenerFelicesOrdenados (listaOriginal):
    listaFeliz = []
    for numero in listaOriginal:
        if (esFeliz(numero)):
            listaFeliz.append(numero)
    listaFeliz.sort()
    return listaFeliz


