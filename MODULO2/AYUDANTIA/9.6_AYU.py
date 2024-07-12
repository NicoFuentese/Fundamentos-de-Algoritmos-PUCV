from PIL import Image

img = Image.open("images.py/C2_9.6.png")
img.show()

#resolucion
def dibujaTrianguloRectangulo (caracter, altura, forma):
    for i in range (0, altura):
        if (forma == 1):
            i += 1
            print((caracter + " ") * i, end = " ")
            print("  " * (altura - i), end = " ")
            print()
        elif (forma == 2):
            print("  " * i, end = "")
            print ((caracter + " ") * (altura - i), end = " ")
            print()
        elif (forma == 3):
            print((caracter + " ") * (altura - i), end = " ")
            print("  " * i, end = " ")
            print()