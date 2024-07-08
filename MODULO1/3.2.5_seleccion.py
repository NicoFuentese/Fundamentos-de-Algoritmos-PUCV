from PIL import Image

img = Image.open('images.py/C3.2.5.png')
img.show()

#resolucion
a = int(input())
b = int(input())
c = int(input())
d = int(input())

promedio = int((a + b + c + d) / 4)
print(f"promedio = {promedio}")

if promedio >= 90 and promedio <= 100:
    print("nota final = A")
elif promedio >= 80 and promedio < 90:
        print("nota final = B")
elif promedio >= 70 and promedio < 80:
        print("nota final = C")
elif promedio >= 60 and promedio < 70:
        print("nota final = D")
elif promedio >= 0 and promedio < 60:
        print("nota final = E")