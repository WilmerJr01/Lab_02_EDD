import sys
import time
from Tienda import Tienda
from ProcesosAux import limpiar
from ProcesosAux import imprimir
from ProcesosAux import opcionValida
from ProcesosAux import verificar_contraseña

def animacion():
    carrito = "🕹️"
    espacio_vacio = " " * len(carrito)
    ancho_pantalla = 50
    correr=True
    while correr:
        for i in range(ancho_pantalla, -1, -1):
            desplazamiento = " " * i + carrito + espacio_vacio
            sys.stdout.write("\r" + desplazamiento)
            sys.stdout.flush()
            time.sleep(0.05)
        correr= False

def menu_Usuario(tienda: Tienda):
    fin_usuario= True
    while fin_usuario:
        limpiar()
        imprimir("----------------  🎮  Bienvenido a Game Stock  🎮  ----------------", "amarillo")
        imprimir("-----------------------  🕹️   Usuario  🕹️  -----------------------", "amarillo")
        imprimir("1️⃣  Iniciar", "cyan")
        imprimir("2️⃣  Registrarme", "cyan")
        imprimir("0️⃣  Regresar", "cyan")
        print("(Digite número según su opción)")
        
        opcion= input(">>> Opcion: ")
        op= opcionValida(opcion, 1, 2)
        while op is False:
            imprimir("Opcion incorrecta", "rojo")
            imprimir("⚠️  Nota: ", "amarillo")
            print("(Digite (1) si ya tiene una cuenta)")
            print("(Digite (2) si aún no tiene una cuenta)")
            print("(Digite (0) para volver al menú inicial)")
            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 1,2)
        
        if opcion == "1":
            imprimir("Ingrese su usuario: ", "magenta")
            usuario= input(">>> ")
            imprimir("Ingrese su contraseña: ", "magenta")
            contraseña= input(">>> ")
            Usuarios_Registrados= tienda.get_Usuarios()
            for Usuario_Registrado in Usuarios_Registrados:
                if Usuario_Registrado.get_usuario == usuario and Usuario_Registrado.get_contraseña == contraseña:
                    #iniciarSesion(tienda, usuario, contraseña)#
                    imprimir("Iniciado correctamente", "verde")
                else:
                    imprimir("❌  No se pudo iniciar sesión","rojo")
            animacion()
        elif opcion == "2":
            imprimir("Ingrese su nombre: ", "magenta")
            nombre= input(">>> ")
            imprimir("Ingrese su apellido: ", "magenta")
            apellido= input(">>> ")
            imprimir("Ingrese su usuario: ", "magenta")
            usuario= input(">>> ")
            imprimir("Ingrese su contraseña: ", "magenta")
            contraseña= input(">>> ")
            Usuarios_Registrados= tienda.get_Usuarios()
            
            verificar_usuario= True
            for Usuario_Registrado in Usuarios_Registrados:
                if Usuario_Registrado.get_usuario == usuario:
                    verificar_usuario= False
            
            if verificar_contraseña(contraseña) and verificar_usuario:
                with open('Usuarios_Registrados', 'a') as archivo:
                    archivo.write(f"{nombre},{apellido},{usuario},{contraseña}")