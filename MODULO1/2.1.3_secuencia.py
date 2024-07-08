from PIL import Image

img = Image.open('images.py/C2.3.png')
img.show()

#resolucion
capital = int(input())
interes = int(input())
print(f"Monto de dinero invertido = {capital}")
print(f"Tasa de interés mensual = {interes}%")

ganancia = int(capital*(interes/100))
total = int(capital*(1+(interes/100)))

print(f"Monto de dinero que ganará el inversionista = {ganancia}")
print(f"Capital actualizado = {total}")