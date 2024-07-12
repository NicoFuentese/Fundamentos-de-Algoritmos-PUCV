from PIL import Image

img = Image.open("images.py/C2_7.1.png")
img.show()

#resolucion
def esHipopar (numero):
    while numero != 0:
        digito = numero % 10
        if digito % 2 == 0:
            print(f"El dígito {digito} es par, ", end = "")
            return True
        numero //= 10
    print("NO se encontraron dígitos pares, ", end = "")
    return False
    
def leerValidar ():
    while True:
        numero = int(input())
        if (numero > 0):
            break
    return numero