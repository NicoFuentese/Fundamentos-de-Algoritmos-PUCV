from PIL import Image

img = Image.open("images.py/C2_5.4.png")
img.show()

#resolucion
def esParitoso (numero):
    contadorPAR = 0
    contadorIMPAR = 0
    while (numero > 0):
        digito = numero % 10
        if (digito % 2 == 0):
            contadorPAR += 1
        else:
            contadorIMPAR += 1
        numero = numero // 10
    
    if (contadorIMPAR == 0):
        return True
    else:
        return False

n = int(input())
if ( esParitoso(n) == True):
    print(f"El número {n} SI es paritoso")
else:
    print(f"El número {n} NO es paritoso")