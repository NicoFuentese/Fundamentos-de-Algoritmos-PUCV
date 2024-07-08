from PIL import Image

img = Image.open('images.py/C1.3.png')
img.show()

#resolucion
#perimetro y area de un rectangulo

ancho = float(input())
largo = float(input())

perimetro = 2*ancho+2*largo
area = ancho*largo

print("El perímetro es",perimetro,"y el área es",area)
