#resolucion
"""----------------------------------------------------------------------------
NOMBRE : NICOLAS FUENTES WILLIAMS
Este programa lee el rut, edad y sexo de la persona analizada. Se calcula el
porcentaje de grasa corporal (PGC) de la perosna segun sexo y se establece su 
clasificacion segun su PGC, sexo y edad.
----------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------
 Se importa la funcion log10 desde la libreria math para utilizarla en el
 calculo de PGC.
----------------------------------------------------------------------------"""
from math import log10

"""----------------------------------------------------------------------------
  Se leen los datos de las personas. Y se decodifica el sexo de la persona.
----------------------------------------------------------------------------"""
rut = input()
edad = int(input())
sexo = int(input()) # 1 = HOMBRE y 2 = MUJER

#sexo
if (sexo == 1):
    sex = "Hombre"
else:
    sex = "Mujer"

"""----------------------------------------------------------------------------
  Segun el sexo de la persona se ingresan sus datos para calcular el PGC. 
  Para Hombres se pide ingresar medidas de cintura, cuello (en cms) y altura
  (mts). Para mujer se pide ingresar las medidas de cintura, cadera, cuello
  ( en cms) y su altura (mts).
----------------------------------------------------------------------------"""
#Calculo PGC
if (sexo == 1):
    cintura = int(input())
    cuello = int(input())
    altura = float(input()) * 100
    
    PGC = round(( (495 / (1.0324 - 0.19077 * log10(cintura - cuello) + 0.15456 * log10(altura))) ) - 450, 2)
    
else:
    cintura = int(input())
    cadera = int(input())
    cuello = int(input())
    altura = float(input()) * 100
    
    PGC = round((495 / (1.29579 - 0.35004 * log10(cintura + cadera - cuello) + 0.22100 * log10(altura) ) ) - 450, 2)

"""----------------------------------------------------------------------------
  Se clasifica segun los datos de sexo, edad y PGC calculado el rango de grasa
  ideal para la persona
----------------------------------------------------------------------------"""
#Clasificacion

#mujer
if (sexo == 2):
    if (20 <= edad < 40):
        if (PGC < 21):
            rango = "Bajo en Grasa"
        elif ( 21 <= PGC < 33):
            rango = "Saludable"
        elif (33 <= PGC < 39):
            rango = "Sobrepeso"
        elif (PGC >= 39):
            rango = "Obesidad"
    elif (40 <= edad < 60):
        if (PGC < 23):
            rango = "Bajo en Grasa"
        elif ( 23 <= PGC < 35):
            rango = "Saludable"
        elif (35 <= PGC < 40):
            rango = "Sobrepeso"
        elif (PGC >= 40):
            rango = "Obesidad"
    elif (60 <= edad < 80):
        if (PGC < 24):
            rango = "Bajo en Grasa"
        elif ( 24 <= PGC < 36):
            rango = "Saludable"
        elif (36 <= PGC < 42):
            rango = "Sobrepeso"
        elif (PGC >= 42):
            rango = "Obesidad"

#hombres

if (sexo == 1):
    if (20 <= edad < 40):
        if (PGC < 8):
            rango = "Bajo en Grasa"
        elif ( 8 <= PGC < 20):
            rango = "Saludable"
        elif (20 <= PGC < 25):
            rango = "Sobrepeso"
        elif (PGC >= 25):
            rango = "Obesidad"
    elif (40 <= edad < 60):
        if (PGC < 11):
            rango = "Bajo en Grasa"
        elif ( 11 <= PGC < 22):
            rango = "Saludable"
        elif (22 <= PGC < 28):
            rango = "Sobrepeso"
        elif (PGC >= 28):
            rango = "Obesidad"
    elif (60 <= edad < 80):
        if (PGC < 13):
            rango = "Bajo en Grasa"
        elif ( 13 <= PGC < 25):
            rango = "Saludable"
        elif (25 <= PGC < 30):
            rango = "Sobrepeso"
        elif (PGC >= 30):
            rango = "Obesidad"

"""----------------------------------------------------------------------------
  Se printean los datos de la persona segun su sexo, su porcentaje graso y
  clasificacion realizada.
----------------------------------------------------------------------------"""

#respuesta
if (sexo == 1):
    print(f"""Rut : {rut}
Edad : {edad}
Sexo : {sex}
Medida cintura en Cms. : {cintura}
Medida cuello en Cms. : {cuello}
Altura en Cms. : {altura}
Porcentaje de Grasa : {PGC}%
Clasificacion = {rango}""")
else:
    print(f"""Rut : {rut}
Edad : {edad}
Sexo : {sex}
Medida cintura en Cms. : {cintura}
Medida cadera en Cms. : {cadera}
Medida cuello en Cms. : {cuello}
Altura en Cms. : {altura}
Porcentaje de Grasa : {PGC}%
Clasificacion = {rango}""")