from PIL import Image

img = Image.open("images.py/C2_8.1.png")
img.show()

#resolucion
def esAntiEcliptico (numero):
    while numero != 0:
        digito = numero % 10
        if (digito == 2) or (digito == 7):
            return False
        numero //= 10
    return True
    
def contarAntiEclipticosEnIntervalo (a, b):
    contador = 0
    for i in range (a, b+ 1):
        if esAntiEcliptico(i):
            contador += 1
    if contador == 0:
        print(f"Total de AntiEclipticos en el intervalo [ {a} .. {b} ] = NO HAY")
    else:
        print(f"Total de AntiEclipticos en el intervalo [ {a} .. {b} ] = {contador}")