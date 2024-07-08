from PIL import Image

img = Image.open('images.py/C3.5.13.png')
img.show()

#resolucion
numero = int(input())
if (numero % 5) == 0 :
    print(numero,"si es divisible por 5")
else :
    print(numero,"no es divisible por 5")