#---------------------------------------------
#   Función para insertar caracter
#   entre cada letra de la cadena
#---------------------------------------------
def insertar_caracter(cadena, caracter):
    resultado = ""
    while cont < len(cadena):
        cadena.append(caracter,cont+1)
        cont+=1
    return cadena
#---------------------------------------------
#   Función para reemplazar todos
#   los espacios por caracter _
#---------------------------------------------
def reemplazar_espacios(cadena, caracter):
    resultado = cadena.replace(" ",caracter)
    return resultado

#---------------------------------------------
#   Función para reemplazar los
#   digitos en la cadena por caracter
#---------------------------------------------
def reemplazar_digitos(cadena, caracter):
    for car in cadena:
        cadena.replace()
        print(car.isnumeric())
        if car.isnumeric() == True:
            res = cadena.replace(str(car),str(caracter))
    return res
            

#---------------------------------------------
#   Función para insertar caracter
#   cada 3 dígitos en una cadena
#---------------------------------------------
def insertar_caracter_3digitos(cadena, caracter):
    cont = 0
    pos = 3
    veces = len(cadena)//3
    while cont < veces:
        cadena[:pos] + caracter + cadena[pos:] 
        cont+=1
        pos+=(3+cont)
    return cadena

def main():
    print(reemplazar_digitos("clave 123","x"))
    
if __name__ == "__main__":
    main()
    

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