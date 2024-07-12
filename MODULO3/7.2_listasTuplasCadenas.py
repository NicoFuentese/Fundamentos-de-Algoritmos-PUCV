from PIL import Image

img = Image.open("images.py/C3_7.2.png")
img.show()

#resolucion
def leerDatos ():
    lista = []
    while True:
        lista1 = []
        for i in range(2):
            palabra = input()
            if (palabra == "FIN"):
                return lista
            lista1.append(palabra)
        lista.append(tuple(lista1))

def mostrarLista (lista):
    print(f"TOTAL PARES DE PALABRAS INGRESADAS : {len(lista)}\n")
    print("LISTA DE PARES DE PALABRAS INGRESADAS\n")
    for tupla in lista:
        print(tupla)

def mostrarParesMayus (lista):
    print("LISTA DE PARES DE PALABRAS EN MAYUSCULAS\n")
    for tupla in lista:
        cadena1, cadena2 = tupla
        print(tuple([cadena1.upper(), cadena2.upper()]))

def listaMayus (lista):
    listaMayus = []
    for tupla in lista:
        cadena1, cadena2 = tupla
        listaMayus.append(tuple([cadena1.upper(), cadena2.upper()]))
    return listaMayus

def anagrama (lista):
    contador = 0
    for tupla in listaMayus(lista):
        cadena1, cadena2 = tupla
        if (sorted(cadena1) == sorted(cadena2)):
            contador += 1
    return contador

def mostrarAnagrama (lista):
    contador = anagrama(lista)
    if (contador != 0):
        print(f"TOTAL DE ANAGRAMAS ENCONTRADOS {contador}\n")
        print("LISTA DE ANAGRAMAS ENCONTRADOS\n")
        for tupla in listaMayus(lista):
            cadena1, cadena2 = tupla
            if (sorted(cadena1) == sorted(cadena2)):
                print(tupla)
    else:
        print("NO SE ENCONTRARON ANAGRAMAS EN LA LISTA!")
#main

lista = leerDatos()
mostrarLista(lista)
print()
mostrarParesMayus (lista)
print()
mostrarAnagrama(lista)
