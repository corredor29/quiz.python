from utils.helpers import leer_json
import json

def _eliminar_elementos(archivo, campo, termino, resultados):
    datos = leer_json(archivo) or []
    encontrados = [item for item in datos if item.get(campo) == termino]
    if encontrados:
        resultados.extend(encontrados)
        nuevos_datos = [item for item in datos if item.get(campo) != termino]
        with open(archivo, "w") as f:
            json.dump(nuevos_datos, f, indent=4)

def eliminar(termino, tipo, archivo):
    resultados = []
    try:
        _eliminar_elementos(archivo, tipo, termino, resultados)
        print(f"El {tipo} {termino} fue eliminado exitosamente")
    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    return resultados

def eliminar_ingrediente(termino):
    from .ingredientes import ARCHIVO_INGREDIENTES as archivo_ingredientes
    return eliminar(termino, "nombre", archivo_ingredientes)

def eliminar_chef(termino):
    from .chef import ARCHIVO_CHEF as archivo_chef
    return eliminar(termino, "nombre", archivo_chef)

def eliminar_categoria(termino):
    from .categoria import ARCHIVO_CATEGORIA as archivo_categoria
    return eliminar(termino, "categoria", archivo_categoria)

def eliminar_hamburguesa(termino):
    from .hamburguesa import ARCHIVO_HAMBURGUESA as archivo_hamburguesa
    return eliminar(termino, "nombre", archivo_hamburguesa)