from utils.screenControllers import *
from utils.helpers import *
from .categoria import*
from .chef import *
import json
import os
ARCHIVO_HAMBURGUESA = "./data/hamburgeesa.json"

def cargar_hamburguesa():
    if not os.path.exists(ARCHIVO_HAMBURGUESA):
        return []

    with open(ARCHIVO_HAMBURGUESA, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de hamburguesa no contiene un JSON válido.")
            return []
        
def registrar_hamburguesa():
    """Registra unahamburguesa nueva."""
    hamburguesas = leer_json(ARCHIVO_HAMBURGUESA)
    
    print("\n=== REGISTRAR NUEVA HAMBURGUESA===")
    

    while True:
        # Validación de la hamburguesa
        nombre_hamburguesa = input("Ingresa el nombre de la hamburguesa: ").strip()
        if not nombre_hamburguesa:
            print("Error: El nombre no puede estar vacío")
            continue
        if any(hamburguesa["nombre"].lower() == nombre_hamburguesa.lower() for hamburguesa in hamburguesas):            
            print("Error: Esta hamburguesa ya existe. Ingrese una nueva hamburguesa.")
            continue

        # Validación del autor
        categoria = print(ARCHIVO_CATEGORIA)
        categoria = input("Ingresa la categoria de la hamburguesa: ").strip()


        ingredientes = input("Ingrese los ingredientes que lleva la hamburguesa: ").strip()
        if not ingredientes:
            print("Error: los ingredientes no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in categoria):
            print("Error: los ingredientes no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in categoria):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue



        # Validación de la valoración
        while True:
            try:
                precio = input("Ingresa el precio del ingrediente: ").strip()
                if not precio:
                    precio = "ingresar precio"
                    break
                precio = int(precio)
                if 1 <= precio <= 10000:
                    precio = f"${precio}"
                    break
            except ValueError:
                print("Error: Debes ingresar un número entero")

        chef = print(ARCHIVO_CHEF)
        chef = input("Ingrese el nombre del chef que creo la hamburguesa: ").strip()
        if not chef:
            print("Error: el chef no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in categoria):
            print("Error: el chef no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in categoria):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue

        nuevo_hamburguesa = {
            "nombre": nombre_hamburguesa,
            "categoria": categoria,
            "ingredientes": ingredientes,
            "precio": precio,
            "chef": chef,

        }
        agregar_diccionario_a_json(ARCHIVO_HAMBURGUESA, nuevo_hamburguesa)
        print(f"\nhamburguesa '{nombre_hamburguesa}' registrado exitosamente .")
        break

def mostrar_hamburguesa():
    """Muestra todos los libros en formato de tabla con ID."""
    hamburguesa = leer_json(ARCHIVO_HAMBURGUESA)
    
    if not hamburguesa:
        print("\nNo hay hamburguesas registradas.")
        return
    


    
