#---------------------------------------------
#   Función para validar si una letra es
#   una vocal
#   Devuelve True si lo es y False sino lo es
#---------------------------------------------

def es_vocal(letra):
    letra = letra.lower()
    if letra in ("a","e","i","o","u"):
        return True
    else:
        return False

def main():
    letra = input("Ingrese una letra: ")
    if(es_vocal(letra) == True):
        print("\nLa letra "+letra+" SÍ es una vocal")
    else:
        print("\nLa letra "+letra+" NO es una vocal")

if __name__ == "__main__":
    main()