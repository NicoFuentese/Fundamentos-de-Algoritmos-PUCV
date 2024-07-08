from PIL import Image

img = Image.open('images.py/C1.2.png')
img.show()

#resolucion
nombre = input()
edad = int(input())
print("Hola,",nombre,"!!")
print("Tu edad actual es",edad)
print("Tu edad en 12 meses sera", edad+1)
