from PIL import Image

img = Image.open('')
img.show('images.py/C3.1.4.png')

#resolucion
peso = float(input())
altura = float(input())

imc = round(peso/(altura ** 2),1)

print(f"imc paciente = {imc}")

if imc <16.5 or imc >= 25:
    print("Alerta : paciente debe modificar su dieta alimenticia")
else:
    print("Alerta : paciente debe mantener su dieta alimenticia")