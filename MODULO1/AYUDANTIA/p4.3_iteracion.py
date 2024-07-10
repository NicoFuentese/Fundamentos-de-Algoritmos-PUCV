from PIL import Image

img = Image.ope('images.py/p4.3.png')
img.show()

#resolucion
n = int(input())
print(f"{n} ", end = ", ")

while n == 1:
    if (n % 2 == 0):
        resultado = int(n / 2)
    else:
        resultado = int(n * 3 + 1)
    n = resultado
    print(f"{resultado} , ", end = "")

while n != 1:
    if (n % 2 == 0):
        resultado = int(n / 2)
    else:
        resultado = int(n * 3 + 1)
    n = resultado
    
    if resultado == 1:
        print(f"{resultado}", end = ".")
    else:
        print(f"{resultado} , ", end = "")

    
    