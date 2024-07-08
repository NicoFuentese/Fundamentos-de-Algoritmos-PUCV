from PIL import Image

img = Image.open('images.py/C3.2.6.png')
img.show()

#resolucion
altura = float(input())
peso = int(input())
edad = int(input())

imc = peso / altura ** 2
print(f"imc = {imc} y edad = {edad}")

if imc < 22:
    if edad < 45:
        print("riesgo cardíaco es bajo")
    else:
        print("riesgo cardíaco es medio")
else:
    if edad < 45:
        print("riesgo cardíaco es medio")
    else:
        print("riesgo cardíaco es alto")
    