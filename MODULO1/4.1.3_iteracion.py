from PIL import Image

img = Image.open('images.py/C4.1.3.png')
img.show()

#resolucion
n = int(input())
control = 1
print(f"Primeros 10 múltiplos de {n} :")
while control<=10:
    resultado = n * control
    print(resultado)
    control += 1