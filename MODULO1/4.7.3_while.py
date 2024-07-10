from PIL import Image

img = Image.open("images.py/C4.7.3.png")
img.show()

#resolucion
casoPrueba = 1
while True:
    ancho = int(input())
    if (ancho == 0 ):
        break
    alto = int(input())
    
    cant_losetas = ancho * alto
    cant_oscuras = cant_losetas // 2
    
    if cant_losetas% 2 == 0:
        cant_claras = cant_oscuras
    else:
        cant_claras = cant_oscuras + 1
    print(f"CASO {casoPrueba} --> Total Losetas = {cant_losetas} --> Losetas Claras : {cant_claras} , Losetas Oscuras : {cant_oscuras}")
    casoPrueba += 1