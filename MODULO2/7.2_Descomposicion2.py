from PIL import Image

img = Image.open("images.py/C2_7.2.png")
img.show()

#resolucion
def invertir(numero):
    nuevo = 0
    while numero != 0:
        digito = numero % 10
        nuevo = nuevo * 10 + digito
        numero = numero // 10
    return nuevo

def palindromo (numero):
    return numero == invertir(numero)