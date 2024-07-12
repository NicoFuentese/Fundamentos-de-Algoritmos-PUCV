from PIL import Image

img = Image.open("images.py/C3_3.5.png")
img.show()

#resolucion
prueba = 0
while True:
    n = int(input())
    if (n == 0):
        break
    prueba += 1
    lista = []
    for i in range (n):
        km = int(input())
        lista.append(km)
    print(f"""=====================
CASO DE PRUEBA {prueba}
=====================
Lista de distancias de c/etapa de la ruta = {lista}""")
    listaKmT = []
    while (len(lista) != 0):
        kms = sum(lista)
        listaKmT.append(kms)
        lista.remove(lista[0])
    print(f"""Lista de distancias por recorrer desde el comienzo
de c/etapa hasta el final de la ruta = {listaKmT}\n""")