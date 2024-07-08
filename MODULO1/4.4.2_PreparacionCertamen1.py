from PIL import Image

img = Image.open('images.py/C4.4.2.png')
img.show()

#resolucion
while True:
    vehiculos = int(input())
    if (vehiculos > 0):
        break

#total vehiculos controlados
print(f"""SE CONTROLARON {vehiculos} VEHICULOS
""")

#contadores
errores = 0
no_excedieron = 0
excedieron = 0
menos_grave = 0
grave = 0
gravisima = 0
suma_utm = 0

for i in range (1, vehiculos + 1):
    patente = input()
    mts = int(input()) #distancia del tramo en mts
    v_max = int(input()) #permitida en todo el tramo
    tramo = int(input()) #segundos en cruzar el tramo
    
    print(f"""VEHICULO {i} PATENTE {patente}""")
    
    if (mts <= 0 or v_max <= 0 or tramo <= 0):
        print("""ERROR EN LOS DATOS REGISTRADOS.
        """)
        errores += 1
    else:
        #velocidad del vehiculo
        # 1 hr -> 3600 sg
        # x hr -> tramo sg
        # hrs = tramo / 3600
        # 1 km -> 1000 mts
        #km = mts / 1000
        tramo_hrs = tramo / 3600
        km = mts / 1000
        v = int(km / tramo_hrs)
        
        print(f"""Velocidad Máxima Permitida en el Tramo = {v_max}
Velocidad Media Vehículo = {v}""")
        
        #excede o no la velocidad maxima
        if (v <= v_max):
            print("""No excedió velocidad máxima permitida.
            """)
            no_excedieron += 1
            multa = 0
        else:
            print(f"Excedió velocidad máxima permitida en {v-v_max} kms/h.")
            excedieron += 1
        
            if (v <= v_max + 10):
                falta = "Menos Grave"
                multa = 1
                print(f"""FALTA : {falta} - SANCIÓN : {multa} UTM.
                """)
                menos_grave += 1
            elif (v_max + 10 < v <= v_max + 20):
                falta = "Grave"
                multa = 1.5
                print(f"""FALTA : {falta} - SANCIÓN : {multa} UTM.
                """)
                grave += 1
            else:
                falta = "Gravísima"
                multa = 3
                print(f"""FALTA : {falta} - SANCIÓN : {multa} UTM y se SUSPENDE LICENCIA 45 días.
                """)
                gravisima += 1
            
        suma_utm += multa

#reporte final

porc_erroneos =round(errores / vehiculos * 100, 1)
porc_no_excedieron = round(no_excedieron / vehiculos * 100, 1)
porc_menos_grave = round(menos_grave / vehiculos * 100, 1)
porc_grave = round(grave / vehiculos * 100, 1)
porc_gravisima = round(gravisima / vehiculos * 100, 1)

print(f"""********** REPORTE FINAL **********

El {porc_erroneos} % presentó un error en el registro de datos.
El {porc_no_excedieron} % NO iba a exceso de velocidad.
El {porc_menos_grave} % cometió una falta menos grave.
El {porc_grave} % cometió una falta grave.
El {porc_gravisima} % cometió una falta gravísima.

Se recaudaron {suma_utm} UTMs.

*********** FIN REPORTE ************""")