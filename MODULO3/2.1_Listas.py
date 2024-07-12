from PIL import Image

img = Image.open("images.py/C3_2.1.png")
img.show()

#resolucion
def validar ():
    while True:
        n = int(input())
        if n > 0:
            return n

def almacenar (lista, n):
    for i in range(n):
        nota = float(input())
        lista.append(nota)
        
#main
n = validar()
lista = []
almacenar(lista, n)

print(f"Lista de Notas de {n} estudiantes = [", end = "")
aprobados = 0
reprobados = 0
for i in range(len(lista)):
    if lista[i] == lista[len(lista) - 1] and i == len(lista) - 1:
        print(lista[i], end = "]")
    else:
        print(lista[i], end = ", ")
    
    if lista[i] >= 4:
        aprobados += 1
    else:
        reprobados += 1

print()
print(f"{aprobados} estudiante(s) aprobaron la asignatura.")
print(f"{reprobados} estudiante(s) reprobaron la asignatura.")

prom = round(sum(lista) / len(lista), 2)
print(f"Promedio General del curso = {prom}")
print(f"""Menor Nota = {min(lista)}
Mayor Nota = {max(lista)}""")