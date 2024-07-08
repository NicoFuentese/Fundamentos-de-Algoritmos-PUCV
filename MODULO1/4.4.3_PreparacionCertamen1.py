from PIL import Image

img = Image.open('images.py/C4.4.3.png')
img.show()

#resolucion
while True:
    comunas = int(input())
    if (1 <= comunas <= 346):
        break

print(f"""Total de Comunas a procesar : {comunas}

AMPLITUDES TÉRMICAS 1 de Enero
==============================
""")

#contadores
t_maximas = 0
contador_insignificante = 0
contador_media = 0
for i in range (1, comunas + 1):
    nombre = input()
    t_min = int(input())
    t_max = int(input())
    amplitud_t = t_max - t_min
    t_maximas += t_max
    
    #categoria
    if (amplitud_t < 5):
        categoria = "INSIGNIFICANTE"
        contador_insignificante += 1
    elif (5 <= amplitud_t < 10):
        categoria = "BAJA"
    elif (10 <= amplitud_t < 18):
        categoria = "MEDIA"
        contador_media += 1
    else:
        categoria = "ALTA"
    
    print(f"""Comuna # {i} nombre: {nombre}
Temp. Mínima = {t_min}
Temp. Máxima = {t_max}
Amplitud Térmica = {amplitud_t} ==> Categoria = {categoria}
""")
    
    #menor amplitud termica
    if ( i == 1 ):
        menor_amplitud_t = amplitud_t
        menor_comuna = nombre
    else:
        menor_amplitud_t = menor_amplitud_t
        menor_comuna = menor_comuna
    
    if (menor_amplitud_t > amplitud_t):
        menor_amplitud_t = amplitud_t
        menor_comuna = nombre

#Reporte final

print("""REPORTE FINAL DE AMPLITUDES TÉRMICAS
====================================
""")

prom_t_max = round(t_maximas / comunas, 2)
print(f"""Promedio de temperaturas máximas registradas es : {prom_t_max} grados Celsius

Menor amplitud térmica calculada : {menor_amplitud_t} grados Celsius - en {menor_comuna}
""")

if (contador_insignificante != 0):
    porc_insignificante = round(contador_insignificante / comunas * 100, 2)
    print(f"""{porc_insignificante} % de Comunas en Categoría 1 - INSIGNIFICANTE
    """)
else:
    print("""No se procesaron comunas cuya amplitud térmica fuera insignificante.
    """)

if (contador_media != 0):
    porc_media = round(contador_media / comunas * 100, 2)
    print(f"""{porc_media} % de Comunas en Categoría 3 - MEDIA
    """)
else:
    print("""No se procesaron comunas cuya amplitud térmica fuera media.
    """)