from PIL import Image

img = Image.open('images.py/C3.2.8.png')
img.show()

#resolucion
peso = float(input())
altura = float(input())

imc = round(peso / altura ** 2, 1)
print(f"imc paciente = {imc}")

if imc < 16.5:
    print("Estado nutricional paciente : Desnutrición")
    print("Alerta : paciente debe modificar su dieta alimenticia")
elif imc >= 16.5 and imc < 18.5:
    print("Estado nutricional paciente : Delgadez")
    print("Alerta : paciente debe mantener su dieta alimenticia")
elif imc >= 18.5 and imc < 25:
    print("Estado nutricional paciente : Peso Normal")
    print("Alerta : paciente debe mantener su dieta alimenticia")
elif imc >= 25 and imc < 30:
    print("Estado nutricional paciente : Sobrepeso")
    print("Alerta : paciente debe modificar su dieta alimenticia")
elif imc >= 30 and imc < 40:
    print("Estado nutricional paciente : Obesidad Moderada")
    print("Alerta : paciente debe modificar su dieta alimenticia")
elif imc >= 40:
    print("Estado nutricional paciente : Obesidad Mórbida o Masiva")
    print("Alerta : paciente debe modificar su dieta alimenticia")