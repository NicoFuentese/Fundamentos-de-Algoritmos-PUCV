from PIL import Image

img = Image.open("images.py/C3_6.2.png")
img.show()

#resolucion
def leerDatos ():
    lista2 = []
    while True:
        lista1 = []
        rut = input()
        if (rut == "0-0"):
            break
        lista1.append(rut)
        nombre = input()
        lista1.append(nombre)
        altura = float(input())
        lista1.append(altura)
        peso = int(input())
        lista1.append(peso)
        lista2.append(tuple(lista1))
    return lista2
    
def mostrarLista(lista):
    print("""Contenido Lista de Tuplas - Datos Pacientes
==============================================""")
    for tupla in lista:
        print(tupla)

def imc (lista):
    listaNueva2 = []
    for tupla in lista:
        listaNueva = []
        listaNueva.append(tupla[0])
        listaNueva.append(tupla[1])
        IMC = round(tupla[3] / (tupla[2] ** 2), 2)
        listaNueva.append(IMC)
        listaNueva2.append(tuple(listaNueva))
    return listaNueva2

def mostrarListaIMC(lista):
    print("""Contenido Lista de Tuplas - IMC Pacientes
==============================================""")
    for tupla in lista:
        print(tupla)

def obesidad (lista):
    listaNombres = []
    contador = 0
    for tupla in lista:
        if (tupla[2] >= 30):
            listaNombres.append(tupla[1])
            contador += 1
    return sorted(listaNombres), contador

#main
lista = leerDatos()
largo = len(lista)
mostrarLista(lista)
listaIMC = imc(lista)
print()
mostrarListaIMC(listaIMC)

obesos = list(obesidad(listaIMC))
print()
if (obesos[1] > 0):
    porc = round(obesos[1] / largo * 100, 1)
    print(f"""REPORTE PACIENTES CON OBESIDAD
==============================
Pacientes con Obesidad : {obesos[1]} persona(s) = {porc} %.
Lista de Pacientes con Obesidad Ordenadas Alfabéticamente  = {obesos[0]}""")
else:
    print("""REPORTE PACIENTES CON OBESIDAD
==============================
Pacientes con Obesidad : NO HAY""")
