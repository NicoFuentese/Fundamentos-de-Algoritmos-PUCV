from PIL import Image

img = Image.open("images.py/C2_7.4.png")
img.show()

#resolucion
def esMariano (numero):
    sumaImpar = 0
    while numero != 0:
        digito = numero % 10
        if digito % 2 == 1:
            sumaImpar += digito
        numero //= 10
    return sumaImpar % 2 == 1
    
def mostrarMarianosEntreAyB (a, b):
    contador = 0
    for i in range (a, b + 1):
        if esMariano(i) == True:
            print(i, end = " ")
            contador += 1
    if contador == 0:
        print("NO HAY")