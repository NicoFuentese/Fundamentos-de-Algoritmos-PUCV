from PIL import Image

img = Image.open('images.py/C4.2.1.png')
img.show()

#resolucion
estudiantes = int(input())

for i in range(1 , estudiantes + 1):
    notaP1 = float(input())
    notaP2 = float(input())
    notaI = float(input())
    notafinal = notaP1*0.3 + notaP2*0.3 + notaI*0.4
    if notafinal >= 4:
        situacion = "Aprueba"
    else:
        situacion = "Reprueba"
    print(f"estudiante {i} - nota final = {notafinal} - situación : {situacion}")