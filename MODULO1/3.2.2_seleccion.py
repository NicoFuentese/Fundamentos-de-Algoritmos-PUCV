from PIL import Image

img = Image.open('images.py/C3.2.2.png')
img.show()

#resolucion
a = float(input())
operador = str(input())
b = float(input())

if operador == "+":
    suma = a + b
    print(f"resultado = {round(suma,1)}")
elif operador == "-":
    resta = a - b
    print(f"resultado = {round(resta,1)}")
elif operador == "*":
    multi = a * b
    print(f"resultado = {round(multi,1)}")
else:
    div = a / b
    print(f"resultado = {round(div,1)}")


