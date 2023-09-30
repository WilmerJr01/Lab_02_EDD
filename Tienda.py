from Personas import Usuario
from Personas import Manager
from Producto import Producto
class Tienda: 
    def __init__(self):
        self.__Usuarios = []
        self.__Managers= []
        self.__Productos= []
    
    def add_Usuario(self, usuario: Usuario):
        self.__Usuarios.append(usuario)
    
    def get_Usuarios(self):
        return self.__Usuarios
    
    def get_Productos(self):
        return self.__Productos
    
    def get_Managers(self):
        return self.__Managers
    
    def cargar_usuarios(self):
        try:
            with open('Usuarios_Registrados.txt', 'r') as file:
                for line in file:
                    nombre, apellido, usuario, contraseña = line.strip().split(',')
                    nuevo_usuario = Usuario(nombre, apellido, usuario, contraseña)
                    self.__Usuarios.append(nuevo_usuario)
            print("Usuarios cargados exitosamente.")
        except FileNotFoundError:
            print(f"El archivo Usuarios_Registrados.txt no se encontró.")
        except Exception as e:
            print(f"Se produjo un error al cargar usuarios: {str(e)}")

    def cargar_managers(self):
        try:
            with open('Manager_Registrados.txt', 'r') as file:
                for line in file:
                    nombre, apellido, usuario, contraseña, ID = line.strip().split(',')
                    nuevo_manager = Manager(nombre, apellido, usuario, contraseña, ID)
                    self.__Managers.append(nuevo_manager)
            print("Managers cargados exitosamente.")
        except FileNotFoundError:
            print(f"El archivo Manager_Registrados.txt no se encontró.")
        except Exception as e:
            print(f"Se produjo un error al cargar usuarios: {str(e)}")

    def cargar_productos(self):
        try:
            with open('Productos.txt', 'r') as file:
                for line in file:
                    nombre, cantidad, precio, categoria = line.strip().split(',')
                    nuevo_producto = Producto(nombre, cantidad, precio, categoria)
                    self.__Productos.append(nuevo_producto)
            print("Productos cargados exitosamente.")
        except FileNotFoundError:
            print(f"El archivo Productos.txt no se encontró.")
        except Exception as e:
            print(f"Se produjo un error al cargar usuarios: {str(e)}")