from ProcesosAux import limpiar
from ProcesosAux import imprimir
from ProcesosAux import opcionValida
from Procesos_Manager import menu_Manager
from Procesos_Usuario import menu_Usuario
from Tienda import Tienda

def main():
    fin=True
    while fin:
        tienda= Tienda()
        tienda.cargar_usuarios()
        tienda.cargar_managers()
        tienda.cargar_productos()
        limpiar()
        imprimir("----------------  🎮  Bienvenido a Game Stock  🎮  ----------------", "amarillo")
        imprimir("---------  🕹️    El lugar 1° en tiendas de videojuegos  🕹️  ---------", "amarillo")
        imprimir("¿Quién quiere ingresar al sistema?", "verde")
        imprimir("1️⃣  Soy Administrator", "cyan")
        imprimir("2️⃣  Soy Usuario", "cyan")
        print("(Digite número según su opción)")
        
        opcion= input(">>> Opcion: ")
        op= opcionValida(opcion, 1, 2)
        while op is False:
            imprimir("Opcion incorrecta", "rojo")
            imprimir("⚠️  Nota: ", "amarillo")
            print("(Digite (1) si es Administrador)")
            print("(Digite (2) si es Administrador)")
            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 1,2)
        
        if opcion == "1":
            menu_Manager(tienda)
        elif opcion == "2":
            menu_Usuario(tienda)


if __name__ == "__main__":
    main()