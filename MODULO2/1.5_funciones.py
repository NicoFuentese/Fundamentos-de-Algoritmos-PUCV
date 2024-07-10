from PIL import Image

img = Image.open("images.py/C2_1.5.png")
img.show()

#resolucion
def puntaje():
    while True:
        punt = int(input())
        if (2 <= punt <= 12):
            return punt

def combinaciones(p):
    print(f"Combinaciones para suma de puntaje = {p}")
    print("Dado 1 - Dado 2")
    contador_combis = 0
    for i in range (1, 7):
        for j in range (1, 7):
            suma = j + i
            if (suma == p):
                contador_combis += 1
                print(f"   {i}   -   {j}")
    print(f"Total Combinaciones = {contador_combis}")
