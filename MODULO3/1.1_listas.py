from PIL import Image

img = Image.open("images.py/C3_1.1.png")
img.show()

#resolucion
def validar ():
    n = 0
    while True:
        n = int(input())
        if n >= 1 and n <= 365:
            break
    return n
    
def leerT(n):
    lista = []
    for i in range (n):
        t = float(input())
        lista += [t]
    return lista
    
"""
def leerT(lista, n):
for temp in range(n):
t = float(input())
lista = [t]
lista += [t]
"""
    
def mostrarT(lista):
    print(f"Las {len(lista)} temperaturas son : ", end ="")
    for i in lista:
        print(f"{i}", end = " ")
    print("\n")
    
def contarSP (lista, prom):
    cont = 0
    for i in lista:
        if i > prom:
            cont += 1
    return cont

#main
n = validar()
listaT = leerT(n)
mostrarT(listaT)

menor = min(listaT)
mayor = max(listaT)

promedio = round(sum(listaT) / len(listaT), 2)
sobrepromedio = contarSP(listaT, promedio)

print(f"""Temperatura mínima es {menor}
Temperatura máxima es {mayor}
Promedio de {n} temperaturas es {promedio}
Cantidad de mediciones sobre el promedio es {sobrepromedio}""")