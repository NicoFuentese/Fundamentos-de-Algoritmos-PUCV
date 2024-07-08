from PIL import Image

img = Image.open('images.py/C2.2.1.png')
img.show()

#resolucion
f = float(input())

c = (f - 32) * (5/9)
k = c + 273.15

print(f"""{f} grados Fahrenheit es equivalente a {round(k,2)} grados Kelvin.""")