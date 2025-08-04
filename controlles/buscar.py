from .ingredientes import ARCHIVO_INGREDIENTES as archivo_ingredientes
from .hamburguesa import ARCHIVO_HAMBURGUESA as archivo_hamburguesa
from .chef import ARCHIVO_CHEF as archivo_chef
from .categoria import ARCHIVO_CATEGORIA as archivo_categoria
from utils.helpers import leer_json


def buscar(termino, tipo):
    bander = True
    try:
        # ingredientes

        ingredientes = leer_json(archivo_ingredientes)
        for ingrediente in ingredientes:
            if ingrediente[tipo] == termino:
                bander = False
                print("="*20, "ingrediente encontrado", "="*20)
                print(f" {'nombre':<15} {'descripcion':<15} {'precio':<15} {'stock':<10} ")
                print("-" * 95)

                print(f" {ingrediente['nombre']:<15} {ingrediente['descriccion']:<15} "
                        f"{ingrediente['precio']:<15} {ingrediente.get('stock'):<10} ")

        # chef
        chefs = leer_json(archivo_chef)
        for chef in chefs:
            if chef[tipo] == termino:
                bander = False
                print("="*20, "chef encontrado", "="*20)
                print(f" {'nombre':<15} {'especialidad':<15} ")
                print("-" * 95)

                print(f" {chef['nombre']:<15} {chef['especialidad']:<15} ")
        # Categoria
        categorias = leer_json(archivo_categoria)
        for categoria in categorias:
            if categoria[tipo] == termino:
                bander = False
                print("="*20, "categoria encontrado", "="*20)
                print(f" {'categoria':<15} {'descripccion':<15} ")
                print("-" * 95)

                print(f" {categoria['categoria']:<15} {categoria['descripccion']:<15} ")

        # Hamburguesa
        hamburguesas = leer_json(archivo_hamburguesa)
        for hamburguesa in   hamburguesas :
            if hamburguesa[tipo] == termino:
                bander = False
                print("="*20, "hamburguesa encontrado", "="*20)
                print(f" {'nombre':<15} {'categoria':<15} {'precio':<15} {'chef':<10} ")
                print("-" * 95)

                print(f" {hamburguesa['nombre']:<15} {hamburguesa['categoria']:<15} "
                        f"{hamburguesa['precio']:<15} {hamburguesa.get('chef'):<10} ")
        if bander:
            print("No se encontraron resultados.")
    except Exception as e:
        print(f"\nError en la edición: {str(e)}")