from PIL import Image

img = Image.open('images.py/C3.5.11.png')
img.show()

#resolucion
precio = int(input())
cantidad = int(input())
precioFinal = cantidad * precio
if cantidad >= 10 :
   precioFinal = precioFinal  *0.9
print("Precio final :",round(precioFinal))
