from PIL import Image

img = Image.open('images.py/C3.5.12.png')
img.show()

#resolucion
numero = int(input())
ultimoDigito = numero % 10
if (ultimoDigito == 3) or (ultimoDigito == 7)  :
    print("SI")
else :
    print("NO")
