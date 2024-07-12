from PIL import Image

img = Image.open("images.py/C3_3.7.png")
img.show()

#resolucion
#main
n = int(input())
print(f"En el concurso participaron {n} equipos.\n")

globos = int(input())
lista = []
for i in range(globos):
    equipo = int(input())
    color = input()
    lista.append([equipo,color])

listadoFinal = []
print(f"""GLOBOS POR EQUIPO
=================\n""")
for j in range(1, n + 1):
    contadorGlobos = 0
    for globosDados in lista:
        if (globosDados[0] == j):
            contadorGlobos += 1
    print(f"Equipo {j} --> {contadorGlobos} Globo(s).")
    listadoFinal.append([j, contadorGlobos])

maxGlobos = 0
equipos = []
for cadaEquipo in listadoFinal:
    if (cadaEquipo[1] > maxGlobos):
        maxGlobos = cadaEquipo[1]
        equipos.clear()
        equipos.append(cadaEquipo[0])
    elif (cadaEquipo[1] == maxGlobos):
        equipos.append(cadaEquipo[0])

print()
if (len(equipos) == 1):
    print(f"El equipo ganador del concurso fue el Nº {equipos[0]}.")
else:
    print("HUBO EMPATE EN EL CONCURSO.")



