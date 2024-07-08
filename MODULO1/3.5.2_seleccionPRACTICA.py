from PIL import Image

img = Image.open('images.py/C3.5.2.png')
img.show()

#resolucion
valorPagado = int(input())
valorProducto = valorPagado /1.19
montoIVA = valorPagado - valorProducto
print("para $",valorPagado, "el iva correspondiente es",round(montoIVA))