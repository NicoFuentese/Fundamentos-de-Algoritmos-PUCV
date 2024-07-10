from PIL import Image

img = Image.open("images.py/C4.7.5.png")
img.show()

#resolucion
cuantosCasos = int(input())
for cada in range (1, cuantosCasos + 1):
    cuantosPago = int(input())
    cuantosCompro = int(input())
    diff = cuantosPago - cuantosCompro
    if diff == 0:
        print(f"CASO {cada} : PAGO EXACTO !!")
    elif diff < 0:
        print(f"CASO {cada} : DEBE $ {abs(diff)}")
    else:
        print(f"CASO {cada} : VUELTO = $ {diff} pesos chilenos -->", end = "")
        mon500 = diff // 500
        diff = diff % 500
        mon100 = diff // 100
        diff = diff % 100
        mon50 = diff // 50
        diff = diff % 50
        mon10 = diff // 10
        diff = diff % 10
        mon5 = diff // 5
        diff = diff % 5
        mon1 = diff
        
        print(f" {mon500} {mon100} {mon50} {mon10} {mon5} {mon1}")