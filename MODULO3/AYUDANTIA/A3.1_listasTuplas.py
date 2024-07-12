from PIL import Image

img = Image.open("images.py/C3_A3.1.png")
img.show()

#resolucion
def filtroEnMenu (tipoPlato, monto, listaMenu):
    contPlatos = 0
    print(f"Listado de {tipoPlato} (s) menores a $ {monto} :")
    for cadaMenu in listaMenu:
        codigo, nombre, tipo, valor = cadaMenu
        if (tipo == tipoPlato) and (valor < monto):
            contPlatos += 1
            print(f"{nombre} = $ {valor}")
    
    if (contPlatos == 0):
        print("no hay información disponible")
        
def valorarConsumo (consumo, miLista):
    print("cantidad - plato - valor")
    print("------------------------")
    valorTotal = 0
    for cadaTupla in consumo:
        codigo, cantidad = cadaTupla
        for tupla in miLista:
            if (codigo == tupla[0]):
                valor = tupla[3] * cantidad
                nombre = tupla[1]
                break
        print(f"{cantidad} {nombre} $ {valor}")
        valorTotal += valor
    print(f"TOTAL = $ {valorTotal}")
