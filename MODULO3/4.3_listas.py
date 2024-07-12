from PIL import Image

img = Image.open("images.py/C3_4.3.png")
img.show()

#resolucion
def leerEdades(n):
    lista = []
    for i in range (n):
        dato = int(input())
        lista.append(dato)
    return lista

#main
n = int(input())
lista = leerEdades(n)
print(f"""Lista Original = {lista}
Largo Lista Original = {len(lista)}""")

elim = int(input())
print(f"Elemento que se elimina : {elim}")

contador = 0
if elim in lista:
    while elim in lista:
        lista.remove(elim)
        contador += 1

print(f"""Se eliminaron {contador} ocurrencia(s) de la edad {elim}
Lista Final = {lista}
Largo Lista Final = {len(lista)}""")

