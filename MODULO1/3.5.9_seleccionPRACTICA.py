from PIL import Image

img = Image.open('images.py/C3.5.9.png')
img.show()

#resolucion
valor = float(input())
iva = (valor * 19 / 100)
valorFinal = round(valor + iva)
print("El valor final del producto con IVA es de",valorFinal,"pesos.")