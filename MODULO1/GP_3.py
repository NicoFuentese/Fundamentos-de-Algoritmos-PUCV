#resolucion

"""----------------------------------------------------------------------------
NOMBRE : NICOLAS FUENTES WILLIAMS
Este programa lee los precios de las gasolinas 93, 95 y 97 del fin de semana,
ademas lee y verifica la cantidad de clientes a procesar, leyendo los datos
de cada uno y calculando el descuento el tipo de gasolina y la cantidad de 
litros comprados. Imprimiendo todo en reportes por cliente y general.
----------------------------------------------------------------------------"""

"""----------------------------------------------------------------------------
  Se lee el valor de fin de semana de los tipos de gasolina.
----------------------------------------------------------------------------"""
fuel93 = int(input())
fuel95 = int(input())
fuel97 = int(input())

"""----------------------------------------------------------------------------
  Se lee el total de clientes validando que el valor se encuente en 
  el intervalo de [0..10000].-
----------------------------------------------------------------------------"""
while True :
    clientes = int(input())
    if 0 < clientes < 10000 :
        break

"""----------------------------------------------------------------------------
  Se printea el total de clientes a procesar.
----------------------------------------------------------------------------"""

print(f'''Se procesarán {clientes} clientes(s). 

INICIO DEL PROCESAMIENTO DE DATOS
=================================
''')
"""----------------------------------------------------------------------------
 Comienzo del procesamiento por cliente y lectura de datos personales. Ademas
 de inicio en 0 de los contadores.
----------------------------------------------------------------------------"""
acumuladoFuel = 0
acumuladoLitros = 0
noDescuento = 0
clientes93 = 0
clientes95 = 0
clientes97 = 0
promFuel93 = 0.0
promFuel97 = 0.0

for i in range(clientes) :
    if clientes > i :
        rut = str(input())
        tipoFuel = int(input())
        litros = int(input())

        acumuladoLitros += litros

    """----------------------------------------------------------------------------
      Clasificacion del descuento asignado segun litros consumidos y tipo
      de gasolina.
    ----------------------------------------------------------------------------"""

    if tipoFuel == 93 :
        promFuel93 += litros
        clientes93 += 1
        valorFuel = fuel93 * litros

        if 1 <= litros <= 10 :
            descuento = 0
            noDescuento += 1
        elif 11 <= litros <= 20 :
            descuento = 5
        else:
            descuento = 10

    elif tipoFuel == 95 :
        clientes95 += 1
        valorFuel = fuel95 * litros

        if 1 <= litros <= 10 :
            descuento = 0
            noDescuento += 1
        elif 11 <= litros <= 20 :
            descuento = 10
        else:
            descuento = 20

    else:
        promFuel97 += litros
        clientes97 += 1
        valorFuel = fuel97 * litros

        if 1 <= litros <= 10 :
            descuento = 10
        elif 11 <= litros <= 20 :
            descuento = 20
        else:
            descuento = 30

    """----------------------------------------------------------------------------
      Calculo del descuento realizado y el descuento acumulado.
    ----------------------------------------------------------------------------"""

    monto_descuento = valorFuel - (valorFuel*(descuento/100))
    acumuladoFuel += monto_descuento
 
    """----------------------------------------------------------------------------
      Se muestran en pantalla los datos de los clientes procesados.
    ----------------------------------------------------------------------------"""

    print(f'''Rut : {rut}
Tipo Gasolina : {tipoFuel}
Litros Comprados : {litros}
Precio bencina sin descuento ${valorFuel}
Porcentaje de descuento {descuento}%
Total a pagar POST descuento ${monto_descuento}
------------------------------------------------
''')

"""----------------------------------------------------------------------------
  Se muestran en pantalla el reporte final que incluye lo recaudado por
  venta de bencina, los litros vendidos y los clientes que no obtuvieron
  un descuento. Ademas, del porcentaje de los clientes que compraron bencina
  de 93 o 97, o si no compraron.
----------------------------------------------------------------------------"""

print(f'''
REPORTE FINAL
=============
Se recaudaron por venta de bencina ${acumuladoFuel}.-
Se vendieron {acumuladoLitros } litros de bencina.-
Clientes que NO obtuvieron descuento = {noDescuento}.-''')

promClie93 = round(( clientes93 / clientes ) * 100,1)
print(f'{promClie93}% de los clientes compraron bencina de 93 octanos.-')

if promClie93 == 0 :
    print('No se procesaron clientes que compraron bencina de 93 Octanos.-')
else:
    print(f'Promedio de litros de bencina de 93 octanos vendidos = {round((promFuel93/clientes93),2)}.-')

promClie97 = round(( clientes97 / clientes ) * 100,1)
print(f'{promClie97}% de los clientes compraron bencina de 97 octanos.-')

if promClie97 == 0 :
    print('No se procesaron clientes que compraron bencina de 97 Octanos.-')
else:
    print(f'Promedio de litros de bencina de 97 octanos vendidos = {round((promFuel97/clientes97),2)}.-')
