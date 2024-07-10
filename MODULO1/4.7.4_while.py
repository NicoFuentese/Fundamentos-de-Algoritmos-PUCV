from PIL import Image

img = Image.open("images.py/C4.7.4.png")
img.show()

#resolucion
from math import ceil
caso = 1

while True:
    caloriasQ = int(input())
    if caloriasQ == 0:
        break
    caloriasC = int(input())
    sumaCalorias = 0
    for cada in range (1, caloriasC + 1 ):
        caloriasPorComida = int(input())
        sumaCalorias += caloriasPorComida
        
    entrenamientos = ceil(sumaCalorias / caloriasQ)
    
    
    
    print(f"""CASO {caso} :
Fitnesstencio consume {caloriasQ} calorías en cada entrenamiento.
Fitnesstencio consumió {sumaCalorias} calorías en sus {caloriasC} comilonas.
Fitnesstencio debe realizar {entrenamientos} entrenamiento(s).""")
    caso += 1
    print()