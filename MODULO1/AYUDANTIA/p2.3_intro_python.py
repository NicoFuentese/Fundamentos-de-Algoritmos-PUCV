from PIL import Image

img = Image.open('images.py/p2.3.png')
img.show()

#resolucion
from math import trunc

#inputs
placa = input()
categoria = int(input())
tarifa = input()
km = float(input())

#imprimir data
print(f"""Vehículo Placa Patente : {placa}
Categoría del Vehículo : {categoria}
Categoría Tarifa : {tarifa}
Distancia recorrida por el vehículo = {km} kms.""")

#Calculo monto total
t_1_baja = 90
t_4_baja = 100
t_2_media = 360
t_3_alta = 780

t_2_baja = t_2_media / 2
t_3_baja = t_3_alta / 3
t_1_media = 2 * t_1_baja
t_3_media = 2 * t_3_baja
t_4_media = 3 * t_4_baja
t_1_alta = 3 * t_1_baja
t_2_alta = 3 * t_2_baja
t_4_alta = 5 * t_4_baja

#monto x portico
if tarifa == "BAJA":
    if categoria == 1:
        monto_total = t_1_baja * km
    elif categoria == 2:
        monto_total = t_2_baja * km
    elif categoria == 3:
        monto_total = t_3_baja * km
    elif categoria == 4:
        monto_total = t_4_baja * km
elif tarifa == "MEDIA":
    if categoria == 1:
        monto_total = t_1_media * km
    elif categoria == 2:
        monto_total = t_2_media * km
    elif categoria == 3:
        monto_total = t_3_media * km
    elif categoria == 4:
        monto_total = t_4_media * km
elif tarifa == "ALTA":
    if categoria == 1:
        monto_total = t_1_alta * km
    elif categoria == 2:
        monto_total = t_2_alta * km
    elif categoria == 3:
        monto_total = t_3_alta * km
    elif categoria == 4:
        monto_total = t_4_alta * km

monto_total = trunc(monto_total)

print(f"Valor del peaje calculado es ${monto_total}")

#descuento
if monto_total < 2000:
    dscto = 0
elif monto_total < 5000:
    dscto = 0.07
elif monto_total <= 10000:
    dscto = 0.12
elif monto_total > 10000:
    dscto = 0.15

if dscto == 0:
    print("No se aplica descuento")
else:
    monto_final = trunc(monto_total * (1 - dscto))
    print(f"Se aplica descuento del {int(dscto*100)}%")
    print(f"Valor Final del peaje a pagar es ${monto_final}")


