from PIL import Image

img = Image.open('images.py/C3.4.4.png')
img.show()

#resolucion
latas = int(input())
packs = int(input())
valor_u = int(input())

valor_total = (latas + packs * 6) * valor_u

if (packs >= 10):
    if (valor_total < 30000):
        dscto = 0
    elif (valor_total >= 30000 and valor_total < 50000):
        dscto = 10
    elif (valor_total >= 50000 and valor_total < 70000):
        dscto = 15
    elif (valor_total >= 70000):
        dscto = 20
else:
    dscto = 0
    
valor_dscto = int(round(valor_total * dscto /100, 0))    
total = int(round(valor_total * (1- dscto / 100), 0))

print(f"""Total de la compra = $ {valor_total}
Descuento = $ {valor_dscto}
Precio total a pagar = $ {total}""")