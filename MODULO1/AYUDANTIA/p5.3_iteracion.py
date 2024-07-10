from PIL import Image

img = Image.open('images.py/p5.3.png')
img.show()

#resolucion
a = float(input())
n = int(input())

potencia = 1
termino = 1
for i in range (1, n + 1):
    potencia *= a
    termino = termino * a

print(potencia)
    