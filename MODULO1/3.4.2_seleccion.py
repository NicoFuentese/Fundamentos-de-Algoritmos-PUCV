from PIL import Image

img = Image.open('images.py/C3.4.2.png')
img.show()

#resolucion
edad = int(input())
destino = int(input())
pasaje = int(input())

#dolar a peso chileno = 1 -> 749

if (edad >= 0 and edad <= 30):
    if (destino == 1):
        dscto = 15
        print(f"Tienes un descuento del {dscto} %")
    elif (destino == 2):
        dscto = 5
        print(f"Tienes un descuento del {dscto} %")
elif (edad >= 31):
    if (destino == 1):
        dscto = 20
        print(f"Tienes un descuento del {dscto} %")
    elif (destino == 2):
        dscto = 10
        print(f"Tienes un descuento del {dscto} %")
        
valor_final_usd = round(pasaje * (1-dscto / 100) ,2)
valor_final_clp = round(valor_final_usd * 749, 2)

print(f"El valor final de tu pasaje en dólares es {valor_final_usd}")
print(f"El valor final de tu pasaje en pesos es {valor_final_clp}")