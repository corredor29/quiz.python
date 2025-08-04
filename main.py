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
        
        elif opcion == "4":  # editar los elementos
            while True:
                limpiar_pantalla()
                print(buscar_elemento)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    print(archivo_hamburguesa)
                    tipo=input("nombre, categoria, ingredientes, precio, chef: ").lower().strip()
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "2":
                    tipo= "autor"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "3":
                    tipo= "genero"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "4":
                    tipo= "valoracion"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "5":  # eliminar los elementos
            while True:
                limpiar_pantalla()
                print(menu_eliminar)
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    print("1. Para libro\n2. Para pelicula\n3. Para cancion")
                    opcionTipo = input("Seleccione si es pelicula, libro o musica: ").strip()
                    if opcionTipo == "1":
                        tipo = "nombre"
                        archivo = archivo_libros
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "2":
                        tipo = "nombre"
                        archivo = archivo_peliculas
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "3":
                        tipo = "nombre"
                        archivo = archivo_musica
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        print(termino)
                        eliminar(termino, tipo, archivo)
                    else:
                        print("Ingrese una opción valida")
                elif opcion == "2":
                    tipo = "id"
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    print("1. Para pelicula\n2. Para libro\n3. Para cancion")
                    opcionTipo = input("Seleccione si es pelicula, libro o musica: ").strip()
                    if opcionTipo == "1":
                        archivo = archivo_peliculas
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "2":
                        archivo = archivo_libros
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "3":
                        archivo = archivo_musica
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    else:
                        print("Ingrese una opción valida")
                elif opcion == "3":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "6":  #ver elementos por categoria
            while True:
                limpiar_pantalla()
                print(ver_elementos_categoria)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    ver_por_categoria_libros()
                    
                elif opcion == "2":
                    ver_categoria_por_peliculas()
                elif opcion == "3":
                    ver_categoria_por_musica()
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()
        elif opcion == "7":  # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            pausar_pantalla()

if __name__ == "__main__":
    main()