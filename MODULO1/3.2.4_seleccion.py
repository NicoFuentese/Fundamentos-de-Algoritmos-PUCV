from PIL import Image

img = Image.open('images.py/C3.2.4.png')
img.show()

#resolucion
a = int(input())
b = int(input())

if a > 10 and b > 10:
    print("Ambos son mayores a 10")
elif a < 10 and b < 10:
    print("Ninguno es mayor a 10")
elif a  > 10 or b > 10:
    if a > 10:
        print(f"{a} es mayor a 10")
    else:
        print(f"{b} es mayor a 10")
else:
    print("Ninguno es mayor a 10")

