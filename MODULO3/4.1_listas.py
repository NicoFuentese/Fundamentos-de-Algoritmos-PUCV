from PIL import Image

img = Image.open("images.py/C3_4.1.png")
img.show()

#resolucion
def leerEdades(n):
    lista = []
    for i in range(n):
        edad = int(input())
        lista.append(edad)
    return lista




#main
#diseño incremental
#aparece una funcion y la defino de inmediato
n = int(input()) #leer total de edades
listaEdades = leerEdades(n)
print(f"Lista Edades = {listaEdades}")

edadBusc = int(input())
if edadBusc in listaEdades:
    pos = listaEdades.index(edadBusc)
    print(f"edad = {edadBusc} se encontró en la lista por primera vez en posición {pos}")
else:
    print(f"edad = {edadBusc} NO se encontró en la lista!")