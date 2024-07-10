from PIL import Image

img = Image.open('images.py/p4.5.png')
img.show()

#resolucion
while True:
    altura = int(input())
    if 0 < altura < 21:
        break

for i in range(1, altura + 1):
    print("*" * i)
