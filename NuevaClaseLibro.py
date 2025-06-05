class Libro:
    def __init__(self, titulo, autor, anio_publicacion,cantidad,estado):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.cantidad = cantidad
        self.estado = estado


    def obtener_titulo(self):
        return self.titulo


    def prestar(self):
        if self.cantidad > 0:
            self.cantidad -= 1 
            print (f"Se ha prestado el libro {self.titulo} - Cantiad Restante: {self.cantidad}")
        else: 
            print (f"No hay Stock del libro {self.titulo} para prestar")


    def devolver(self):
        self.cantidad += 1 
        print (f"Devolvieron {self.titulo} - Cantiad disponible: {self.cantidad}")


    def mostrar(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Año de Publicacion {self.cantidad} - Estado: {self.estado}"


libro1 = Libro("Análisis Matemático", "Dysktra", 1990, 5, "Bueno")
print(libro1.mostrar())
print(libro1.obtener_titulo())
libro1.prestar()
libro1.prestar()
libro1.prestar()
libro1.prestar()
libro1.prestar()
libro1.prestar()
libro1.devolver()
libro1.devolver()
libro1.prestar()
libro1.prestar()