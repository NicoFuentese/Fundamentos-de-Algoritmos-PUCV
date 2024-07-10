from PIL import Image

img = Image.ope('images.py/p5.2.png')
img.show()

#resolucion
while True:
    n = int(input())
    if (n > 0):
        break

sumatoria = 0
for i in range (1, n + 1):
    termino = i
    sumatoria += termino

print(f"Sumatoria de 1 a {n} = {sumatoria}")