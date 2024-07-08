from PIL import Image

img = Image.open('images.py/C3.5.14.png')
img.show()

#resolucion
promCatedras = float(input())
notaFinalProy = float(input())
porcCatedra = float(input())

porcProyecto = 100 - porcCatedra
notaFinalSinBonif = (promCatedras * porcCatedra/100) + (notaFinalProy * porcProyecto/100)
if (promCatedras >= 5) and (notaFinalProy > 6) :
    totalBonificacion = notaFinalSinBonif * 0.15
else :
    totalBonificacion = notaFinalSinBonif * 0.06
notaFinalConBon = notaFinalSinBonif + totalBonificacion
print("Nota Final sin bonificacion =",round(notaFinalSinBonif,1))
print("Total Bonificacion          =",round(totalBonificacion,1))
print("Nota Final con bonificacion =",round(notaFinalConBon,1))