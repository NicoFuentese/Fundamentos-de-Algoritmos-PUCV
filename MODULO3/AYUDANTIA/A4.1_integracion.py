from PIL import Image

img = Image.open("images.py/C3_A4.1.png")
img.show()

#resolucion
# ---------- POBLAR DATOS ---------- #
def poblarLista():
    lista = []
    while True:
        cadena = input()
        if cadena == "FIN":
            print(f"datos ingresados = {lista}\n")
            return lista

        if cadena not in lista:
            lista.append(cadena)
# ---------- POBLAR DATOS ---------- #

# ---------- ES ORDENADO ---------- #
def esOrdenado(cadena):
    lista = list(cadena)
    copiaOrdenada = lista.copy()
    copiaOrdenada.sort()
    return lista == copiaOrdenada


# ---------- ES ORDENADO ---------- #

# ---------- PROCESAR DATOS ---------- #
def procesarDatos(lista):
    listaOrd = []
    listaNoOrd = []
    for cadena in lista:
        if esOrdenado(cadena):
            listaOrd.append(int(cadena))
        else:
            listaNoOrd.append(int(cadena))

    listaOrd.sort()
    listaNoOrd.sort()

    print(f"lista de    ORDENADOS - (de menor a mayor) = {listaOrd}")
    print(f"lista de NO ORDENADOS - (de menor a mayor) = {listaNoOrd}\n")

    return listaOrd, listaNoOrd
# ---------- PROCESAR DATOS ---------- #

# ---------- RESUMEN ---------- #
def resumen(listaOrdenados, listaNoOrdenados):
    print("RESUMEN")
    print(f"Cantidad    Total     = {len(listaOrdenados) + len(listaNoOrdenados)}")
    print(f"Cantidad    Ordenados = {len(listaOrdenados)}")
    print(f"Cantidad NO Ordenados = {len(listaNoOrdenados)}")
# ---------- RESUMEN ---------- #

# ---------- MAIN ---------- #
lista = poblarLista()
listaOrdenados, listaNoOrdenados = procesarDatos(lista)
resumen(listaOrdenados, listaNoOrdenados)
# ---------- MAIN ---------- #