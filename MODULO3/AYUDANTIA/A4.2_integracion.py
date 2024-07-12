from PIL import Image

img = Image.open("images.py/C3_A4.2.png")
img.show()

#resolucion
# ---------- POBLAR FRASES ---------- #
def poblarFrases():
    lista = []
    while True:
        frase = input()
        if frase == "FIN":
            print(f"Lista de Frases = {lista}\n")
            return lista

        lista.append(frase)
# ---------- POBLAR FRASES ---------- #

# ---------- CONVERTIR FRASES ---------- #
def convertirFrase(frase):
    frase = frase.lower()
    lista = []
    for caracter in frase:
        if caracter.isalpha():
            lista.append(caracter)
    return lista

# ---------- CONVERTIR FRASES ---------- #

# ---------- PROCESAR FRASES ---------- #
def procesarFrases(lista):
    fraseActual = 1
    totalPalindromos = 0
    totalNoPalindromos = 0
    for frase in lista:
        listaFrase = convertirFrase(frase)
        listaInversa = listaFrase.copy()
        listaInversa.reverse()
        if listaFrase == listaInversa:
            print(f"frase {fraseActual} SI es palíndroma")
            totalPalindromos += 1
        else:
            print(f"frase {fraseActual} NO es palíndroma")
            totalNoPalindromos += 1
        fraseActual += 1

    print(f"\nEn total hubo {totalPalindromos} frase(s) palíndroma(s)")
    print(f"En total hubo {totalNoPalindromos} frase(s) NO palíndroma(s)")

# ---------- PROCESAR FRASES ---------- #

# ---------- MAIN ---------- #
lista = poblarFrases()
procesarFrases(lista)
# ---------- MAIN ---------- #