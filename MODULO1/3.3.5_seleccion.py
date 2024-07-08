from PIL import Image

img = Image.open('images.py/C3.3.5.png')
img.show()

#resolucion
to1 = float(input())
to2 = float(input())
to3 = float(input())
p1 = float(input())
p2 = float(input())
rp1 = float(input())
s1 = float(input())

prom_to = (to1 + to2 + to3) / 3
prom_p = (p1 + p2) / 2

if rp1 >= 4 and s1 >= 4:
    nf = round(0.4 * s1 + 0.4 * rp1 + 0.1 * prom_to + 0.1 * prom_p , 1)
else:
    nf = round(0.4 * s1 + 0.4 * rp1 + 0.2 * prom_p , 1)
    
print(f"Nota presentación = {nf}")

if nf >= 5:
    print("Aprobado")
elif nf < 5 and nf >= 3:
    print("Debe rendir examen")
else:
    print("Reprobado")
    
if nf > 6:
    print("Vuelo de observación!")
else:
    print("")

