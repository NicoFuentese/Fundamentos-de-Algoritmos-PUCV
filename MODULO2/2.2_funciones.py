from PIL import Image

img = Image.open("images.py/c2_2.2.png")
img.show()

#resolucion
def contarDivisores (n):
    contador = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            contador += 1
    return contador
