from PIL import Image

img = Image.open("images.py/C4.6.1.png")
img.show()

#resolucion
while True:
    n = int(input())
    if (1 <= n <= 100):
        break

suma = 0
for i in range (0, n):
    termino = 1 + 3 * i
    
    if (i != n - 1):
        print(termino, end =" , ")
    else:
        print(termino)

