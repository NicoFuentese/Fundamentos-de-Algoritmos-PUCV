from PIL import Image

img = Image.open("images.py/C3_3.2.png")
img.show()

#resolucion
def leerDatos():
    lista = []
    while True:
        voto = input()
        if (voto == "FIN"):
            return lista
        lista.append(voto)

def binario (lista):
    listaNueva = []
    for voto in lista:
        if (voto == "RECHAZO"):
            votoNuevo = 0
        else:
            votoNuevo = 1
        listaNueva.append(votoNuevo)
    return listaNueva

def conteo (lista):
    rechazo = 0
    apruebo = 0
    for numero in lista:
        if (numero == 0):
            rechazo += 1
        else:
            apruebo += 1
    return rechazo, apruebo

#main
lista = leerDatos()
print(f"En total votaron {len(lista)} convencionales en el pleno.")
listaBinaria = binario(lista)
print(f"La lista de votos fue = {listaBinaria}.\n")

rechazos, apruebos = conteo(listaBinaria)
print(f"""Total de votos APRUEBO = {apruebos}.
Total de votos RECHAZO = {rechazos}.\n""")

#apruebos >= 2/3 del quorum --> aprobada
#si alcanza la mayoria simple vuelvo a comision
#si apruebos no alcanza la mayoria simple es rechazada

if (apruebos / len(lista) >= 2/3):
    print(f"La norma es aprobada con {apruebos} de {len(lista)} votos.")
    if (apruebos == len(lista)):
        print("LA APROBACIÓN FUE UNÁNIME!.")
elif (apruebos > rechazos) and (apruebos / len(lista) < 2/3):
    print("La norma regresa a la comisión de origen para ser reformulada.")
else:
    print("La norma es rechazada definitivamente.")
    if (rechazos == len(lista)):
        print("EL RECHAZO FUE UNÁNIME!.")