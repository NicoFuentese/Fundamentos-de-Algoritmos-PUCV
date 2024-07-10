from PIL import Image

img = Image.open("images.py/C2_1.7.png")
img.show()

#resolucion
def leerValidar ():
    while True:
        x = float(input())
        if x >= -10 and x <= 10:
            return x
            
def factorial(x):
    factorial = 1
    for i in range (1, x +1):
        factorial *= i
    return factorial
    
def omega (x):
    sumatoria = 0
    for i in range (1, 51):
        termino = (x ** (2*i - 1)) / (factorial(2*i - 1))
        sumatoria += termino
    return sumatoria

#main

x = leerValidar()
print(f"Omega ( {x} ) = {omega(x)}")