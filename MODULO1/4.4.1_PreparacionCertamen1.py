from PIL import Image

img = Image.open('images.py/C4.4.1.png')
img.show()

#resolucion
while True:
    profesionales = int(input())
    if (profesionales >= 4 and profesionales < 101):
        break
print(f"""Total de Profesionales que Rindieron EXAMEN 2021 = {profesionales}
""")

#bucle cada profesional

aprobados_bajo = 0
aprobados_medio = 0
aprobados_alto = 0
aprobados = 0
reprobados = 0
suma = 0
suma_aprobados = 0

for i in range (1, profesionales + 1):
    rut = input()
    ST = int(input())
    SP = int(input())
    SI = int(input())
    
    puntaje_final = int(0.3 * ST + 0.5 * SP + 0.2 * SI)
    suma += puntaje_final

    #aprobacion o reprobacion
    if (ST >= 60 and SP >= 60 and SI >= 60):
        eunacoinf = "APRUEBA"
        suma_aprobados += puntaje_final
        aprobados += 1
        
        if (60 <= puntaje_final < 71):
            competencia = "BAJO"
            aprobados_bajo += 1
        elif (71 <= puntaje_final < 90):
            competencia = "MEDIO"
            aprobados_medio += 1
        else:
            competencia = "ALTO"
            aprobados_alto += 1
    
        #printeo
        print(f"""Profesional rut {rut}
APRUEBA EUNACOINF
Puntaje Final = {puntaje_final}
NIVEL DE COMPETENCIA {competencia}
""")

    else:
        eunacoinf = "REPRUEBA"
        reprobados += 1
        print(f"""Profesional rut {rut}
REPRUEBA EUNACOINF
""")

#porcentajes

if (aprobados > 0):
    prom_PF = round(suma_aprobados / aprobados, 1)
    porc_apro = round(aprobados / profesionales * 100, 1)
    porc_reprob = round(reprobados / profesionales * 100, 1)
    porc_bajo = round(aprobados_bajo / aprobados * 100, 1)
    porc_medio = round(aprobados_medio / aprobados * 100, 1)
    porc_alto = round(aprobados_alto / aprobados * 100, 1)
    
    print(f"""El {porc_apro}% de los profesionales APROBÓ el examen.
El {porc_reprob}% de los profesionales REPROBÓ el examen.
El promedio de puntajes de los aprobados fue {prom_PF}
El {porc_bajo}% de los profesionales que aprobó el examen tiene un nivel de competencia BAJO.
El {porc_medio}% de los profesionales que aprobó el examen tiene un nivel de competencia MEDIO.
El {porc_alto}% de los profesionales que aprobó el examen tiene un nivel de competencia ALTO.""")

else:
    print("""El 0.0% de los profesionales APROBÓ el examen.
El 100.0% de los profesionales REPROBÓ el examen.
NADIE aprobó el examen.""")

