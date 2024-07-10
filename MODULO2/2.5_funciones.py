from PIL import Image

img = Image.open("images.py/c2_2.5.png")
img.show()

#resolucion
def esDeficiente (n):
    suma = 0
    for i in range (1, n):
        if (n % i == 0):
            suma += i
    if (suma < n):
        return True
    else:
        return False