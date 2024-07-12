from PIL import Image

img = Image.open("images.py/C2_5.3.png")
img.show()

#resolucion
def sumaDigitos (numero):
    suma = 0
    while (numero > 0):
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

# main
n = int(input())
print(f"La suma de los dígitos del número {n} es {sumaDigitos(n)}")