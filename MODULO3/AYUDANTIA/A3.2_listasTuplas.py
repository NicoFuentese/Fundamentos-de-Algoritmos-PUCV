from PIL import Image

img = Image.open("images.py/C3_A3.2.png")
img.show()

#resolucion
from math import sqrt

def procesarPuntos (listaPuntos, listaCirc):
    print("----- PROCESO DE LISTA DE PUNTOS EN FUNCIÓN -----")
    for cadaPunto in listaPuntos:
        contPuntos = 0
        print(f"Punto {cadaPunto} se encuentra al interior de")
        for circunferencia in listaCirc:
            radio = sqrt((cadaPunto[0] - circunferencia[0][0]) ** 2 + (cadaPunto[1] - circunferencia[0][1]) ** 2)
            if (radio < circunferencia[1]):
                print(circunferencia)
                contPuntos += 1
        if (contPuntos == 0):
            print("ninguna circunferencia de la lista")