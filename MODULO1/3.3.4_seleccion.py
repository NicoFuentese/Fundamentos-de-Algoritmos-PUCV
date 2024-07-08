from PIL import Image

img = Image.open('images.py/C3.3.4.png')
img.show()

#resolucion
ventas = int(input())

if ventas < 50000: 
    comision = 0
elif ventas >= 50000 and ventas < 500000:
    comision = 0.08
elif ventas >= 500000 and ventas < 1000000:
    comision = 0.1
else:
    comision = 0.15
    
comision = int(ventas * comision)

print(f"su comisión es de $ {comision}")
