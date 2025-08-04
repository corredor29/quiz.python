from utils.screenControllers import *
from utils.helpers import *

ARCHIVO_CATEGORIA = "./data/categoria.json"

def cargar_categoria():
    if not os.path.exists(ARCHIVO_CATEGORIA):
        return []

    with open(ARCHIVO_CATEGORIA, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de categoria no contiene un JSON válido.")
            return []

def registrar_categoria():
    """Registra un nuevo libro con validaciones e ID único."""
    categorias = leer_json(ARCHIVO_CATEGORIA)
    
    print("\n=== REGISTRAR NUEVA CATEGORIA===")
    
    while True:
        # Validación del nombre del libro
        nombre_categoria = input("Ingresa la categoria: ").strip()
        if not nombre_categoria:
            print("Error: La categoria no puede estar vacío")
            continue
        if any(categoria["nombre"].lower() == nombre_categoria.lower() for categoria in categorias):            
            print("Error: Esta categoria ya existe. Ingrese uno nuevo.")
            continue
                # Validación del descriptor
        descripcion = input("Ingresa la descripcion del ingrediente: ").strip()
        if not descripcion:
            print("Error: la descripcion no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in descripcion):
            print("Error: la descripcion  no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in descripcion):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue

        nuevo_categoria = {
            "categoria": nombre_categoria,
            "descripccion": descripcion,
        }
        agregar_diccionario_a_json(ARCHIVO_CATEGORIA, nuevo_categoria)
        print(f"\ncategoria '{nombre_categoria}' registrada exitosamente.")
        break

def mostrar_categoria():
    """Muestra las categorias en formato de tabla ."""
    categorias = leer_json(ARCHIVO_CATEGORIA)
    
    if not categorias:
        print("\nNo hay categorias registradss.")
        return
    
    