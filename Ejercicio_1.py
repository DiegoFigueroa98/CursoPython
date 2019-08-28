def pedirNumeroEntero():
    correcto = False
    while(not correcto):
        try:
            num = int(input("\nIngrese un número entero: "))
            correcto = True
        except ValueError:
            print('\nError, tiene que ser un número entero')
    return num

def ejercicio():
    num1 = pedirNumeroEntero()
    num2 = pedirNumeroEntero()

    while num2 <= num1:
        print("\nError, el segundo número NO es mayor que el primero")
        num2 = pedirNumeroEntero()

    print(f"\nNúmero 1: {num1}")
    print(f"\nNúmero 2: {num2}")

def main():
    ejercicio()

if __name__ == "__main__":
    main()