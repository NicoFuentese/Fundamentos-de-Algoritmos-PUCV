from PIL import Image

img = Image.open('images.py/C3.5.3.png')
img.show()

#resolucion
largo = float(input())
ancho = float(input())
perimetro = largo * 2 + ancho * 2
area = largo * ancho
print("El perimetro es",perimetro,"y el area",area)
