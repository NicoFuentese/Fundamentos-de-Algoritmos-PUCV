"""----------------------------------------------------------------------------
NOMBRE : NICOLAS FUENTES WILLIAMS
Este programa entrega la cantidad en mililitros de la dosis correspondiente de 
FELIX FELICIS segun la edad del estudiante, mediante la subdivision del 
problema en funciones.
----------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------
  Se importan las funciones utilizadas de la librertia math
----------------------------------------------------------------------------"""
from math import trunc
from math import sqrt
from math import ceil

"""----------------------------------------------------------------------------
  Se definen las funciones a utilizar:
  Omega = es el N-ésimo término de la siguiente sucesión aritmética : 
  7, 8, 10, 13, 17, 22, 28, 35, 43, 52, 62, 73, 85...
  factorial = Calcula el factorial de un numero.
  Sigma = es el valor obtenido al evaluar y sumar los 50 primeros términos de
  la sumatoria.
  Sampi = es la SUMATORIA de TODOS los DIVISORES POSITIVOS IMPARES del valor N.
  Kappa = es la SUMATORIA de TODOS los números naturales PARES entre 1 y el 
  valor de N.
  Validar = Valida que el dato ingresado sea valido para el problema.
  FelixFelicis = Calcula los mililitros de la persona usando las funciones 
  previas y los datos ingresados por el estudiante.
  Procesar = Funcion que procesa los datos del alumno e imprime los resultados
  recomendados de la dosis de FelixFelicis.
----------------------------------------------------------------------------"""
def omega (numero):
    valor = 7
    for i in range (0,numero + 1):
        valor += i
    return valor

def factorial (x):
    productoria = 1
    if x == 0:
        productoria = 1
    else:
        for i in range (1, x + 1):
            productoria *= i
    return productoria

def sigma (x):
    sumatoria = 0
    for i in range (1, 51):
        termino = x ** i / factorial(i)
        sumatoria += termino
    return sumatoria
        
def sampi (n):
    sumatoria = 0
    for i in range (1, n + 1):
        if (i % 2 == 1):
            if (n % i == 0):
                sumatoria += i
            else:
                sumatoria = sumatoria
    return sumatoria

def kappa (n):
    sumatoria = 0
    for i in range (1, n + 1):
        if (i % 2 == 0):
            sumatoria += i
    return sumatoria
            
def validar ():
    dato = int(input())
    while True:
        if (0 < dato <= 10000):
            break
        dato = int(input())
    return dato

def FelixFelicis (edad, peso, estatura):
    edadMeses = edad * 12
    peso_grs = peso * 1000
    estatura_mts = estatura / 100
    if (1 <= edad <= 20):
        formula = trunc( (omega(edadMeses) * peso) / sigma (estatura_mts) )
    elif (21 <= edad <= 40):
        formula = trunc((sampi(peso) * kappa (edad)) / estatura_mts)
    elif (41 <= edad <= 60):
        formula = trunc((sampi (edadMeses) * trunc(sqrt(peso_grs))) / estatura)
    else:
        formula = trunc((kappa(peso) * trunc( sqrt( edad ))) / estatura_mts)
    return formula
    
def procesar (n):
    for i in range (1, n + 1):
        edad = int(input())
        peso = int(input()) #kg
        estatura = int(input()) #cm
        dosis = FelixFelicis (edad, peso, estatura)
        dias_suerte = trunc((dosis / 50 * 12) / 24)
        print(f"""Habitante #{i}
Edad : {edad} año(s) - {edad * 12} meses.-
Peso : {peso} Kg - {peso * 1000} g.-
Estatura : {estatura} cm - {estatura / 100} m.-
Dosis de FELIX FELICIS según su edad = {dosis} ml.
El habitante tendrá {dias_suerte} día(s) de SUERTE !""")
        print("--------------------------------------------------")

"""----------------------------------------------------------------------------
  Codigo principal, se ingresa el dato habitantes para representar cuantos
  alumnos seran calculadas sus dosis recomendadas.
----------------------------------------------------------------------------"""
#main
habitantes = validar()

"""----------------------------------------------------------------------------
  Printeo del inicio del informe tecnico y aplicacion de la funcion procesar.
----------------------------------------------------------------------------"""
print(f"Harry, se procesarán {habitantes} habitantes del mundo mágico.")
print()
print("----- INICIO DEL PROCESO -----")
print()
procesar (habitantes)

