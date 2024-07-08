from PIL import Image

img = Image.open('images.py/C4.1.2.png')
img.show()

#resolucion
n = int(input())

control = 2
while (control <= n):
    print(control, end = " ")
    control +=2
    