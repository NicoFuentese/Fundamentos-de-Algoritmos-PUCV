from PIL import Image

img = Image.open("images.py/C3_8.2.png")
img.show()

#resolucion
def validar ():
    while True:
        n = int(input())
        if (n > 0):
            return n

def leerDatos (n):
    lista = []
    for i in range (n):
        nombre = input()
        personaje = input()
        mundo = int(input())
        nivel = int(input())
        monedas = int(input())
        lista.append(tuple([nombre, personaje, mundo, nivel, monedas]))
    return lista
        
def mostrar (lista):
    print("""LISTA DE PARTIDAS
-----------------""")
    for tupla in lista:
        print(tupla)
    print()

def masMonedas (lista):
    mayor = 0
    for tupla in lista:
        if (mayor == 0):
            mayor = tupla[4]
        elif (mayor < tupla[4]):
            mayor = tupla[4]
    print(f"LA MAYOR CANTIDAD DE MONEDAS FUE {mayor}")
    return mayor

def MejoresJugadores (lista, mayor):
    listaNombres = []
    print(f"""JUGADOR(ES) QUE RECOLECTARON MAYOR CANTIDAD DE MONEDAS
------------------------------------------------------""")
    for tupla in lista:
        if (tupla[4] == mayor):
            listaNombres.append(tupla[0])
            print(tupla[0])
    print()
    
def MasUsado (lista):
    mario = 0
    luigi = 0
    toad = 0
    barbie = 0
    listaP = []
    mayor = 0
    personajes = []
    for tupla in lista:
        listaP.append(tupla[1])
    for personaje in listaP:
        if (mayor == 0):
            mayor = listaP.count(personaje)
            personajes.append(personaje)
        elif (mayor < listaP.count(personaje)):
            mayor = listaP.count(personaje)
            personajes.clear()
            personajes.append(personaje)
        elif (mayor == listaP.count(personaje)) and (personaje not in personajes):
            personajes.append(personaje)
    print(f"PERSONAJE(S) MÁS USADO(S) = {personajes}\n")
    """for tupla in lista:
        if (tupla[1] == "MARIO"):
            mario += 1
        elif (tupla[1] == "LUIGI"):
            luigi += 1
        elif (tupla[1] == "TOAD"):
            toad += 1
        elif (tupla[1] == "BARBIE"):
            barbie += 1
    listaP.append(tuple(["MARIO", mario]))
    listaP.append(tuple(["LUIGI", luigi]))
    listaP.append(tuple(["BARBIE", barbie]))
    listaP.append(tuple(["TOAD", toad]))
    for tupla in listaP:
        if (mayor == 0):
            mayor = tupla[1]
        elif (mayor < tupla[1]):
            mayor = tupla[1]
    for tupla in listaP:
        if mayor in tupla:
            personajes.append(tupla[0])
    print(f"PERSONAJE(S) MÁS USADO(S) = {personajes}\n")"""
            
def mundoMasJugado (lista):
    mayor = 0
    listaMundos = []
    MundosRepetidos = []
    for tupla in lista:
        listaMundos.append(tupla[2])
    for mundo in listaMundos:
        if (listaMundos.count(mundo) > mayor):
            mayor = listaMundos.count(mundo)
            MundosRepetidos.clear()
            MundosRepetidos.append(mundo)
        elif (mayor == 0):
            mayor = listaMundos.count(mundo)
            MundosRepetidos.append(mundo)
        elif (listaMundos.count(mundo) == mayor) and (mundo not in MundosRepetidos):
            MundosRepetidos.append(mundo)
    MundosRepetidos.sort()
    print(f"MUNDO(S) MÁS JUGADO(S) = {MundosRepetidos}")

#main
n = validar()
lista = leerDatos(n)
mostrar(lista)
mayor = masMonedas (lista)
MejoresJugadores (lista, mayor)
MasUsado (lista)
mundoMasJugado (lista)
