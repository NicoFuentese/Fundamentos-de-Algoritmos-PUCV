from PIL import Image

img = Image.open("images.py/c2_2.3.png")
img.show()

#resolucion
def esPrimo (numero):
    if numero == 1:
        return False
    else:
        raizTruncada = int ( numero ** 0.5)
        for divisor in range (2, raizTruncada + 1):
            if (numero % divisor == 0 and numero != divisor):
                return False
        return True
            