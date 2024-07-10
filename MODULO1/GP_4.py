#resolucion
"""----------------------------------------------------------------------------
NOMBRE : NICOLAS FUENTES WILLIAMS
Este programa mide el Test de Rubier, lee la cantidad de estudiantes, el nombre, 
y edad de cada uno para calcular la resistencia aerobica para cada uno.
----------------------------------------------------------------------------"""

"""----------------------------------------------------------------------------
  Se lee el total de estudiantes validando que el valor se encuente en 
  el intervalo de [4..200].-
----------------------------------------------------------------------------"""

while True:
    estudiantes = int(input())
    if (4 < estudiantes < 200):
        break

"""----------------------------------------------------------------------------
  Se imprime por pantalla el total de estudiantes controlados.
----------------------------------------------------------------------------"""

print(f"""SE CONTROLARON {estudiantes} estudiantes.
""")

"""----------------------------------------------------------------------------
  Para cada estudiante se leen el nombre, edad y pulsaciones antes y despues
  de las sentadillas, y post 1 minuto de descanso.
  
  Se cuenta el total de niños y adolescentes testeados, la suma de su registro
  aerobico y la cantidad de estudiantes excelentes, buenos, promedios, 
  insuficientes y pobres segun su registro.
----------------------------------------------------------------------------"""

niños = 0
suma_niños = 0
adolescentes = 0
suma_adolescentes = 0
contador = 0
contador_exc = 0
contador_bue = 0
contador_prom = 0
contador_insuf = 0
contador_pobre = 0
for i in range (1, estudiantes + 1):
    contador += 1
    nombre = input()
    edad = int(input())
    p0 = int(input()) #durante 15 seg antes sentadilla
    p1 = int(input()) #durante 15 seg despues sentadilla
    p2 = int(input()) #15 seg post 1 min descanso
    
    #calculo a 1 min
    p0_min = p0 * 4
    p1_min = p1 * 4
    p2_min = p2 * 4
    
    #resistencia aerobica
    
    RA = round(((p0_min + p1_min + p2_min) - 200) / 10, 1)
    
    #estado de forma fisica
    if (RA == 0):
        estado = "EXCELENTE"
        contador_exc += 1
    elif (0 < RA <= 5):
        estado = "BUENO"
        contador_bue += 1
    elif (5 < RA <= 10):
        estado = "PROMEDIO"
        contador_prom += 1
    elif (10 < RA <= 15):
        estado = "INSUFICIENTE"
        contador_insuf += 1
    else:
        estado = "POBRE"
        contador_pobre += 1
    
    #niño o adolescente
    if (edad < 14):
        grado = "NIÑO"
        niños += 1
        suma_niños += RA
    else: 
        grado = "ADOLESCENTE"
        adolescentes += 1
        suma_adolescentes += RA
    
    
    #printeo
    print(f"""ESTUDIANTE # {i} - {nombre} - {grado}
Resistencia aeróbica = {RA}
Estado de forma física es {estado}
""")

#reporte final promedios
#niños

"""----------------------------------------------------------------------------
  Se imprime por pantalla rl titulo del reporte final de promedios.
----------------------------------------------------------------------------"""    
print(f"""REPORTE FINAL PROMEDIOS
=======================
""")

"""----------------------------------------------------------------------------
  Se calcula el promedio de niños y/o adolescentes si esque hay en el estudio,
  sino, se imprime otro mensaje y no se calcula.
----------------------------------------------------------------------------"""   

if (niños != 0):
    prom_niños = round(suma_niños / niños, 1)
    print(f"""Promedio de resistencia aeróbica del grupo de niños = {prom_niños}""")
else:
    print(f"""Dentro del grupo de estudiantes controlados NO habían niños""")

if (adolescentes != 0):
    prom_adolescentes = round(suma_adolescentes / adolescentes, 1)
    print(f"""Promedio de resistencia aeróbica del grupo de adolescentes = {prom_adolescentes}
    """)
else:
    print(f"""Dentro del grupo de estudiantes controlados NO habían adolescentes
    """)

"""----------------------------------------------------------------------------
  Se calcula el porcentaje total de estudiantes excelentes, promedios y
  pobres del curso.-
----------------------------------------------------------------------------"""   

#reporte final porcentajes
porc_exc = round((contador_exc / contador) * 100, 1)
porc_prom = round((contador_prom / contador) * 100, 1)
porc_pobre = round((contador_pobre / contador) * 100, 1)

"""----------------------------------------------------------------------------
  Se imprime por pantalla el porcentaje total de estudiantes excelentes, 
  promedios y pobres del curso.-
----------------------------------------------------------------------------"""   

print(f"""REPORTE FINAL PORCENTAJES
=========================

El {porc_exc} % de estudiantes tenían una forma de estado físico excelente.
El {porc_prom} % de estudiantes tenían una forma de estado físico promedio.
El {porc_pobre} % de estudiantes tenían una forma de estado físico pobre.""")
