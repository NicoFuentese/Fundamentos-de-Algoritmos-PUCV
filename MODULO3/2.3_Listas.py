from PIL import Image

img = Image.open("images.py/C3_2.3.png")
img.show()

#resolucion
#Este ejercicio tenia un error de calculo
from math import exp
from math import trunc

def PoblacionFinal (poblacionInicial, tasaRep, meses):
    valor = trunc(poblacionInicial * (1 + tasaRep) ** meses)
    return valor

#main
n = int(input())
m = int(input())
listaNombre = []
listaPob = []
listaRep = []
listaPF = []

for i in range (0, m):
    listaNombre.append(input())
    listaPob.append(int(input()))
    listaRep.append(float(input()))
    valor = PoblacionFinal(listaPob[i], listaRep[i], n)
    listaPF.append(valor)
    print(f"""ESPECIE {listaNombre[i]} - TASA DE REPRODUCCIÓN MENSUAL = {listaRep[i]}
POBLACIÓN INICIAL = {listaPob[i]} - POBLACION FINAL MES {n} = {listaPF[i]}
PORCENTAJE DE AUMENTO DE LA POBLACIÓN EN {n} MES(ES) = {round((listaPF[i] - listaPob[i]) / listaPob[i] * 100, 1)}%
""")

    