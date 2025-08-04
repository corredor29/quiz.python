from .ingredientes import ARCHIVO_INGREDIENTES as archivo_ingredientes
from .hamburguesa import ARCHIVO_HAMBURGUESA as archivo_hamburguesa
from .chef import ARCHIVO_CHEF as archivo_chef
from .categoria import ARCHIVO_CATEGORIA as archivo_categoria
from utils.helpers import leer_json
import json

def editar(termino, nuevo_dato, tipo):
    resultados = []
    try:
        # ingredientes
        ingredientes = leer_json(archivo_ingredientes) or []
        for ingrediente in ingredientes:
            if ingrediente[tipo] == termino:
                ingrediente[tipo] = nuevo_dato
                resultados.append(ingrediente)
        
        with open(archivo_ingredientes, "w") as f:
            json.dump(ingredientes, f, indent=4)

        # chef
        chefs = leer_json(archivo_chef) or []
        for chef in chefs:
            if chef[tipo] == termino:
                chef[tipo] = nuevo_dato
                resultados.append(chef)
        
        with open(archivo_chef, "w") as f:
            json.dump(chefs, f, indent=4)

        # Categoria
        categorias = leer_json(archivo_categoria) or []
        for categoria in categorias:
            if categoria[tipo] == termino:
                categoria[tipo] = nuevo_dato
                resultados.append(categoria)
        
        with open(archivo_categoria, "w") as f:
            json.dump(categorias, f, indent=4)

        # Hamburguesa
        hamburguesas = leer_json(archivo_hamburguesa) or []
        for hamburguesa in hamburguesas:
            if hamburguesa[tipo] == termino:
                hamburguesa[tipo] = nuevo_dato
                resultados.append(hamburguesa)
        
        with open(archivo_hamburguesa, "w") as f:
            json.dump(hamburguesas, f, indent=4)


    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    return resultados