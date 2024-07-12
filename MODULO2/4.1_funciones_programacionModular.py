from PIL import Image

img = Image.open("images.py/C2_4.1.png")
img.show()

#resolucion
def esPrimo (numero):
    if (numero == 1):
        return False
    else:
        contador = 0
        for i in range (1, numero + 1):
            if (numero % i == 0):
                contador += 1
        if (contador == 2):
            return True
        else: 
            return False
            
def esPrimoSophieGermain (n):
    if (esPrimo (n) == True and esPrimo(2*n + 1) == True):
        return True
    else:
        return False