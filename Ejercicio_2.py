def ejercicio():
    n = int(input("\nIngrese la cantidad de números positivos que desea ingresar: "))

    while n < 0:
        print("\nTiene que ser un entero positivo")
        n = int(input("\nIngrese la cantidad de números positivos que desea ingresar: "))

    cont = 0

    while cont <= n:
        num = int(input(f"\nIngrese el número {cont+1}: "))
    
        while num < 0:
            print("\nTiene que ser un entero positivo")
            num = int(input(f"\nIngrese el número {cont+1}: "))

        cont += 1

    print("\nNúmeros ingresados correctamente")

def main():
    ejercicio()

if __name__ == "__main__":
    main()