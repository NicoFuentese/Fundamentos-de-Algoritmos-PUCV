from PIL import Image

img = Image.open("images.py/C2_1.4.png")
img.show()

#resolucion
def dibujaTriangulo (caracter, lado):
    for linea in range (1, lado + 1):
        for espacio in range (1, lado - linea + 1):
            print (" ", end = "")
        for car in range (1, linea + 1):
            print(f"{caracter}", end = " ")
        print()