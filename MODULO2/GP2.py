"""----------------------------------------------------------------------------
NOMBRE : NICOLAS FUENTES WILLIAMS
Este programa entrega la cantidad en mililitros de la dosis correspondiente de 
FELIX FELICIS segun la edad del estudiante, mediante la subdivision del 
problema en funciones.
----------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------
  Se importan la funcion utilizada de la libreria math
----------------------------------------------------------------------------"""
from math import trunc

"""----------------------------------------------------------------------------
  Se definen las funciones a utilizar:
  esPrimo = retorna True o False si el numero es primo o no.
  esPar = retorna True o False si el numero es par
  esCuadradoPerfecto = retorna True o False si el numero es un
  cuadrado perfecto o no
  esDeficiente = retorna True o False si el numero es deficiente o no.
  ArmaMagicaLegendaria = Segun los valores booleanos de las funciones previas,
  se retorna True o False si se puede crear un arma magica legendaria o no.
----------------------------------------------------------------------------"""
def esPrimo (numero):
    if numero == 1:
        return False
    else:
        raizTruncada = int(numero ** 0.5)
        for divisor in range (2, raizTruncada + 1):
            if (numero % divisor == 0 and numero != divisor):
                return False
        return True

def esPar (numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def esCuadradoPerfecto (numero):
    comparacion = int (numero ** 0.5)
    comparacion = comparacion ** 2
    if comparacion != numero:
        return False
    else:
        return True

def esDeficiente (n):
    suma = 0
    for i in range (1, n):
        if (n % i == 0):
            suma += i
    if (suma < n):
        return True
    else:
        return False

def ArmaMagicaLegendaria (sumatoria, productoria, valorMax, valorMin, total_gemas):
    truncado = trunc(total_gemas / 2)
    if ( esPrimo(sumatoria) == True and esPar(productoria) == True and esCuadradoPerfecto(valorMax - valorMin) == True and esDeficiente(truncado) == True):
        return True
    else:
        return False
    
"""----------------------------------------------------------------------------
  Codigo principal del programa.
----------------------------------------------------------------------------"""
#main
"""----------------------------------------------------------------------------
  Se definen los contadores para poder calcular medidas estadisticas y contadores
  normales. Se realiza el ingreso de datos dentro de un bucle indefinido 
  hasta que el rut ingresado sea "0-0"
----------------------------------------------------------------------------"""
contador = 0
jugadoresSI = 0
jugadoresNO = 0
sumaGemasSI = 0
while True:
    rut = input()
    if ( rut == "0-0"):
        break
    total_gemas = int(input())
    contador += 1
    
    #print inicial
    print(f"Jugador # {contador} - Rut = {rut}")
    print(f"Total gemas recolectadas : {total_gemas}")
    print("Poder Mágico Gemas = [", end = "")
    
    sumatoria = 0
    productoria = 1
    valorMax = 0
    valorMin = 0
    
    """----------------------------------------------------------------------------
  Se Ingresan los poderes de todas las gemas ingresadas previamente. 
  Se printean estos poderes, se encuentra el poder magico, el minimo, la
  sumatoria total del poder de todas las gemas y la productoria de todas ellas.
----------------------------------------------------------------------------"""
    for i in range (1, total_gemas + 1):
        poder = int(input())
        
        #print de poderes
        if ( i != total_gemas):
            print(poder, end = " , ")
        else:
            print(f"{poder}]")
        #termino print de poderes
        
        #valor maximo
        if (valorMax == 0):
            valorMax = poder
        else:
            if (valorMax < poder):
                valorMax = poder
        
        #valor minimo
        if (valorMin == 0):
            valorMin = poder
        else:
            if ( valorMin > poder):
                valorMin = poder
        
        #sumatoria y productoria
        sumatoria += poder
        productoria *= poder
    """----------------------------------------------------------------------------
  Se calcula si con el poder de las gemas entregadas se puede crear un arma
  magica legendaria.
----------------------------------------------------------------------------"""
    #Calculo de funciones para SI o NO
    valor = ArmaMagicaLegendaria (sumatoria, productoria, valorMax, valorMin, total_gemas)
    
    """----------------------------------------------------------------------------
  Se genera la respuesta respectiva para el caso de SI se puede crear un arma
  magica legendaria o si NO se puede crear.
----------------------------------------------------------------------------"""
    if (valor == True):
        sumaGemasSI += total_gemas
        jugadoresSI += 1
        print("SI puede formar un arma mágica legendaria.")
        print()
    else:
        print("NO puede formar un arma mágica legendaria.")
        jugadoresNO += 1
        print()
    

#resumen general
"""----------------------------------------------------------------------------
  Se printea los datos de los jugadores ingresados, el total de jugadores 
  que si pudo forjar un arma magica, los que no pudieron, y el promedio
  general de las gemas utilizadas por los jugadores que SI pudieron forjarla 
  (si es el caso que existan jugadores que pudieron forjar un arma magica).
----------------------------------------------------------------------------"""
print(f"""Total jugadores procesados = {contador}
Total de jugadores que SI pudo forjar un arma mágica legendaria = {jugadoresSI}
Total de jugadores que NO pudo forjar un arma mágica legendaria = {jugadoresNO}""")

if (jugadoresSI != 0):
    prom = round(sumaGemasSI / jugadoresSI, 2)
    print(f"Promedio total gemas usadas para forjar armas mágicas legendarias = {prom}")