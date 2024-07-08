from PIL import Image

img = Image.open('images.py/C3.5.8.png')
img.show()

#resolucion
numero = int(input())
ultimoDig = abs (numero) % 10
print(ultimoDig)
