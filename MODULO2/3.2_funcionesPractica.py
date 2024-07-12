from PIL import Image

img = Image.open("images.py/C2_3.2.png")
img.show()

#resolucion
def fnAbsoluto (numero):
    if (numero < 0):
        numero = -numero
    elif (numero > 0):
        numero = numero
    else:
        numero = 0.0
    return numero