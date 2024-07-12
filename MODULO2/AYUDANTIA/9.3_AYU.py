from PIL import Image

img = Image.open("images.py/C2_9.3.png")
img.show()

#resolucion
def factorial (n):
    productoria = 1
    for i in range (1, n + 1):
        productoria *= i
    return productoria