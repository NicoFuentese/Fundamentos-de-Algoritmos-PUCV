from PIL import Image

img = Image.open('images.py/C3.4.3.png')
img.show()

#resolucion
ahorro = int(input())
evento = int(input())
valor = int(input())

if (ahorro >= 1 and ahorro <= 99):
    if (evento == 1):
        dscto = 8
        print(f"Tienes un descuento del {dscto} %")
    elif (evento == 2):
        dscto = 25
        print(f"Tienes un descuento del {dscto} %")
elif (ahorro >= 100):
    if (evento == 1):
        dscto = 30
        print(f"Tienes un descuento del {dscto} %")
    elif (evento == 2):
        dscto = 45
        print(f"Tienes un descuento del {dscto} %")
        

# 1 usd -> 845 clp

final_usd = round(valor * (1 - dscto / 100), 2)
final_clp = round(final_usd * 845, 2)

print(f"El valor final de tu entrada en dólares es {final_usd}")
print(f"El valor final de tu entrada en pesos es {final_clp}")