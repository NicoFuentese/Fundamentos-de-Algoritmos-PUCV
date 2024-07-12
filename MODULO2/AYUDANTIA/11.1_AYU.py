from PIL import Image

img = Image.open("images.py/C2_11.1.png")
img.show()

#resolucion
def esOrdenado (numero):
    if (numero < 10):
        return True
    else:
        digito_anterior = numero % 10
        numero //= 10
        
        while (numero != 0):
            digito_actual = numero % 10
            numero //= 10
            if (digito_anterior < digito_actual):
                return False
            digito_anterior = digito_actual
        return True


def ordenadosEnIntervalo (a, b):
    contador = 0
    for i in range (a, b + 1):
        if (esOrdenado(i) == True):
            print(i, end = " ")
            contador += 1
    if (contador == 0):
        print("NO HAY")


    
    