from PIL import Image

img = Image.open("images.py/C3_8.1.png")
img.show()

#resolucion
def leerDatos ():
    listaFinal = []
    while True:
        lista = []
        titulo = input()
        if (titulo == "FINAL"):
            return listaFinal
        horas = int(input())
        minutos = int(input())
        segundos = int(input())
        visualizaciones = int(input())
        lista.append(titulo)
        lista.append(horas)
        lista.append(minutos)
        lista.append(segundos)
        lista.append(visualizaciones)
        listaFinal.append(tuple(lista))
    return listaFinal

def datosVideos(lista):
    print("""DATOS VIDEOS
------------""")
    for tupla in lista:
        print(f"TITULO : {tupla[0].upper()} - DURACION {tupla[1]}:{tupla[2]}:{tupla[3]} - VISTAS : {tupla[4]}")
    print()

def tiempoTotal (lista):
    horas = 0
    minutos = 0
    segundos = 0
    for tupla in lista:
        segundos += tupla[3]
        if (segundos >= 60):
            minutosExtra = segundos // 60
            minutos += minutosExtra
            segundos = segundos % 60
        minutos += tupla[2]
        if (minutos >= 60):
            horasExtra = minutos // 60
            horas += horasExtra
            minutos = minutos % 60
        horas += tupla[1]
    print(f"TIEMPO TOTAL DE TODOS LOS VIDEOS {horas}:{minutos}:{segundos}\n")
    
def promedioVisitas (lista):
    vistas = 0
    for tupla in lista:
        vistas += tupla[4]
    prom = round(vistas / len(lista), 1)
    print(f"PROMEDIO DE VISTAS DE TODOS LOS VIDEOS = {prom}\n")

def menorDuracionSeg (lista):
    menor = 0
    listaVideo = []
    for tupla in lista:
        segundos = tupla[1] * 60 * 60 + tupla[2] * 60 + tupla[3]
        if (menor == 0):
            menor = segundos
            listaVideo.append(tupla)
        elif (segundos < menor):
            menor = segundos
            listaVideo.clear()
            listaVideo.append(tupla)
        elif (segundos == menor):
            listaVideo.append(tupla)
    print(f"MENOR DURACIÓN EN SEGUNDOS = {menor}\n")
    return menor, listaVideo
        
def tituloVideo (lista):
    print(f"""TÍTULO(S) VIDEO(S) + VISTAS CON MENOR DURACIÓN EN SEGUNDOS
----------------------------------------------------------""")
    for tupla in lista:
        print(f"* {tupla[0].upper()} - {tupla[4]} VISTAS")
    print()
    
def masMil (lista):
    contador = 0
    listaMasMil = []
    for tupla in lista:
        if (tupla[4] > 1000):
            contador += 1
            listaMasMil.append(tupla[0].upper())
    if (contador == 0):
        print("NO HAY VIDEOS CON MÁS DE 1000 VISUALIZACIONES")
    else:
        listaMasMil.sort()
        print("""LISTA DE VIDEOS CON MÁS DE 1000 VISTAS ORDENADOS ALFABÉTICAMENTE
----------------------------------------------------------------""")
        for nombre in listaMasMil:
            print(f"{nombre}")

#main
tuplas = leerDatos ()
print(f"TOTAL VIDEOS LEÍDOS = {len(tuplas)}\n")
datosVideos(tuplas)
tiempoTotal (tuplas)
promedioVisitas(tuplas)
menor, listaVideo = menorDuracionSeg(tuplas)
tituloVideo(listaVideo)
masMil (tuplas)