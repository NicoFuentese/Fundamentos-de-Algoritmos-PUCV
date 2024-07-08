from PIL import Image

img = Image.open('images.py/C4.1.1.png')
img.show()

#resolucion
n = int(input())

control = 1
while (control <=n):
    print(control, end = " ")
    control +=1