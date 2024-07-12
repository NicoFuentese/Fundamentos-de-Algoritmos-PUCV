from PIL import Image

img = Image.open("images.py/C3_8.3.png")
img.show()

#resolucion
def leerDatos (n):
    lista = []
    for i in range(n):
        dato = input()
        lista.append(dato)
    print("Lista inicial es:")
    print(lista)
    print()
    return lista

def paritoso (numero):
    lista = []
    while (numero != 0):
        digito = numero % 10
        if (digito % 2 != 0):
            return False
        numero //= 10
    return True

def listaParitoso (lista):
    listaNueva = []
    for numero in lista:
        if (paritoso(int(numero)) == True):
            listaNueva.append(int(numero))
    listaNueva.sort()
    print("Lista de Paritosos es:")
    print(listaNueva)
    print()
    return listaNueva

#main
n = int(input())
lista = leerDatos(n)
listaParitoso = listaParitoso (lista)
porc = round(len(listaParitoso) / len(lista) * 100, 1)
print(f"Porcentaje de Paritosos es: {porc} %")
