class Libro(object):
    def __init__(self, autor_apellido, autor_nombre, titulo, lugar, editorial, year):
        self.autor_apellido = autor_apellido
        self.autor_nombre = autor_nombre
        self.titulo = titulo
        self.editorial = editorial
        self.lugar = lugar
        self.year = year

    def escribe_entrada_bibliografica(self):
        return self.autor_apellido + ", " + self.autor_nombre + ", " + self.titulo + \
            ", " + self.editorial + ", " + self.lugar + ", " + self.year + ", " + self.autor_year + "."
    
    def hacer_autor_year(self):
        self.autor_year  = self.autor_apellido + " (" + self.year + ")"
        
        
class Articulo(object):
    def __init__(self, autor_apellido, autor_nombre, titulo, volumen, paginas, lugar, year):
        self.autor_apellido = autor_apellido
        self.autor_nombre = autor_nombre
        self.titulo = titulo
        self.lugar = lugar
        self.year = year
        self.volumen = volumen
        self.paginas = paginas

    def escribe_entrada_bibliografica(self):
        return self.autor_apellido + ", " + self.autor_nombre + ", " + self.titulo + \
            ", " + self.volumen + ", " + self.paginas + ", " + \
            ", " + self.lugar + ", " + self.year + ", " + self.autor_year + "."
    
    def hacer_autor_year(self):
        self.autor_year  = self.autor_apellido + " (" + self.year + ")"


def main():
    belleza = Libro("Dubay","Thomas","The Evidential Power o Beuty", "San Francisco", "Ignatius Press", "2010")
    programacion_python = Libro("Martelli", "Alex", "Python in a Nutshell", "sebastopol,CA", "O'Reilly Media, Inc.","2003")
    print("Apellido del Autor:", belleza.autor_apellido)
    print("Nombre del Autor:", belleza.autor_nombre)
    
    articuloDiego = Articulo("Figueroa","Diego","Python POO","1","20","colima","2019")
    Articulo.hacer_autor_year(articuloDiego)
    print(Articulo.escribe_entrada_bibliografica(articuloDiego))

if __name__ == "__main__":
    main()