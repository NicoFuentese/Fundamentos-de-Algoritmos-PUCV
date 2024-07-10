from PIL import Image

img = Image.open('images.py/p3.2.png')
img.show()

#resolucion
asistentes = int(input())

contador = 0
for i in range (1, asistentes + 1):
    edad = int(input())
    if edad >= 18:
        contador += 1
    else:
        contador = contador

if contador == asistentes:
    print("Todos eran mayores de edad")
elif contador == 0:
    print("No hubo mayores de edad")
else:
    print(f"Cantidad de mayores de edad: {contador}")