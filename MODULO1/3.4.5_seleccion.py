from PIL import Image

img = Image.open('images.py/C3.4.5.png')
img.show()

#resolucion
total_articulos = int(input())
total_servicios = int(input())

total_compra = total_articulos + total_servicios

#dscto articulos
if (total_articulos <= 10000):
    dscto_art = 0
elif (total_articulos > 10000 and total_articulos <= 50000):
    dscto_art = 7
elif (total_articulos > 50000):
    dscto_art = 9

dscto_articulos = int(round(total_articulos * dscto_art / 100,0))

#dscto servicios
if (total_servicios <= 15000):
    dscto_ser = 10
    dscto_servicio = int(round(total_servicios * dscto_ser / 100,0))
elif (total_servicios > 15000):
    primer_dscto = 1500 #dscto del 10%
    dscto_ser_exc = 15
    dscto_servicio = int(round(1500 + (total_servicios - 15000) * dscto_ser_exc / 100,0))

#dscto por ambas compras
if (total_articulos != 0 and total_servicios != 0):
    dscto_ser_art = 8
    if (((total_compra- dscto_articulos - dscto_servicio) * 8 / 100) >= 5000):
        dscto_ser_art_aplicado = 5000
    else: 
        dscto_ser_art_aplicado = (total_compra- dscto_articulos - dscto_servicio) * dscto_ser_art / 100
else:
    dscto_ser_art = 0
    dscto_ser_art_aplicado = 0

#total dscto
total_dscto = int(round(dscto_articulos + dscto_servicio + dscto_ser_art_aplicado,0))

dscto_acumulado = dscto_articulos + dscto_servicio

#TOTAL
total_pagar = int(round(total_compra - total_dscto,0))

print(f"descuento venta es {dscto_articulos}")
print(f"descuento servicio es {dscto_servicio}")
print(f"descuento acumulado es {int(round(dscto_ser_art_aplicado,0))}")
print(f"TOTAL es {total_pagar}")