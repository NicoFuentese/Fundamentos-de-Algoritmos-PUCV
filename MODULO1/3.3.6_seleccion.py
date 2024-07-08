from PIL import Image

img = Image.open('images.py/C3.3.6.png')
img.show()

#resolucion
tiempo = int(input())
categoria = int(input())

base_pago = 800

if tiempo > 30:
    t_extra = tiempo - 30
    if categoria == 1:
        extra = 20 * t_extra
        pago = base_pago + extra
        print(pago)
    elif categoria == 2:
        extra = 25 * t_extra
        pago = base_pago + extra
        print(pago)
    elif categoria == 3:
        extra = 30 * t_extra
        extra2 = (t_extra // 30) * 15
        pago = base_pago + extra + extra2
        print(pago)
    else:
        extra = 35 * t_extra
        extra2 = (t_extra // 25) * 15
        extra3 = 200
        pago = base_pago + extra + extra2 + extra3
        print(pago)

else:
    if categoria != 4:
        extra = 0
        extra2 = 0
        pago = base_pago
        print(pago)
    else:
        extra = 200
        pago = base_pago + extra
        print(pago)
    
