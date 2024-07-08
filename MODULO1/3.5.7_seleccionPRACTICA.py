from PIL import Image

img = Image.open('images.py/C3.5.7.png')
img.show()

#resolucion
X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
distancia = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2)**(1/2)
print ("La distancia total es de", round(distancia,1))
