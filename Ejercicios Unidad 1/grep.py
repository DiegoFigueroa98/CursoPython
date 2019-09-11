#---------------------------------------------
#   Función que dado una expresion
#   identificar en qué linea aparece
#   e imprimir la línea de texto
#---------------------------------------------

def encontrar_Expresion(expresion):
    archivo = open("texto.txt","r")
    texto = archivo.readlines()
    archivo.close()
    cont = 0
    for linea in texto:
        if (linea.find(expresion) != -1):
            print("\n"+linea)
            cont+=1
    if (cont == 0):
        print("\nNo se encontraron oraciones con la expresion "+expresion)

def main():
    expresion = input("Ingrese una expresión a buscar: ")
    encontrar_Expresion(expresion)

if __name__ == "__main__":
    main()