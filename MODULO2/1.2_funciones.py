from PIL import Image

img = Image.open("images.py/C2_1.2.png")
img.show()

#resolucion
def sumaArmonica (n):
    sumatoria = 0
    for i in range (1 , n + 1):
        termino = 1 / i
        sumatoria += termino
    return sumatoria