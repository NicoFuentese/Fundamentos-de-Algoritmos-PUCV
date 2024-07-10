from PIL import Image

img = Image.ope('images.py/p1.2.png')
img.show()

#resolucion
import math

arista = float(input())
area = 6*pow(arista,2)
volumen = pow(arista,3)

print(f"""área del cubo = {area}
volumen del cubo = {volumen}""")