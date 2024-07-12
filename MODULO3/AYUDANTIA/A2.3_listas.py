from PIL import Image

img = Image.open("images.py/C3_A2.3.png")
img.show()

#resolucion
def similitud (lista1, lista2):
    contador = 0
    for i in range (len(lista1)):
        if (lista1[i] == lista2[i]):
            contador += 1
    valor = contador * 100 / len(lista1)
    return valor

#main
n = int(input())
lista1 = []
lista2 = []

for i in range(0, n):
    dato = int(input())
    lista1.append(dato)

for i in range (0, n):
    dato = int(input())
    lista2.append(dato)

print(f"""cadena de bits 1 = {lista1}
cadena de bits 2 = {lista2}""")

porc = similitud(lista1, lista2)
print(f"El porcentaje de similitud es de un {porc} %")