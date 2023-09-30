from ProcesosAux import obtener_categoria
class Producto:
    def __init__(self, nombre: str, cantidad: int, precio: float, categoria: int):
        self.__nombre= nombre
        self.__cantidad= cantidad
        self.__precio= precio
        self.__categoria= categoria
    
    def __repr__(self) -> str:
        return (
            f'Nombre: {self.__nombre} \n'
            f'Cantidad: {self.__cantidad} \n'
            f'Precio: {self.__precio} \n'
            f'Categoria: {obtener_categoria(self.__categoria)}'
        )