from PIL import Image

img = Image.open('images.py/p4.1.png')
img.show()

#resolucion
while True:
    n = int(input())
    if n >= 1:
        break

sumatoria = 0
for i in range(1, n + 1):
    termino = (2 * i) / (2 * i - 1)
    sumatoria += termino
    
print(f"El resultado de la sumatoria es {sumatoria}")