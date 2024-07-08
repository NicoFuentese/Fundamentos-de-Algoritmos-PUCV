from PIL import Image

img = Image.open('images.py/C3.5.15.png')
img.show()

#resolucion
numero1 = int(input())
numero2 = int(input())
if numero1 < numero2 :
    print("Menor es",numero1)
    print("Mayor es",numero2)
elif numero2 < numero1 :
    print("Menor es",numero2)
    print("Mayor es",numero1)
else :
    print("Iguales")