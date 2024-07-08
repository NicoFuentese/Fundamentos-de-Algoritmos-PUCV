from PIL import Image

img = Image.open('images.py/C4.5.2.png')
img.show()

#resolucion

while True:
    n = int(input())
    if n > 0:
        break

suma = 0
for i in range (1 , n + 1):
    termino = (2*i - 1) / (2 * i)
    suma += termino
    
print(f"El resultado de la sumatoria es {suma}")