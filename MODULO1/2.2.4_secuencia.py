from PIL import Image

img = Image.open('images.py/C2.2.4.png')
img.show()

#resolucion
celsius = float(input())
fa = celsius * 9 / 5 + 32

print(f"{celsius} grados Celsius en grados Fahrenheit es {fa}")
