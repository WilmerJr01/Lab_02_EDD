import os
import platform
import sys
import time

def verificar_solo_numeros(cadena):
    # Verifica si la cadena no está vacía y si contiene solo números
    if cadena and cadena.isdigit():
        return True
    else:
        return False

def verificar_solo_letras(cadena):
    # Verifica si la cadena no está vacía y si contiene solo letras (sin espacios ni otros caracteres)
    if cadena and cadena.isalpha():
        return True
    else:
        return False

def verificar_sin_espacios(cadena):
    # Verifica si la cadena no está vacía y si no contiene espacios en blanco
    if cadena and ' ' not in cadena:
        return True
    else:
        return False

def imprimir(texto, color):
    # Definir códigos ANSI para cambiar el color del texto
    colores = {
        "rojo": "\033[91m",
        "verde": "\033[92m",
        "amarillo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blanco": "\033[97m",
        "reset": "\033[0m"  # Restablece el color a su valor predeterminado
    }

    # Imprime el texto con el color especificado
    if color in colores:
        print(colores[color] + texto + colores["reset"])

def verificar_contraseña(cadena):
    # Verificar si la cadena tiene al menos 8 caracteres
    if len(cadena) < 8:
        return False

    # Inicializar contadores para números, letras y caracteres especiales
    num_count = 0
    letra_count = 0
    especial_count = 0

    # Caracteres especiales permitidos
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

    # Iterar a través de la cadena
    for caracter in cadena:
        if caracter.isdigit():
            num_count += 1
        elif caracter.isalpha():
            letra_count += 1
        elif caracter in caracteres_especiales:
            especial_count += 1
        elif caracter.isspace():
            return False  # Si contiene espacios, no cumple con el requisito

    # Verificar si cumple con los requisitos
    if num_count >= 1 and letra_count >= 1 and especial_count >= 1:
        return True
    else:
        return False

def obtener_categoria(numero):
    categorias = [
        'RPG',
        'Shooter',
        'Multijugador',
        'Aventura',
        'Sandbox',
        'Battle Royale',
        'Deportes',
        'Mundo Abierto',
        'Simulación',
        'MOBA',
        'Acción',
        'Survival'
    ]
    
    if 1 <= numero <= 12:
        return categorias[numero - 1]
    else:
        return 'Desconocida'

def limpiar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def opcionValida(opcion, a, b):
    if opcion.isdigit():
        numero = int(opcion)
        return a <= numero <= b
    return False


def animacion(a: str):
    carrito = a
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