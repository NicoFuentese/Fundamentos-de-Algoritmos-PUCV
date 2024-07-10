from PIL import Image

img = Image.open("images.py/C4.6.3.png")
img.show()

#resolucion
while True:
    n = int(input())
    if (1 <= n <= 40):
        break

if ( n < 2):
    f1 = 1
    print(f1)
elif ( n < 3):
    f1 = 1
    f2 = 1
    print(f1, f2)
else:
    f1 = 1
    f2 = 1
    print (f1, f2, end = " ")
    
    for i in range (3, n + 1):
        termino = f1 + f2
        f1 = f2
        f2 = termino
        print(termino, end = " ")

    