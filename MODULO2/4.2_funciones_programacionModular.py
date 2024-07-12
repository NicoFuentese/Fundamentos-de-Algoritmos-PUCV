from PIL import Image

img = Image.open("images.py/C2_4.2.png")
img.show()

#resolucion
def esPrimo (numero):
    if (numero <= 1):
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

def determina_escribe_gemelos (p, q):
    if (esPrimo(p) and esPrimo(q) == True):
        if (q > p):
            if ((q - p) == 2):
                print(f"Los números ({p},{q}) SI son primos gemelos")
            else:
                print(f"Los números ({p},{q}) NO son primos gemelos")
        else:
            if ((p - q) == 2):
                print(f"Los números ({q},{p}) SI son primos gemelos")
            else:
                print(f"Los números ({q},{p}) NO son primos gemelos")
    else:
        if (q > p):
            print(f"Los números ({p},{q}) NO son primos gemelos")
        else:
            print(f"Los números ({q},{p}) NO son primos gemelos")

        