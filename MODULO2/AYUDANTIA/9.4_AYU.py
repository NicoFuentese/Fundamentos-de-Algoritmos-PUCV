from PIL import Image

img = Image.open("images.py/C2_9.4.png")
img.show()

#resolucion
def sumaSerieAlternada (n):
    sumatoria = 0
    for i in range (1, n + 1):
        if (i == 1):
            termino = 2
            sumatoria += termino
        elif (i % 2 == 0):
            termino += 7
            sumatoria += termino
        else:
            termino += -3
            sumatoria += termino
    return sumatoria
            