from PIL import Image

img = Image.open("images.py/C4.7.1.png")
img.show()

#resolucion
enumeracion = 0
while True:
    casos = int(input())
    if (2 <= casos <= 1000):
        if (casos % 2 == 0):
            pagina_sig = casos + 1
            enumeracion += 1
        else:
            pagina_sig = casos - 1
            enumeracion += 1

        print(f"CASO {enumeracion} : La página ingresada es la No. {casos} --> la otra página visible es la Nº : {pagina_sig}")
    else: 
        break
