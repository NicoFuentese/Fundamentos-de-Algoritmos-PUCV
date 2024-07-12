from PIL import Image

img = Image.open("images.py/C3_5.4.png")
img.show()

#resolucion
def leerCoef (n):
    lista = []
    for i in range(n):
        dato = int(input())
        lista.append(dato)
    return lista

def polinomio (coef, x):
    contador = 0
    suma = 0
    for i in range(len(coef)):
        suma += coef[i] * x ** (i)
        contador += 1
    return suma
#main

n = int(input())
coef = leerCoef (n)
x = int(input())

valor = float(polinomio(coef, x))
print(f"Para X = {float(x)} el polinomio evaluado es igual a {valor}")