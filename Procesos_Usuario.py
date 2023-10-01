from Personas import Usuario
from Tienda import Tienda
from ProcesosAux import limpiar
from ProcesosAux import imprimir
from ProcesosAux import opcionValida
from ProcesosAux import verificar_contraseña
from ProcesosAux import verificar_solo_letras
from ProcesosAux import verificar_sin_espacios
from ProcesosAux import animacion

def menu_Usuario(tienda: Tienda):
    fin_usuario= True
    while fin_usuario:
        limpiar()
        imprimir("----------------  🎮  Bienvenido a Game Stock  🎮  ----------------", "amarillo")
        imprimir("-----------------------  🕹️   >Cliente<  🕹️  ------------------------", "amarillo")
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
            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 0,2)
        
        if opcion == "1":
            imprimir("Ingrese su usuario: ", "magenta")
            usuario= input(">>> ")
            imprimir("Ingrese su contraseña: ", "magenta")
            contraseña= input(">>> ")
            Usuarios_Registrados= tienda.get_Usuarios()
            iniciar= False
            for Usuario_Registrado in Usuarios_Registrados:
                if Usuario_Registrado.get_usuario() == usuario and Usuario_Registrado.get_contraseña() == contraseña:
                    usuario_para_iniciar= Usuario_Registrado
                    iniciar= True
            if iniciar:
                imprimir("Iniciado correctamente", "verde")
                animacion("🔒")
                iniciarSesion(tienda, usuario_para_iniciar)
            else:
                imprimir("❌  No se pudo iniciar sesión","rojo")
            animacion("🕹️")
        
        elif opcion == "2":
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
            
            Usuarios_Registrados= tienda.get_Usuarios()
            
            verificar_usuario= True
            for Usuario_Registrado in Usuarios_Registrados:
                if Usuario_Registrado.get_usuario() == usuario:
                    verificar_usuario= False
            
            if verificar_contraseña(contraseña) and verificar_usuario:
                with open('Usuarios_Registrados.txt', 'a') as archivo:
                    archivo.write(f"{nombre},{apellido},{usuario},{contraseña}\n")
                nuevo_usuario= Usuario(nombre, apellido, usuario, contraseña)
                tienda.add_Usuario(nuevo_usuario)
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

def iniciarSesion(tienda: Tienda, usuario: Usuario):
    fin_sesion= True
    limpiar()
    while fin_sesion:
        imprimir(f"----------------  🎮  Hola {usuario.get_nombre()}  🎮  ----------------", "amarillo")
        imprimir(f"----------------  🕹️   >Carrito: {len(usuario.get_Carrito())}<  🕹️  ----------------", "amarillo")
        imprimir("1️⃣  Ver Productos", "cyan")
        imprimir("2️⃣  Filtrar Productos", "cyan")
        imprimir("3️⃣  Ver Carrito", "cyan")
        imprimir("4️⃣  Pagar", "cyan")
        imprimir("0️⃣  Cerrar Sesion", "cyan")
        
        print("(Digite número según su opción)")
        
        opcion= input(">>> Opcion: ")
        op= opcionValida(opcion, 0, 4)
        while op is False:
            imprimir("Opcion incorrecta", "rojo")
            imprimir("⚠️  Nota: ", "amarillo")
            print("(Digite (1) si quiere ver los productos de la tienda)")
            print("(Digite (2) si quiere añadir un filtro)")
            print("(Digite (3) si quiere ver su carrito)")
            print("(Digite (4) si quiere pagar)")
            print("(Digite (0) si quiere cerrar sesion)")
            
            opcion = input(">>> Opcion: ")
            op = opcionValida(opcion, 0,4)
        
        if opcion == "1":
            pass
        elif opcion== "2":
            pass
        elif opcion== "3":
            pass
        elif opcion== "4":
            pass
        elif opcion== "0":
            print("Cerrando Sesion...")
            animacion("⏪")
            fin_sesion= False