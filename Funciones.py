#---------------------------------------------
#   Función para calcular el promedio
#   de un número indeterminado de parámetros
#---------------------------------------------
def promedio(*argv):
    suma = 0
    n = len(argv)
    for arg in argv:
        suma += arg
    return suma/n

if __name__ == "__main__":
    print("El promedio es:",promedio(7.5,10,15,20))
