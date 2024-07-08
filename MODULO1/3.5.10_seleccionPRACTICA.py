from PIL import Image

img = Image.open('images.py/C3.5.10.png')
img.show()

#resolucion
radio = float(input())
perimetro = 2 * 3.14 * radio
area = 3.14 * (radio ** 2)
print("area =",area)
print("perimetro =",perimetro)