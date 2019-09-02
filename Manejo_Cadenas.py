#---------------------------------------------
#   Función para calcular el número de renglones
#   y letras de un documento de texto
#---------------------------------------------
def contarRenglones():
    archivo = open('texto.txt', 'r')
    numLineas = len(archivo.readlines())

    #Posiciona el puntero en el inicio del archivo
    archivo.seek(0)
    arch = archivo.read()
    numLetras = len(arch)

    archivo.seek(0)
    arch = archivo.read()
    numPal = len(arch.split())

    print(f"El archivo tiene {numLineas} renglones, {numPal} palabras y {numLetras} letras")
    archivo.close()

if __name__ == "__main__":
    contarRenglones()

'''
mensaje = "Hola mundo"
mensaje = "¡"+mensaje+", Buenos días!"
print(mensaje)
print(mensaje*3)
longitud = len(mensaje)
print(mensaje.find("H"))
print(mensaje.upper())
print(mensaje.lower())
print(mensaje.replace("m","M"))
print(mensaje[0:3])
print(mensaje[3:(len(mensaje))])
'''