from PIL import Image

img = Image.open('images.py/C1.1.png')
img.show()

#resolucion
altura = float(input())
peso = float(input())

imc = peso / (altura ** 2)
print(imc)
