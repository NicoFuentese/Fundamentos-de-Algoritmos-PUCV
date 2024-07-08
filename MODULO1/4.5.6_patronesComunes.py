from PIL import Image

img = Image.open('images.py/C4.5.6.png')
img.show()

#resolucion
while True:
    total = int(input())
    if total > 0:
        break


for i in range(1 , total+ 1):
    temperatura = float(input())
    if i== 1:
        menor = temperatura
    else: 
        if temperatura < menor:
            menor = temperatura
            
print(f"Menor temperatura registrada es : {menor}")