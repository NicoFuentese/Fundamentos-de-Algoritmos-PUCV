from PIL import Image

img = Image.open("images.py/C3_A6.2.png")
img.show()

#resolucion
def poblarCadenas():
    listaCadenas = []
    while True:
        cadena = input()
        if (cadena == "FIN"):
            return listaCadenas
        if (not cadena.isdigit()):
            continue
        if (int(cadena) <= 0):
            continue
        if (cadena in listaCadenas):
            continue
        listaCadenas.append(cadena)

def mostrarCadenas (listaCadenas):
    print(f"LISTA INICIAL DE CADENAS = {listaCadenas}")
    print(f"TOTAL ELEMENTOS EN LISTA INICIAL DE CADENAS = {len(listaCadenas)}")

def convertirNumeros (listaCadenas):
    listaNumeros = []
    for cadena in listaCadenas:
        listaNumeros.append(int(cadena))
    listaNumeros.sort()
    print(f"LISTA NUMEROS EN ORDEN CRECIENTE = {listaNumeros}")
    return listaNumeros

def calcularSumaDigitos (numero, largo):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += (digito) ** largo
        numero //= 10
    return suma

def obtenerTuplas (listaNumeros):
    listaDeTuplas = []
    for numero in listaNumeros:
        largo = len(str(numero))
        sumaDigitosElevado = calcularSumaDigitos (numero, largo)
        tupla = (numero, largo, sumaDigitosElevado)
        listaDeTuplas.append(tupla)
    print(f"LISTA TUPLAS = {listaDeTuplas}")
    return listaDeTuplas

def verificarNarcisismo (listaDeTuplas):
    listaNarcisismo = []
    for tupla in listaDeTuplas:
        if (tupla[0] == tupla[2]):
            listaNarcisismo.append(tupla[0])
    if (listaNarcisismo == []):
        print(f"NO SE ENCONTRARON NÚMEROS N-NARCISISTAS EN LA LISTA")
        return
        
    print(f"LISTA DE NÚMEROS N-NARCISISTAS = {listaNarcisismo}")
    print(f"TOTAL ELEMENTOS EN LISTA DE NÚMEROS N-NARCISISTAS = {len(listaNarcisismo)}")
    print(f"--- GRAN NARCISISMO ---")

#main
listaCadenas = poblarCadenas()
if (listaCadenas == []):
    print("LISTA INICIAL DE CADENAS VACIA")
else:
    mostrarCadenas(listaCadenas)
    listaNumeros = convertirNumeros (listaCadenas)
    listaDeTuplas = obtenerTuplas (listaNumeros)
    verificarNarcisismo(listaDeTuplas)
