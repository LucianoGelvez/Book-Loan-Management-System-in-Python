

from clases.libro import Libro
from clases.prestamo import Prestamo
from clases.usuario import Usuario

def main():
    
    print("Bienvenido a Ph la biblioteca en salsa")

    list_usuarios = []
    list_libros = []
    list_prestamos = []


    while True:
        print("Escoja una opción: ")
        print("1 - Crear Usuario")
        print("2 - Actualizar correo de Usuario")
        print("3 - Registrar Libro")
        print("4 - Mostrar informacion del Libro")
        print("5 - Mostrar informacion del usuario")
        print("6 - Sacar libro prestado")
        print("7 - Mostrar información de los prestamos de libro")
        print("8 - Salir")

        opcion = int(input(""))

        if opcion == 1:
            usuario = Usuario.registro_usuarios()
            list_usuarios.append(usuario)
            print("Se a creado correctamente el usuario")
   
        elif opcion == 2:
            list_usuarios = Usuario.actualizar(list_usuarios)
        elif opcion == 3:
            libro = Libro.registrar_libro()
            if libro:
                list_libros.append(libro)
        elif opcion == 4:
            Libro.traer_libro(list_libros)
        elif opcion == 5:
            Usuario.traer_usuario(list_usuarios)
        elif opcion == 6:
            prestamo = Prestamo.registrar_prestamo(list_usuarios, list_libros)
            if prestamo:
                list_prestamos.append(prestamo)
                print(list_prestamos)
        elif opcion == 7:
            for prestamo in list_prestamos:
                print(prestamo)
        elif opcion == 8:
            print("Gracias, vuelva pronto..")
            break

        else: 
            print("Has colocado una opción que no se encuentra en el menú")
            
        
if __name__ == "__main__":
    main()
        





