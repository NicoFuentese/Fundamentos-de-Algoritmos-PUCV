from PIL import Image

img = Image.open('images.py/C4.5.5.png')
img.show()

#resolucion
negativos = 0
positivos = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if n < 0:
            negativos += 1
        else:
            positivos += 1
            
print("POSITIVOS", positivos * "*")
print("NEGATIVOS", negativos * "*")