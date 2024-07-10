from PIL import Image

img = Image.open("images.py/C2_1.1.png")
img.show()

#resolucion
def calcularAreaCirculo (radio):
    area = radio ** 2 * 3.14
    return area