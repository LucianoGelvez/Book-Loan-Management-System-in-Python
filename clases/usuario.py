class Usuario:
    def __init__(self, nombre, apellido, matricula, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.correo = correo
        self.prestamos = 3

    def __str__(self):
        return f"El usuario es {self.nombre + self.apellido} con número de matrícula: {self.matricula} y correo {self.correo}"

    def registro_usuarios():
        nombre = input("Ingrese el nombre por favor: ")
        apellido = input("Ingrese el apellido por favor: ")
        matricula = input("Ingrese el número de matrícula por favor: ")
        correo = input("Ingrese el correo: ")
        correo = Usuario.validar_correo(correo)
        

        usuario = Usuario(nombre, apellido, matricula, correo)
        if usuario:
            return usuario
   
    def validar_correo(correo):
        while True:
            if "@" not in correo or len(correo) <= 3:
                print("El correo debe contener @ y mas de 3 caracteres")
                correo = input("Por favor ingrese un correo valido: ")
            else:
                break
        return correo
    
    def actualizar(list_usuarios):
        matricula_recibida= input("Porfavor coloque el número de matrícula a actualizar los datos: ")
        for usuario in list_usuarios:
            if usuario.matricula == matricula_recibida:
                nuevo_correo = input("Porfavor ingresa el nuevo correo que deseas: ")
                usuario.correo = Usuario.validar_correo(nuevo_correo)
                print("El usuario a sido actualizado exitosamente")
                break
            else:
                print("No exite un usuario con esa matricula")
        return list_usuarios
 
        
    def traer_usuario(list_usuarios):
        matricula = input("Escribe el número de matricula del usuario que requieres información: ")
        for usuario in list_usuarios:
            if usuario.matricula == matricula:
                print(usuario)
            else:
                print("No se encontró el usuario que buscabas")        