from PIL import Image

img = Image.open('images.py/C3.2.3.png')
img.show()

#resolucion
t = float(input())

if t < 20:
        color = "AZUL"
        print(color)
elif t >= 20 and t < 35:
        color = "AMARILLO"
        print(color)

else:
        color = "ROJO"
        print(color)
