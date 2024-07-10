from PIL import Image

img = Image.ope('images.py/p2.1.png')
img.show()

#resolucion
num_epi = int(input())
num_niv = int(input())
punt_min = int(input())
punt_obt = int(input())
vidas = int(input())

estrellas = 0
if punt_obt < punt_min:
    print("Nivel no superado NO lograste el objetivo")
    vidas = vidas - 1
    if vidas == 0:
        print("No te quedan más vidas.")
    elif vidas == 1:
        print("Te queda 1 vida.")
    else:
        print(f"Te quedan {vidas} vidas.")
elif punt_obt >= punt_min:
    print("Genial nivel superado !")
    if punt_obt / punt_min  >= 1 and punt_obt / punt_min < 2:
        estrellas = estrellas + 1
        print(f"Obtuviste {estrellas} estrella.")
    elif punt_obt / punt_min  >= 2 and punt_obt / punt_min < 3:
        estrellas = estrellas + 2
        print(f"Obtuviste {estrellas} estrellas.")
    else:
        estrellas = estrellas + 3
        print(f"Obtuviste {estrellas} estrellas.")
    
    if num_niv % 15 == 0:
        print(f"Completaste el episodio {num_epi}")
    else:
        print(f"Pasaste al nivel {num_niv + 1} del episodio {num_epi}")

        