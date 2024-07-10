from PIL import Image

img = Image.ope('images.py/p5.5.png')
img.show()

#resolucion
inicial = int(input())
print(inicial, end = " ")

restante = inicial
while (restante > 0):
    restante = restante - 20
    if (restante >= 0):
        print(restante, end = " ")