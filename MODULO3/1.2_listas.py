from PIL import Image

img = Image.open("images.py/C3_1.2.png")
img.show()

#resolucion
def validar():
    lista = []
    while True:
        n = int(input())
        if n < 0:
            break
        lista.append(n)
    return lista
    
#main
lista = validar()
menor = min(lista)
mayor = max(lista)
rango = mayor - menor
print(f"El rango de edades es = {rango}")