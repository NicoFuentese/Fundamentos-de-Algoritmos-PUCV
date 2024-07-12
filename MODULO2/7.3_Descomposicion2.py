from PIL import Image

img = Image.open("images.py/C2_7.3.png")
img.show()

#resolucion
def esSuertudo (numero):
    while numero != 0:
        digito = numero % 10
        if digito == 7:
            return True
        numero //= 10
    return False
    
def mostrarSuertudos (a, b):
    contador = 0
    for i in range (a, b + 1):
        if esSuertudo (i):
            if contador == 0:
                print(f"NÚMEROS SUERTUDOS EN EL INTERVALO {a} .. {b} = {i}", end = " ")
            else:
                print(f"{i}", end = " ")
            contador += 1
    if contador == 0:
        print("NO HAY NÚMEROS SUERTUDOS EN EL INTERVALO")