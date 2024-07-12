from PIL import Image

img = Image.open("images.py/C2_3.1.png")
img.show()

#resolucion
def convertirAMetros (cm):
    mts = cm / 100
    return mts