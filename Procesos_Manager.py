from Tienda import Tienda
from Personas import Manager
from ProcesosAux import limpiar
from ProcesosAux import imprimir
from ProcesosAux import opcionValida
from ProcesosAux import verificar_contraseña
from ProcesosAux import verificar_solo_letras
from ProcesosAux import verificar_solo_numeros
from ProcesosAux import verificar_sin_espacios
from ProcesosAux import animacion

def menu_Manager(tienda: Tienda):
    fin_usuario= True
    while fin_usuario:
        limpiar()
        imprimir("----------------  🎮  Bienvenido a Game Stock  🎮  ----------------", "amarillo")
        imprimir("--------------------  🕹️   >Administrador<  🕹️  ---------------------", "amarillo")
        imprimir("1️⃣  Iniciar Sesión", "cyan")
        imprimir("2️⃣  Registrarme", "cyan")
        imprimir("0️⃣  Regresar", "cyan")
        print("(Digite número según su opción)")
        
        opcion= input(">>> Opcion: ")
        op= opcionValida(opcion, 0, 2)
        while op is False:
            imprimir("Opcion incorrecta", "rojo")
            imprimir("⚠️  Nota: ", "amarillo")
            print("(Digite (1) si ya tiene una cuenta)")
            print("(Digite (2) si aún no tiene una cuenta)")
            print("(Digite (0) para volver al menú inicial)")
            print("(Digite (3) para cerrar el programa)")
            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 0,2)
        
        if opcion == "1":
            imprimir("Ingrese su usuario: ", "magenta")
            usuario= input(">>> ")
            imprimir("Ingrese su contraseña: ", "magenta")
            contraseña= input(">>> ")
            Managers_Registrados= tienda.get_Managers()
            iniciar= False
            for Manager_Registrado in Managers_Registrados:
                if Manager_Registrado.get_usuario() == usuario and Manager_Registrado.get_contraseña() == contraseña:
                    manager_para_iniciar= Manager_Registrado
                    iniciar= True
            if iniciar:
                imprimir("Iniciando Sesion...", "verde")
                animacion("🔒")
                a = iniciarSesion(tienda, manager_para_iniciar)
                if a == False:
                    return False
            else:
                imprimir("❌  No se pudo iniciar sesión","rojo")
            animacion("🕹️")
        
        elif opcion == "2":
            imprimir("Ingrese su ID en la empresa: ", "magenta")
            ID= input(">>> ")
            valido= verificar_solo_numeros(ID)
            while valido==False:
                imprimir("El ID dentro de nuestra empresa solo pueden ser números", "rojo")
                ID= input(">>> ")
                valido = verificar_solo_numeros(ID)
            
            imprimir("Ingrese su nombre: ", "magenta")
            nombre= input(">>> ")
            valido= verificar_solo_letras(nombre)
            while valido==False:
                imprimir("El nombre solo puede tener letras y no puede ser vacio", "rojo")
                nombre= input(">>> ")
                valido = verificar_solo_letras(nombre)
            
            imprimir("Ingrese su apellido: ", "magenta")
            apellido= input(">>> ")
            valido= verificar_solo_letras(apellido)
            while valido==False:
                imprimir("El apellido solo puede tener letras y no puede ser vacio", "rojo")
                apellido= input(">>> ")
                valido = verificar_solo_letras(apellido)
            
            imprimir("Ingrese su usuario: ", "magenta")
            usuario= input(">>> ")
            valido= verificar_sin_espacios(usuario)
            while valido==False:
                imprimir("El usuario no puede ser vacio ni tener espacios", "rojo")
                usuario= input(">>> ")
                valido = verificar_sin_espacios(usuario)
            
            imprimir("Ingrese su contraseña: ", "magenta")
            contraseña= input(">>> ")
            
            Managers_Registrados= tienda.get_Managers()
            
            verificar_usuario= True
            for Manager_Registrado in Managers_Registrados:
                if Manager_Registrado.get_usuario() == usuario:
                    verificar_usuario= False
            
            if verificar_contraseña(contraseña) and verificar_usuario:
                with open('Manager_Registrados.txt', 'a') as archivo:
                    archivo.write(f"{nombre},{apellido},{usuario},{contraseña},{ID}\n")
                nuevo_manager= Manager(nombre, apellido, usuario, contraseña, ID)
                tienda.add_Manager(nuevo_manager)
                imprimir("Registrado Correctamente", "verde")
            else:
                imprimir("❌  No se pudo registrar","rojo")
                if verificar_contraseña(contraseña) == False:
                    imprimir("⚠️  La contraseña tiene que tener: ","rojo")
                    imprimir("Minimo 8 caracteres","rojo")
                    imprimir("Minimo 1 Caracter Especial","rojo")
                    imprimir("Minimo 1 Letra","rojo")
                    imprimir("Minimo 1 Digito","rojo")
                if verificar_usuario== False:
                    imprimir("⚠️  Su usuario ya existe","rojo")
            animacion("🔐")
        elif opcion == "0":
            fin_usuario= False
            print("Volviendo al menú principal...")
            animacion("⬅️")

def iniciarSesion(tienda: Tienda, manager: Manager):
    fin_sesion= True
    limpiar()
    while fin_sesion:
        imprimir(f"----------------  🎮  Hola {manager.get_nombre()}  🎮  ----------------", "amarillo")
        imprimir(f"----------------  🕹️   >ID: {manager.get_ID()}<  🕹️  ----------------", "amarillo")
        imprimir("1️⃣  Editar Inventario", "cyan")
        imprimir("2️⃣  Visualizar Ganancias", "cyan")
        imprimir("3️⃣  Cerrar Programa", "cyan")
        imprimir("0️⃣  Cerrar Sesion", "cyan")
        
        print("(Digite número según su opción)")
        
        opcion= input(">>> Opcion: ")
        op= opcionValida(opcion, 0, 3)
        while op is False:
            imprimir("Opcion incorrecta", "rojo")
            imprimir("⚠️  Nota: ", "amarillo")
            print("(Digite (1) para ver el inventario)")
            print("(Digite (2) para visualizar las ganancias del dia)")
            print("(Digite (3) para cerrar el programa)")
            print("(Digite (0) para cerrar sesion)")

            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 0,3)
        
        if opcion == "1":
            pass
        elif opcion== "2":
            pass
        elif opcion== "3":
            #Cosas Antes de cerrar el programa#
            return False
        elif opcion== "0":
            print("Cerrando Sesion...")
            animacion("⏪")
            fin_sesion= False