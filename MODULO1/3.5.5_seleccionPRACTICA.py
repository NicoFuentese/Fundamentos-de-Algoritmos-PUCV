from PIL import Image

img = Image.open('images.py/C3.5.5.png')
img.show()

#resolucion
altura = float(input())
peso = float(input())
imc = peso / (altura**2)
print(round(imc,2))
