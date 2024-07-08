from PIL import Image

img = Image.open('images.py/C4.5.4.png')
img.show()

#resolucion
while True:
    n = int(input())
    if n >= 0:
        break

factorial = 1
for i in range(1 , n + 1):
    factorial = factorial * i
    
print(f"El factorial de {n} es {factorial}")