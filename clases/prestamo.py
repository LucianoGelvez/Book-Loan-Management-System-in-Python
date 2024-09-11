from datetime import date
from random import randint


class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha = date.today()
        self.serial = randint(1, 10)


    def __str__(self):
        return f"El prestamo del libro fue a nombre de {self.usuario.nombre + self.usuario.apellido}, se llevo el libro {self.libro.nombre}, con fecha: {self.fecha}"
    
    def registrar_prestamo(list_usuario, list_libros):

        matricula = input("Por favor ingrese el número de matricula de usuario: ")
        usuario_prestamos = None
        libro_prestamo = None

        for usuario in list_usuario:
            if usuario.matricula == matricula:
                usuario_prestamos = usuario
                break

        numero_serie_prestamo = input("Por favor ingrese el número de serie del libro: ")

        for libro in list_libros:
            if libro.numero_serie == numero_serie_prestamo:
                libro_prestamo = libro
                break 

        prestamo = Prestamo(usuario_prestamos, libro_prestamo)    
        if prestamo:
            return prestamo
        else:
            print("Hubo un error, vuelva a intentarlo")

