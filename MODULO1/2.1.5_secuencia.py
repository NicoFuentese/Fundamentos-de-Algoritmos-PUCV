from PIL import Image

img = Image.open('images.py/C2.5.png')
img.show()

#resolucion
alto = int(input())
ancho = int(input())
manos = int(input())
rinde = int(input())

superficie = alto*ancho

print(f"Superficie Pared = {superficie} m2")
print(f"Manos de Pintura = {manos}")
print(f"Metros Cuadrados por Litro de Pintura = {rinde}")

tarros = superficie/rinde*manos
print(f"Humberto necesitas comprar {tarros} litro(s) de pintura")