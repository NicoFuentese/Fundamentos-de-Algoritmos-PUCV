from PIL import Image

img = Image.open('images.py/C2.1.png')
img.show()

#resolucion
ingreso = int(input())

urgencia = 0.37*ingreso
pediatria = 0.42*ingreso
trauma = 0.21*ingreso

print(f"Presupuesto Área Urgencia =  ${int(urgencia)}")
print(f"Presupuesto Área Pediatría =  ${int(pediatria)}")
print(f"Presupuesto Área Traumatología =  ${int(trauma)}")