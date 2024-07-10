from PIL import Image

img = Image.open('images.py/p1.3.png')
img.show()

#resolucion
bebidas = int(input())
jabas = int(bebidas/12)
sobrantes = int(bebidas%12)

print(f"""Cantidad de jabas = {jabas}
quedan {sobrantes} sin trasladar""")