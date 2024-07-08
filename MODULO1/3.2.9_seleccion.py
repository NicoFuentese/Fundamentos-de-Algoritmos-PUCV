from PIL import Image

img = Image.open('images.py/C3.2.9.png')
img.show()

#resolucion
a = float(input())
b = float(input())
c = float(input())

if a >= b + c or b >= a + c or c >= a + b:
    print("No es un triángulo")
else:
    print("Si es un triángulo")
    if a == b and b == c and c == a:
        print("El triángulo es equilátero")
    elif a == b or b == c or c == a:
        print("El triángulo es isósceles")
    elif not(a == b or b == c or c == a):
        print("El triángulo es escaleno")
    