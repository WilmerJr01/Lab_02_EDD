from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, usuario: str, contraseña: str):
        self._nombre= nombre
        self._apellido= apellido
        self._usuario= usuario
        self._contraseña= contraseña
    
    @abstractmethod
    def iniciarSesion(self, usuario: str, contraseña: str)->bool:
        pass
    
    @abstractmethod
    def cerrarSesion(self)->bool:
        pass
    

class Manager(Persona):
    def __init__(self, nombre: str, apellido: str, usuario: str, contraseña: str, ID: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self.__ID = ID
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_usuario(self):
        return self._usuario
    
    def get_contraseña(self):
        return self._contraseña
    
    def get_ID(self):
        return self.__ID
    
    def iniciarSesion(self, usuario: str, contraseña: str) -> bool:
        print("Inicio de sesión fallido")

    def cerrarSesion(self) -> bool:
        print("Sesión cerrada para el usuario")

class Usuario(Persona):
    def __init__(self, nombre: str, apellido: str, usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self.__Carrito = []
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_usuario(self):
        return self._usuario
    
    def get_contraseña(self):
        return self._contraseña
    
    def get_Carrito(self):
        return self.__Carrito
    
    def iniciarSesion(self, usuario: str, contraseña: str) -> bool:
        print("Sesion Iniciada")

    def cerrarSesion(self) -> bool:
        print("Sesión Cerrada")
    
    def __repr__(self) -> str:
        return (
            f'Nombre: {self._nombre} \n'
            f'Apellido: {self._apellido} \n'
            f'Usuario: {self._usuario} \n'
            f'Contraseña: {self._contraseña}'
        )