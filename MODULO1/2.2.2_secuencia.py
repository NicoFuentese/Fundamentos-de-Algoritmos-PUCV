from PIL import Image

img = Image.open('images.py/C2.2.2.png')
img.show()

#resolucion
num = int(input())
dig = num % 10
print(dig)