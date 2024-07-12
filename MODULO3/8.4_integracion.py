from PIL import Image

img = Image.open("images.py/C3_8.4.png")
img.show()

#resolucion
def suertudo (numero):
    while (numero != 0):
        digito = numero % 10
        if (digito == 7):
            return True
        numero //= 10
    return False

#main
lista = []
while True:
    dato = input()
    if (dato == "FIN"):
        break
    lista.append(dato)
print(f"listado de datos = {lista}\n")

listaSuertudo = []
for numero in lista:
    if (suertudo(int(numero)) == True):
        listaSuertudo.append(numero)

if (len(listaSuertudo) == 0):
    print("listado de suertudos = NO HAY")
else:
    print(f"listado de suertudos = {listaSuertudo}")
print()

porc = round(len(listaSuertudo) / len(lista) * 100, 1)
print(f"porcentaje de suertudos = {porc} %")
