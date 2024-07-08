from PIL import Image

img = Image.open('images.py/C4.5.1.png')
img.show()

#resolucion
a = int(input())
b = int(input())

#patron sumatoria
suma = 0 #acumulador de sumas

for i in range(a , b + 1):
    suma += (i ** 2)
    
print(f"La suma de cuadrados entre {a} y {b} es {suma}")