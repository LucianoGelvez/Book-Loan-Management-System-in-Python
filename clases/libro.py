class Libro:
    def __init__(self, nombre, autor, numero_serie):
        self.nombre = nombre
        self.autor = autor
        self.numero_serie = numero_serie

    def __str__(self):
        return f"El nombre del libro es {self.nombre} y su autor es {self.autor} además su número de serie es:{self.numero_serie}."
    
    def registrar_libro():
        nombre = input("Por favor ingrese el nombre del libro: ")
        autor = input("Por favor ingrese el autor del mismo: ")
        numero_serie = input("Ingrese el número de serie para terminar: ")
        
        libro = Libro(nombre, autor, numero_serie)
        if libro:
            return libro
        
    def traer_libro(list_libros):
        numero_serie = input("Escribe el número de serie del libro que requieres información: ")
        for libro in list_libros:
            if libro.numero_serie == numero_serie:
                print(libro)
            else:
                print("No se encontró el libro que buscabas")
        
            
        

    

    
