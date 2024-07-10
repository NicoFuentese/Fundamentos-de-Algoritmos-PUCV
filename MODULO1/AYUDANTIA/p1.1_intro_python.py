from PIL import Image

img = Image.ope('images.py/p1.1.png')
img.show()

#resolucion
numero = int(input())
antecesor = numero -1
sucesor = numero + 1

print(f"""El antecesor de {numero} es {antecesor}
El sucesor de {numero} es {sucesor}""")
