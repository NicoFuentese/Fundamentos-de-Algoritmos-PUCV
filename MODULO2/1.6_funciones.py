from PIL import Image

img = Image.open("images.py/C2_1.6.png")
img.show()

#resolucion
def factorial (dato):
    productoria = 1
    for i in range (1, dato + 1):
        productoria *= i
    return productoria

def combinaciones(n, x):
    combi = factorial(n) / (factorial(x) * factorial(n - x))
    return combi

#main
    numero = int(input())
    elementos = int(input())
    combinaciones(numero , elementos)
    print(f"Combinaciones de {numero} elementos tomando {elementos} de una vez = {combina}")

#porque tiene que estar identado para que pase los casos de prueba?
# en la jerarquia mas alta me lanza error EOF