from utils.screenControllers import *
from utils.helpers import *

ARCHIVO_CHEF = "./data/chef.json"

def cargar_chef():
    if not os.path.exists(ARCHIVO_CHEF):
        return []

    with open(ARCHIVO_CHEF, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de chef no contiene un JSON válido.")
            return []


def registrar_chef():
    """Registra un nuevo libro con validaciones e ID único."""
    chefs = leer_json(ARCHIVO_CHEF)
    
    print("\n=== REGISTRAR NUEVO CHEF ===")
    
    while True:
        nombre_chef = input("Ingresa el nombre del chef: ").strip()
        if not nombre_chef:
            print("Error: El nombre no puede estar vacío")
            continue
        if any(chef["nombre"].lower() == nombre_chef.lower() for chef in chefs):            
            print("Error: Este chef ya existe. Ingrese uno nuevo.")
            continue


        especialidad = input("Ingresa la especialidad del chef: ").strip()
        if not especialidad:
            print("Error: El la especialidad no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in especialidad):
            print("Error: la especialidad no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in especialidad):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue


        nuevo_chef = {
            "nombre": nombre_chef,
            "especialidad": especialidad,
        }
        agregar_diccionario_a_json(ARCHIVO_CHEF, nuevo_chef)
        print(f"\nresgistrado '{nombre_chef}' registrado exitosamente")
        break

def mostrar_chef():
    """Muestra todos los libros en formato de tabla con ID."""
    chefs = leer_json(ARCHIVO_CHEF)
    
    if not chefs:
        print("\nNo hay libros registrados.")
        return
    