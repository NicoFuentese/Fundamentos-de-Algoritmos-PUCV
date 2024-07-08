from PIL import Image

img = Image.open('images.py/C4.1.4.png')
img.show()

#resolucion
n = int(input())

print(f"Potencias de 2 de 0 a {n} :")
for i in range(n + 1):
    resultado = pow(2,i)
    print (resultado)