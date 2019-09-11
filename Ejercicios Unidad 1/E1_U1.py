#---------------------------------------------
#   Función para validar si una cadena es
#   un palíndromo.
#   Devuelve True si lo es y False sino lo es
#---------------------------------------------
def es_palindromo(cadena):
    cadenaInvertida = cadena[::-1]
    if(cadenaInvertida == cadena):
        return True
    else:
        return False

def main():
    cadena = input("Ingrese una palabra: ")
    if(es_palindromo(cadena) == True):
        print("\nLa palabra "+str(cadena)+" SÍ es un palíndromo")
    else:
        print("\nLa palabra "+str(cadena)+" NO es un palíndromo")


if __name__ == "__main__":
    main()