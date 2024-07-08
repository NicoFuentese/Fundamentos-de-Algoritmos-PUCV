from PIL import Image

img = Image.open('images.py/C3.4.1.png')
img.show()

#resolucion
pasajero = int(input())
horario = int(input())


if ((pasajero == 4 or pasajero == 7)):
    if (horario == 1):
        valor = 680
        print(f"valor pasaje = {valor}")
    elif (horario == 2):
        valor = 550
        print(f"valor pasaje = {valor}")
    elif (horario == 3):
        valor = 410
        print(f"valor pasaje = {valor}")
elif (pasajero == 5 or pasajero == 6):
        valor = 250
        print(f"valor pasaje = {valor}")