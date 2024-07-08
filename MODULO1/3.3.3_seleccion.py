from PIL import Image

img = Image.open('images.py/C3.3.3.png')
img.show()

#resolucion
edad = int(input())
cajas = int(input())
precio = float(input())
iva = 0.19

#valor de la compra
precio_iva = round(precio * (1 + iva), 1)
precio_total = round(cajas * precio_iva, 1)
print(f"Valor Compra con IVA       = $ {precio_total}")

#descuento
if edad >= 60 and cajas >= 10:
    dscto = 60
else:
    dscto = 7

descuento = round(precio_total * dscto / 100, 1)
print(f"Total Descuento            = $ {descuento}")

valor_compra = round(precio_total - descuento, 1)
print(f"Valor Compra con Descuento = $ {valor_compra}")

