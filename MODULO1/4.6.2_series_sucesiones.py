from PIL import Image

img = Image.open("images.py/C4.6.2.png")
img.show()

#resolucion
while True:
    n = int(input())
    if (n > 0):
        break

sumatoria = 0
for i in range (1, n + 1):
    if (i == 1):
        suma = 1
    else:
        if (i % 2 == 0):
            suma = suma + 4
        else:
            suma = suma - 2
    
    sumatoria += suma
print(f"El valor de la suma es : {sumatoria}")