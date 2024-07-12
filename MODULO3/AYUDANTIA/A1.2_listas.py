from PIL import Image

img = Image.open("images.py/C3_A1.2.png")
img.show()

#resolucion
edades = []
while True:
    edad = int(input())
    if edad < 0:
        break
    edades.append(edad)

print("Lista Original =", edades)
print("Lista Nueva = [", end="")

for i in range(len(edades)):
    if (i % 2 == 0):
        edades[i] += 1
    else:
        edades[i] -= 1
    
    if (i != len(edades) - 1):
        print(f"{edades[i]}, ", end = "")
    else:
        print(edades[i], end = "")

print("]")