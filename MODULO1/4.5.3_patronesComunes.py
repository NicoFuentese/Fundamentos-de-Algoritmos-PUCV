from PIL import Image

img = Image.open('images.py/C4.5.3.png')
img.show()

#resolucion
while True:
    n = int(input())
    if n >0:
        break
    
sumaJuan = 0
sumaMario = 0

for i in range(1 , n+1):
    mario = int(input())
    juan = int(input())
    
    sumaJuan += juan
    sumaMario += mario

if sumaJuan > sumaMario:
    print(f"Mario ha ganado con un total de {sumaMario} minutos de viaje!")
elif sumaMario > sumaJuan:
    print(f"Juan ha ganado con un total de {sumaJuan} minutos de viaje!")
else:
    print(f"Mario y Juan empataron con un total de {sumaJuan} minutos de viaje!")
