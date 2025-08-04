from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from controlles.ingredientes import ARCHIVO_INGREDIENTES as archivo_ingredientes
from controlles.hamburguesa import ARCHIVO_HAMBURGUESA as archivo_hamburguesa
from controlles.chef import ARCHIVO_CHEF as archivo_chef
from controlles.categoria import ARCHIVO_CATEGORIA as archivo_categoria
from controlles.hamburguesa import *
from controlles.chef import *
from controlles.categoria import *
from controlles.ingredientes import *
from utils.helpers import leer_json
from controlles.buscar import *
from controlles.editar import *
from controlles.eliminar import *
from utils.menus import *


def main():
    while True:
        limpiar_pantalla()
        print(menu_principal)
        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == "1":  # Menú registrar elementos
            while True:
                limpiar_pantalla()
                print(anadir_elemento)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    registrar_hamburguesa()
                elif opcion == "2":
                    registrar_chef()
                elif opcion == "3":
                    registrar_ingredientes()
                elif opcion == "4":
                    registrar_categoria()
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "2":  # buscar elementos
            while True:
                limpiar_pantalla()
                print(buscar_elemento)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    print(archivo_hamburguesa)
                    tipo = "nombre"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "2":
                    print(archivo_chef)
                    tipo = "nombre"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "3":
                    print(archivo_ingredientes)
                    tipo = "nombre"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "4":
                    print(archivo_categoria)
                    tipo = "categoria"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "3":  # editar elementos
            while True:
                limpiar_pantalla()
                print(editar_elemento)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    print(archivo_hamburguesa)
                    tipo = "nombre"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "2":
                    print(archivo_chef)
                    tipo = "nombre"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "3":
                    print(archivo_ingredientes)
                    tipo = "nombre"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "4":
                    print(archivo_categoria)
                    tipo = "categoria"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "5":
                    print("Regresando al menú principal...")
                    limpiar_pantalla()
                    pausar_pantalla()
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()
        
        elif opcion == "4":  # busca los elementos
            while True:
                limpiar_pantalla()
                print(buscar_elemento)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    print(archivo_hamburguesa)
                    tipo=input("nombre, categoria, ingredientes, precio, chef: ").lower().strip()
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    eliminar(termino, tipo)
                elif opcion == "2":
                    print(archivo_chef)
                    tipo=input("nombre, especialidad : ").lower().strip()
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    eliminar(termino, tipo)
                elif opcion == "3":
                    print(archivo_ingredientes)
                    tipo=input("nombre, categoria, precio, stok : ").lower().strip()
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    eliminar(termino, tipo)
                elif opcion == "4":
                    print(archivo_categoria)
                    tipo=input("categoria, descripccion, : ").lower().strip()
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    eliminar(termino, tipo)
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "5":  # lista de  los elementos
            while True:
                limpiar_pantalla()
                print(listar_elemento)
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    mostrar_hamburguesa                
                elif opcion == "2":
                    mostrar_chef()
                    
                elif opcion == "3":
                    mostrar_ingredientes()
                elif opcion == "4":
                    mostrar_categoria()
                elif opcion == "5":
                    print("Regresando al menú principal...")
                    limpiar_pantalla()
                    break
                pausar_pantalla()
        elif opcion == "6":  # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            pausar_pantalla()

if __name__ == "__main__":
    main()