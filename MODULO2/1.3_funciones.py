from PIL import Image

img = Image.open("images.py/C2_1.3.png")
img.show()

#resolucion
def muestraImpares(a , b):
    contador = 0
    print(f"Impares en el intervalo [ {a} .. {b} ] = ", end = "")
    for i in range (a, b + 1):
        if (i % 2 != 0):
            contador += 1
            print(i, end = " ")
        
        if (contador == 0 and i == b):
            print( "NO HAY !")
        