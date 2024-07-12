from PIL import Image

img = Image.open("images.py/C3_3.3.png")
img.show()

#resolucion
def leerDatos ():
    listaNumeros = []
    out = 0
    contador = 0
    while True:
        if (out == 6):
            return listaNumeros, contador
        dato = int(input())
        contador += 1
        if (dato not in listaNumeros) and (dato >= 1) and (dato <= 41):
            listaNumeros.append(dato)
            print(f"SE AGREGÓ UN NÚMERO VÁLIDO! --> LISTA PARCIAL {listaNumeros}.")
            out += 1
    

#main
lista, personas = leerDatos()
print(f"\nFELICIDADES SE COMPLETARON LOS 6 NÚMEROS --> LISTA FINAL {lista}.")
print(f"EL TOTAL DE PERSONAS ENCUESTADAS FUE : {personas}.\n")
print(f"ESTOS SON LOS NÚMEROS QUE DEBES JUGAR ORDENADOS = {sorted(lista)}.")