from PIL import Image

img = Image.open('images.py/C3.2.7.png')
img.show()

#resolucion
salario_actual = int(input())

if salario_actual < 250000:
    reajuste = int(salario_actual * (1.2))
    print(f"Salario reajustado = $ {reajuste}" )
elif salario_actual >= 250000 and salario_actual < 500000:
    reajuste = int(salario_actual * (1.1))
    print(f"Salario reajustado = $ {reajuste}" )
elif salario_actual >= 500000 and salario_actual < 1000000:
    reajuste = int(salario_actual * (1.05))
    print(f"Salario reajustado = $ {reajuste}" )
elif salario_actual >= 1000000:
    reajuste = int(salario_actual * (1))
    print(f"Salario reajustado = $ {reajuste}" )