from PIL import Image

img = Image.open("images.py/C2_9.5.png")
img.show()

#resolucion
def sucesionPadovan (n):
    p1 = 1
    p2 = 1
    p3 = 1
    aux = 1
    for i in range(1, n + 1):
        if (i > 3):
            aux = p1 + p2
            p1 = p2
            p2 = p3
            p3 = aux
        if (i != n):
            print(aux, end = ", ")
        else:
            print(aux, end ="")
    print(".")