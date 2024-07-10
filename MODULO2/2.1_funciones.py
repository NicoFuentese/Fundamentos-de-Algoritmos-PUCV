from PIL import Image

img = Image.open("images.py/c2_2.1.png")
img.show()

#resolucion
def mostrarDivisores(numero):
    print(f"Divisores de {numero} : ", end = "")
    for divisor in range (1, numero + 1):
        if numero % divisor == 0:
            print (f"{divisor}", end = " ")