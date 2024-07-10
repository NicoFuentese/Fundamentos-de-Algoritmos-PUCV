from PIL import Image

img = Image.ope('images.py/p3.3.png')
img.show()

#resolucion
a = int(input())
b = int(input())

suma = 0

for i in range (a, b + 1):
    #SUMA
    if (i % 2 == 0 and i % 3 == 0):
        suma += i
    
if suma == 0:
    print("NO EXISTEN NUMEROS DIVISIBLES POR 2 Y POR 3 EN EL INTERVALO")
else:
    print(f"SUMA = {suma}")