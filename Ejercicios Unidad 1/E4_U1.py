#---------------------------------------------
#   Función para validar si un nombre de
#   usuario es válido o no
#   Devuelve True si lo es y False sino lo es
#---------------------------------------------
def validar_nombre_usuario(nombre):
    valido = False
    if(len(nombre)>=6):
        if(len(nombre)<=12):
            if(nombre.isalnum() == True):
                valido = True
            else:
                valido = False
                print("\nEl nombre de usuario puede contener sólo letras y números")
        else:
            valido = False
            print("\nEl nombre de usuario no puede contener más de 12 caracteres")
    else:
        valido = False
        print("\nEl nombre de usuario debe contener al menos 6 caracteres")
    return valido

def main():
    nombre = input("Ingrese el nombre de usuario: ")
    if(validar_nombre_usuario(nombre) == True):
        print("\nEl nombre de usuario "+str(nombre)+" es correcto")

if __name__ == "__main__":
    main()