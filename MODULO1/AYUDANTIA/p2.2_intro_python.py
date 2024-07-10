from PIL import Image

img = Image.ope('images.py/p2.2.png')
img.show()

#resolucion
cargo_fijo = float(input())
cant_lts = float(input())
valor_uni_consu = float(input())
valor_uni_reco = float(input())
valor_uni_trata = float(input())

cant_m3 = cant_lts / 1000

#cargo variable de agua potable
cargo_var_potable = cant_m3 * valor_uni_consu

#cargo variable de alcantarillado
#recoleccion
cargo_reco = cant_m3 * valor_uni_reco
#tratamiento
cargo_trata = cant_m3 * valor_uni_trata

#monto total momentaneo
monto_total = cargo_fijo + cargo_var_potable + cargo_reco + cargo_trata

print(f"""BOLETA ESVALPITO
Cargo Fijo = ${cargo_fijo}
Metros cúbicos de agua consumidos = {cant_m3}
Monto parcial por agua consumida = ${cargo_var_potable}
Monto parcial por agua recolectada = ${cargo_reco}
Monto parcial por agua tratada = ${cargo_trata}""")

#cargo por sobreconsumo
if cant_m3 >= 40 and cant_m3 < 45:
    porcentaje = 15
    print(f"Cliente presenta sobreconsumo, su recargo es de un {porcentaje}%")
    print(f"Monto Total Antes del recargo = ${monto_total}")
elif cant_m3 >= 45 and cant_m3 < 50:
    porcentaje = 20
    print(f"Cliente presenta sobreconsumo, su recargo es de un {porcentaje}%")
    print(f"Monto Total Antes del recargo = ${monto_total}")
elif cant_m3 >= 50 and cant_m3 < 65:
    porcentaje = 30
    print(f"Cliente presenta sobreconsumo, su recargo es de un {porcentaje}%")
    print(f"Monto Total Antes del recargo = ${monto_total}")
elif cant_m3 >= 65:
    porcentaje = 55
    print(f"Cliente presenta sobreconsumo, su recargo es de un {porcentaje}%")
    print(f"Monto Total Antes del recargo = ${monto_total}")
else:
    porcentaje = 0
    print("Cliente no presenta sobreconsumo")

monto_final = monto_total * (1 + porcentaje / 100)

print(f"""Monto Total a Pagar = ${monto_final}""")