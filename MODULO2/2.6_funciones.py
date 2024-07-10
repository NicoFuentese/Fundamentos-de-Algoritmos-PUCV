from PIL import Image

img = Image.open("images.py/c2_2.6.png")
img.show()

#resolucion
def esDeficiente (n):
    suma = 0
    for i in range (1, n):
        if (n % i == 0):
            suma += i
    if (suma < n):
        return True
    else:
        return False

def deficientesEnIntervalo (a , b):
    print(f"Deficientes en intervalo entre {a} y {b} : ", end = "")
    contador = 0
    for i in range (a, b + 1):
        if (esDeficiente(i) == True):
            print(i, end = " ")
            contador += 1
    if (contador == 0):
        print("NO HAY")