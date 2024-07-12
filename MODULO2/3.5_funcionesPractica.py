from PIL import Image

img = Image.open("images.py/C2_3.5.png")
img.show()

#resolucion
def sumaSerieAlternada (numero):
    valor = 2
    suma = 0
    for i in range (1, numero + 1):
        if ( i == 1):
            valor = valor
        elif ( i % 2 == 0):
            valor += 7
        elif ( i % 2 != 0):
            valor -= 3
        suma += valor
    return suma
    