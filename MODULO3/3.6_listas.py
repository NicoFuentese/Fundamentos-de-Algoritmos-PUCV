from PIL import Image

img = Image.open("images.py/C3_3.6.png")
img.show()

#resolucion
def leerDatos(n):
    lista = []
    for i in range(n):
        dato = int(input())
        lista.append(dato)
    return lista



def turnos (cartas, lista, orden):
    primero = []
    segundo = []
    if (cartas % 2 == 0):
        numeroTurnos = cartas // 2
    else:
        numeroTurnos = cartas // 2 + 1
    for turno in range (1, numeroTurnos + 1):
        print(f"******************** Turno Nº {turno} ********************\n")
        for sacador in orden:
            if (lista[0] > lista[-1]):
                saca = lista[0]
                lista.remove(saca)
            else:
                saca = lista[-1]
                lista.remove(saca)
                
            if (sacador == orden[0]):
                primero.append(saca)
            elif (sacador == orden[1]):
                segundo.append(saca)
                
            print(f"""{sacador} tomó la carta = {saca}.
Estado PARCIAL de cartas en la FILA = {lista}.\n""")
            if (len(lista) == 0):
                break
    return primero, segundo

def resultados (lista1, lista2, orden):
    lista = [lista1, lista2]
    print("******************** FIN DEL JUEGO y RESULTADO FINAL ********************\n")
    puntajeGanador = [0,0]
    for sacador in range(len(orden)):
        puntos = sum(lista[sacador])
        print(f"""{orden[sacador]} acumuló las siguientes cartas = {lista[sacador]}
Su puntaje FINAL es {puntos}.\n""")
        if (puntos > puntajeGanador[0]):
            puntajeGanador[0] = puntos
            puntajeGanador[1] = orden[sacador]
    print(f"GANADORA/GANADOR es {puntajeGanador[1]}")
        
    

#main

primero = input()
segundo = input()
orden = [primero, segundo]
cartas = int(input())
numeros= leerDatos(cartas)
print(f"Estado INICIAL de cartas en la FILA = {numeros}.\n")
lista1, lista2 = turnos(cartas, numeros, orden)

pg = resultados(lista1, lista2, orden)
