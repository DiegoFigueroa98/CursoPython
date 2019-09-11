#---------------------------------------------
#   Función para sumar los elementos de
#   una lista entre sí
#   Devuelve el resultado de la suma
#---------------------------------------------
def sum(lista):
    suma = 0
    for i in lista:
        suma+=i
    return suma

#---------------------------------------------
#   Función para multiplicar los elementos de
#   una lista entre sí
#   Devuelve el resultado de la multiplicación
#---------------------------------------------
def mult(lista):
    mul = 1
    for i in lista:
        mul*=i
    return mul


def main():
    lista = []
    terminar = True
    lista.append(int(input("\nIngrese un número: ")))
    while terminar == True:
        lista.append(int(input("\nIngrese otro número: ")))
        letra = input("\n¿Desea agregar otro número? (s/n): ")
        if(letra.lower() != "s"):
            terminar = False 
    print("\nEl resultado de la suma es: ",sum(lista))
    print("\nEl resultado de la multiplicación es: ",mult(lista))

if __name__ == "__main__":
    main()