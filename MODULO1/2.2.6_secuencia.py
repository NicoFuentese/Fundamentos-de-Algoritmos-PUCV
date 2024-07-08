from PIL import Image

img = Image.open('images.py/C2.2.5.png')
img.show()

#resolucion
real = float(input())
redondeo = int(round(real,0))
print(f"""Numero Redondeado = {redondeo}
Numero Truncado = {int(real)}""")