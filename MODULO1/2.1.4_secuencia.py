from PIL import Image

img = Image.open('images.py/C2.4.png')
img.show()

#resolucion
precio = int(input())
dscto = int(input())

print(f"Monto Total Medicamentos = {precio}")
print(f"Porcentaje de descuento = {dscto}%")

descontado = int(precio*(dscto/100))
final = int(precio-descontado)

print(f"Monto de descuento = {descontado}")
print(f"Monto Total a Pagar = {final}")
