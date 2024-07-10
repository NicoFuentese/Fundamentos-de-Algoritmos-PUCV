from PIL import Image

img = Image.open('images.py/p4.2.png')
img.show()

#resolucion
# i = 0 -> n
# (3*(i - 1) + 1) / (3 * (i - 1) + 2)

while True:
    n = int(input())
    if (n >= 1):
        break
sumatoria = 0
for i in range (1, n + 1):
    termino = (3*(i - 1) + 1) / (3 * (i - 1) + 2)
    sumatoria += termino

print(f"El resultado de la sumatoria es {sumatoria}")