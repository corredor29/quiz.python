
from utils.screenControllers import *
from utils.helpers import *

ARCHIVO_INGREDIENTES = "./data/ingredientes.json"

def cargar_ingredientes():
    if not os.path.exists(ARCHIVO_INGREDIENTES):
        return []

    with open(ARCHIVO_INGREDIENTES, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de ingredientes no contiene un JSON válido.")
            return []



def registrar_ingredientes():
    """Registra un nuevo libro con validaciones e ID único."""
    ingredientes = leer_json(ARCHIVO_INGREDIENTES)
    
    print("\n=== REGISTRAR NUEVO INGREDIENTE ===")

    while True:
        # Validación del ingrediente
        nombre_ingrediente = input("Ingresa el nombre del libro: ").strip()
        if not nombre_ingrediente:
            print("Error: El nombre no puede estar vacío")
            continue
        if any(ingredientes["nombre"].lower() == nombre_ingrediente.lower() for ingredientes in ingredientes):            
            print("Error: Este ingrediente ya existe. Ingrese uno nuevo.")
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

        # Validación de la valoración
        while True:
            try:
                stock = input("Ingresa el stock: ").strip()
                if not stock:
                    stock = "Sin stockr"
                    break
                stock = int(stock)
                if 1 <= stock :
                    stock = f"{stock}"
                    break
            except ValueError:
                print("Error: Debes ingresar un número entero")

        # Guardar el libro con ID
        nuevo_ingrediente = {
            "nombre": nombre_ingrediente,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
        }
        agregar_diccionario_a_json(ARCHIVO_INGREDIENTES, nuevo_ingrediente)
        print(f"\ningrediente '{nombre_ingrediente}' registrado exitosamente .")
        break

def mostrar_libros():
    """Muestra todos los libros en formato de tabla con ID."""
    ingrediente = leer_json(ARCHIVO_INGREDIENTES)
    
    if not ingrediente:
        print("\nNo hay ingrediente registrados.")
        return
    


    
    print("\n=== LISTA DE INGREDIENTES ===")
    print(f" {'nombre':<15} {'descripcion':<15} {'precio':<15} {'stock':<10} ")
    print("-" * 95)
    
    print(f"\nTotal de ingredientes: {len(ingrediente)}")

