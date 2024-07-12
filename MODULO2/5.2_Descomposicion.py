from PIL import Image

img = Image.open("images.py/C2_5.2.png")
img.show()

#resolucion
def largo (numero):
    contador = 1
    while ( numero // 10 != 0):
        contador += 1
        numero = numero // 10
    return contador

#main
n = int(input())
print(f"El largo de {n} es {largo(n)}")