from PIL import Image

img = Image.open("images.py/C3_8.5.png")
img.show()

#resolucion
def leerDatos ():
    lista = []
    while True:
        cadena = input()
        if (cadena == "FIN"):
            break
        if (cadena.isdigit() == True):
            if (int(cadena) > 0):
                if (int(cadena) not in lista):
                    lista.append(int(cadena))
    return lista

def abundante (numero):
    suma = 0
    for i in range (1, numero):
        if (numero % i == 0):
            suma += i
    if (suma > numero):
        return True
    else:
        return False

def divisorAbundante (numero):
    suma = 0
    for i in range (1, numero):
        if (numero % i == 0):
            suma += i
    tupla = (numero, suma)
    return tupla

def listaAbundantes (lista):
    listaNueva = []
    for numero in lista:
        listaNueva.append(divisorAbundante(numero))
    return listaNueva

#main
lista = leerDatos ()
if (len(lista) != 0):
    print(f"LISTA INICIAL = {lista}")
    print(f"TOTAL ELEMENTOS EN LISTA INICIAL = {len(lista)}")
    lista.sort(reverse = True)
    print(f"LISTA INICIAL ORDENADA DECRECIENTE = {lista}")
    print(f"LISTA TUPLAS = {listaAbundantes(lista)}")
    listaAbundantes = []
    for numero in lista:
        if (abundante(numero) == True):
            listaAbundantes.append(numero)
    if (len(listaAbundantes) == 0):
        print("NO SE ENCONTRARON NÚMEROS ABUNDANTES EN LA LISTA")
    else:
        print(f"LISTA DE NÚMEROS ABUNDANTES = {listaAbundantes}")
        print(f"TOTAL ELEMENTOS EN LISTA DE NÚMEROS ABUNDANTES = {len(listaAbundantes)}")
        print(f"--- GRAN ABUNDANCIA ---")
            
else:
    print("LISTA INICIAL VACIA")