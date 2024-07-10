from PIL import Image

img = Image.open('images.py/p1.5.png')
img.show()

#resolucion
bebidas = int(input())
p_bebidas = int(input())
pizzas = int(input())
p_pizzas = int(input())
palomitas = int(input())
p_palomitas = int(input())
amigos = int(input())

total = p_bebidas*bebidas + p_pizzas*pizzas + p_palomitas*palomitas
cuota = round(total/amigos)
cantidad = bebidas + pizzas + palomitas

print(f"""Total gasto compra = {total}
Valor cuota por invitado = {cuota}
Total items comprados = {cantidad}""")
