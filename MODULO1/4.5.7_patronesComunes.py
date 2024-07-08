from PIL import Image

img = Image.open('images.py/C4.5.7.png')
img.show()

#resolucion
while True:
    n = int(input())
    if n > 0:
        break

mayor_t = 0
suma = 0
for i in range (1, n + 1):
    temperatura = float(input())
    t_fa = (temperatura * 9 / 5) + 32
    suma += t_fa
    
    #mayor t
    if i == 1:
        mayor_t = t_fa
    else:
        if (mayor_t < t_fa):
            mayor_t = t_fa

prom_t = suma / n

print(f"""Reporte de Temperaturas
=======================
Se han procesado {n} datos de temperaturas en grados Celsius
Promedio de temperaturas = {prom_t} grados Fahrenheit
Mayor temperatura registrada : {mayor_t} grados Fahrenheit""")