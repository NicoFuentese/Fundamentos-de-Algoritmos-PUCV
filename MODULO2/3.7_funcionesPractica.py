from PIL import Image

img = Image.open("images.py/C2_3.7.png")
img.show()

#resolucion
def mostrarSerieAlternada (numero):
    valor = 1
    for i in range (1, n + 1):
        if ( i == 1):
            valor = valor
        elif ( i % 2 == 0):
            valor *= 4
        else: 
            valor = int(valor / 2)
        
        if ( i != n):
            print(valor, end = ", ")
        else:
            print(valor)
    