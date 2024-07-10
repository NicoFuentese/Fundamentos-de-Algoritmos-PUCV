from PIL import Image

img = Image.open('images.py/p3.1.png')
img.show()

#resolucion
n = int(input())

contador = 0
while (contador <= n):
    if (contador % 3 == 0 or contador % 7 == 0 or contador == 0):
        contador += 1
    else:
        print(contador, end = " ")
        contador += 1

"""
numero = int(input())

for cadaNumero in range(1, numero + 1):
    if (cadanumero % 3 == 0 and (cadanumero % 7 == 0)):
    print(cadanumero, end = " ")
    
"""