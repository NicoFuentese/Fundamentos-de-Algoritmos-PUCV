from PIL import Image

img = Image.open("images.py/C3_5.1.png")
img.show()

#resolucion
def leerDatos ():
    lista = []
    while True:
        dato = int(input())
        if dato < 0:
            break
        if dato not in lista:
            lista.append(dato)
    return lista

def esPrimo (numero):
    if numero <= 1:
        return False
    raizT = int(numero ** 0.5)
    for divisor in range (2, raizT + 1):
        if numero % divisor == 0:
            return False
    return True

def filtrarPrimos (lista):
    listaPrimos = []
    for i in lista:
        if esPrimo(i):
            listaPrimos.append(i)
    return listaPrimos

#MAIN
lista = leerDatos ()
lista.sort()
print(f"Lista =", lista)
print(f"total de elementos en la lista SIN repeticiones = {len(lista)}")

primos = filtrarPrimos(lista)
if len(primos) == 1:
    print(f"Numeros Primos en lista :", *primos)
    print("Se encontró 1 número primo en la lista original.")
elif len(primos) == 0:
    print("La lista original NO contiene números primos.")
else:
    print(f"Numeros Primos en lista :", *primos)
    print(f"Se encontraron {len(primos)} números primos en la lista original.")