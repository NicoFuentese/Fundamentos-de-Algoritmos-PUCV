from PIL import Image

img = Image.open("images.py/C3_6.1.png")
img.show()

#resolucion
def leerDatos (n):
    lista = []
    for i in range (n):
        rut = input()
        nombre = input()
        edad = int(input())
        resultado = input()
        tupla = (rut, nombre, edad, resultado)
        lista.append(tupla)
    return lista

def mostrarPacientes (lista):
    print(f"""LISTADO DE PERSONAS QUE SE REALIZARON PCR
=========================================""")
    for tupla in lista:
        rut, nombre, edad, resultado = tupla
        print(f"{rut} {nombre} {edad} {resultado}")

def positivos (lista):
    contador = 0
    for tupla in lista:
        if (tupla[3] == "POSITIVO"):
            contador += 1
    return contador
    
def negativos (lista):
    contador = 0
    largo = len(lista)
    for i in range(largo):
        if lista[i][3] == "NEGATIVO":
            contador += 1
    return contador

def obtenerRutPos (listaR):
    lista = []
    for tupla in listaR:
        if tupla[3] == "POSITIVO":
            lista.append(tupla[0])
    return lista

def mostrarRut (lista):
    print("Listado Ordenado Por Rut de Personas con PCR POSITIVO")
    for rut in lista:
        print(rut)
        
def mayores (lista):
    contador = 0
    largo = len(lista)
    for i in range(largo):
        if (lista[i][3] == "POSITIVO"):
            if (lista[i][2]) >= 18:
                contador += 1
    return contador

def menores (lista):
    contador = 0
    largo = len(lista)
    for i in range (largo):
        if (lista[i][3] == "POSITIVO"):
            if (lista[i][2] < 18):
                contador += 1
    return contador

#main
pacientes = int(input())
listaPaciente = leerDatos(pacientes)
mostrarPacientes(listaPaciente)
positivos = positivos(listaPaciente)
negativos = negativos(listaPaciente)
porcPositivos = round(positivos / pacientes * 100, 1)
porcNegativos = round(negativos / pacientes * 100, 1)
print()
print(f"""REPORTE MINSAL
==============""")
print()

print(f"""El {porcPositivos} % de las personas procesadas tiene PCR POSITIVO
El {porcNegativos} % de las personas procesadas tiene PCR NEGATIVO""")
print()

if positivos == 0:
    print("NO hay personas con PCR POSITIVO.")
else:
    listaRut = obtenerRutPos(listaPaciente)
    listaRut.sort()
    mostrarRut(listaRut)
    posMayores = mayores(listaPaciente)
    posMenores = menores(listaPaciente)
    mayor = round(posMayores / positivos * 100, 1)
    menor = round(posMenores / positivos * 100, 1)
    print()
    print(f"""El {mayor} % de personas con PCR POSITIVO eran MAYORES DE EDAD.
El {menor} % de personas con PCR POSITIVO eran MENORES DE EDAD.""")