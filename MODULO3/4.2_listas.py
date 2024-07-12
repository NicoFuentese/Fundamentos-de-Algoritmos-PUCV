from PIL import Image

img = Image.open("images.py/C3_4.2.png")
img.show()

#resolucion
def leerEdades():
    lista = []
    while True:
        dato = int(input())
        if dato < 0:
            break
        lista.append(dato)
    return lista

#MAIN
listaEdades = leerEdades()
print(f"""Lista Original = {listaEdades}
Largo Lista Original = {len(listaEdades)}""")

elem = int(input())
print(f"""Elemento que se elimina : {elem}""")

if elem in listaEdades:
    listaEdades.remove(elem)
    
print(f"""Lista Final = {listaEdades}
Largo Lista Final = {len(listaEdades)}""")