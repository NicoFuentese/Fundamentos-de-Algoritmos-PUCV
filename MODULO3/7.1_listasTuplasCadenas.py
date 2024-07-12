from PIL import Image

img = Image.open("images.py/C3_7.1.png")
img.show()

#resolucion
def leerDatos():
    lista = []
    while True:
        dato = input()
        if (dato == "FIN"):
            return lista
        if (dato.isdigit() == True):
            if dato not in lista:
                lista.append(dato)
    return lista
    
def hipopar (numero):
    dato = int(numero)
    if (dato == 0):
        return True
    else:
        while (dato != 0):
            digito = dato % 10
            if (digito % 2 == 0):
                return True
            dato //= 10
    return False

#main
lista = leerDatos()
print(f"lista de datos = {lista}\n")

listaHipopar = []
for caracter in lista:
    numero = int(caracter)
    if (hipopar(numero) == True):
        listaHipopar.append(numero)
listaHipopar.sort(reverse = True)
print(f"lista de hipopares - ordenado de mayor a menor = {listaHipopar}\n")

print(f"RESUMEN : Cantidad de Hipopares / Cantidad de leídos = {len(listaHipopar)} / {len(lista)}")



