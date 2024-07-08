from PIL import Image

img = Image.open('images.py/C2.2.5.png')
img.show()

#resolucion
personas = int(input())
c_pasteles = int(input())
p_pastel = int(input())
c_bebidas = int(input())
p_bebida = int(input())

cantidad = c_pasteles + c_bebidas
total = p_pastel*c_pasteles + p_bebida*c_bebidas

cuota = round(total/personas)

print(f"""Total items comprados : {cantidad}
Total gastado en pasteles y bebidas : {total}
Monto a pagar por cada uno : {cuota}""")