from PIL import Image

img = Image.open("images.py/C3_2.2.png")
img.show()

#resolucion
def ICA (N, P, M):
    pesoN = 0.4
    pesoP = 0.3
    pesoM = 0.3
    return (pesoN * N + pesoP * P + pesoM * M) / (pesoN + pesoP + pesoM)

def calificador(n):
    if (n >= 0 and n <= 25):
        valor = "MALA"
    elif (n >= 76 and n <= 100):
        valor = "EXCELENTE"
    else:
        valor = "NORMAL"
    return valor

#main
n = int(input())
listaICA = []

for i in range(1, n + 1):
    nitratos = int(input())
    fosfatos = int(input())
    metales = int(input())
    valor = round(ICA(nitratos, fosfatos, metales), 1)
    listaICA.append(valor)

mal = 0
exc = 0
for i in listaICA:
    if (calificador(i) == "MALA"):
        mal += 1
    elif (calificador(i) == "EXCELENTE"):
        exc += 1

print(f"ICA de {n} días = {listaICA}")
print()
print(f"""{mal} día(s) el AGUA del río fue categorizada como MALA
{exc} día(s) el AGUA del río fue categorizada como EXCELENTE""")