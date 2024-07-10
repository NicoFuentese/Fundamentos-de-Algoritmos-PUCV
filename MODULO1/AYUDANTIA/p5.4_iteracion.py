from PIL import Image

img = Image.ope('images.py/p5.4.png')
img.show()

#resolucion
while True:
    n = int(input())
    if (1 <= n <= 100):
        break


denominador = 0
for i in range (1, n + 1):
    numero = float(input())
    denominador += 1 / numero
    
    funcion = n / denominador

print(f"Media Armonica = {funcion}")