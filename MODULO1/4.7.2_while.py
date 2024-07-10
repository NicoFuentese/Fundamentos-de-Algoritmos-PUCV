from PIL import Image

img = Image.open("images.py/C4.7.2.png")
img.show()

#resolucion
caso = 0
while True:
    caso += 1
    n = int(input())
    if (n <= 0):
        break
    m = int(input())
    r = int(input())
    if (r // (n * m) == 0):
        necesito = 1
    elif (r // (n * m) == 1) and (r % (n * m) == 0):
        necesito = 1
    elif (r // (n * m) == 1) and (r % (n * m) != 0):
        necesito = 2
    elif (r // (n * m) != 1) and (r % (n * m) == 0):
        necesito = r // (n * m)
    elif (r // (n * m) != 1) and (r % (n * m) != 0):
        necesito = r // (n * m) + 1
    print(f"""CASO {caso} :
Una tableta de chocolate tiene {n} x {m} = {n * m} cuadrados.
Necesitas {r} cuadrados para la tarta Sacher.
Debes comprar como mínimo {necesito} tableta(s) de chocolate.\n""")