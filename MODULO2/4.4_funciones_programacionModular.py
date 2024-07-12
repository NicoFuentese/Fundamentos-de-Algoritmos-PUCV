from PIL import Image

img = Image.open("images.py/C2_4.4.png")
img.show()

#resolucion
def validar ():
    while True:
        n = int(input())
        if ( n >= 3):
            break
    return n
    
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
            
def enteroPrimo (x):
    segmentoMenor = x - 1
    segmentoMayor = x + 1
    while (esPrimo(segmentoMenor) == False):
        segmentoMenor -= 1
    while (esPrimo(segmentoMayor) == False):
        segmentoMayor += 1
    print(f"EL MENOR SEGMENTO PRIMO QUE CONTIENE A {x} ES [ {segmentoMenor} .. {segmentoMayor} ]")


#main
numero = validar()
enteroPrimo(numero)