import os
from utilidades import cargar_paises, guardar_paises
from funciones import (
    buscar_pais,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_paises,
    mostrar_estadisticas,
    mostrar_paises,
    agregar_pais,
    actualizar_pais
)

def menu():
    # Define la ruta absoluta del archivo CSV
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "countries.csv")
    
    # Carga inicial de los paises desde el CSV
    paises = cargar_paises(ruta)

    # Valida que la carga haya sido correcta
    if not paises:
        print("Error al cargar el CSV.")
        return

    # Bucle principal del menu
    while True:
        print("\n===== Gestor de Paises =====")
        print("1. Buscar pais")
        print("2. Filtrar paises")
        print("3. Ordenar paises")
        print("4. Mostrar estadisticas")
        print("5. Mostrar todos")
        print("6. Agregar pais")
        print("7. Actualizar pais")
        print("0. Salir")

        # Lectura de opcion principal
        op = input("Opcion: ").strip()

        if op == "1":
            # Busca paises por texto
            texto = input("Buscar: ").strip()
            mostrar_paises(buscar_pais(paises, texto))

        elif op == "2":
            # Menu de filtrado
            print("1. Por continente")
            print("2. Por poblacion")
            print("3. Por superficie")
            sub = input("Opcion: ").strip()

            if sub == "1":
                # Filtra por continente
                cont = input("Continente: ")
                mostrar_paises(filtrar_por_continente(paises, cont))

            elif sub == "2":
                # Filtra por rango de poblacion
                try:
                    mn = int(input("Min: "))
                    mx = int(input("Max: "))
                    mostrar_paises(filtrar_por_poblacion(paises, mn, mx))
                except ValueError:
                    print("Valores invalidos.")

            elif sub == "3":
                # Filtra por rango de superficie
                try:
                    mn = int(input("Min: "))
                    mx = int(input("Max: "))
                    mostrar_paises(filtrar_por_superficie(paises, mn, mx))
                except ValueError:
                    print("Valores invalidos.")

        elif op == "3":
            # Menu de ordenamiento
            print("1. Nombre")
            print("2. Poblacion")
            print("3. Superficie")
            sub = input("Orden: ")

            # Define si el orden es descendente
            desc = input("Descendente (s/n): ").lower() == "s"

            # Mapea la opcion a un campo valido del diccionario
            campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}

            # Ordena y muestra si la opcion es valida
            if sub in campos:
                mostrar_paises(ordenar_paises(paises, campos[sub], desc))

        elif op == "4":
            # Calcula y muestra estadisticas generales
            mostrar_estadisticas(paises)

        elif op == "5":
            # Muestra todos los paises cargados
            mostrar_paises(paises)

        elif op == "6":
            # Agrega un pais y guarda los cambios
            agregar_pais(paises)
            guardar_paises(ruta, paises)

        elif op == "7":
            # Actualiza un pais existente y guarda los cambios
            actualizar_pais(paises)
            guardar_paises(ruta, paises)

        elif op == "0":
            # Finaliza el programa
            print("Fin del programa.")
            break

        else:
            # Maneja opciones incorrectas
            print("Opcion invalida.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()

# ==============================================================
# Fuentes Bibliográficas
# ==============================================================
# 1. Documentación oficial de Python: https://docs.python.org/3/library/csv.html
# 2. W3Schools Python Tutorial: https://www.w3schools.com/python/
# 3. Real Python - Sorting Data in Python: https://realpython.com/sort-python/
# 4. Programiz Python Functions: https://www.programiz.com/python-programming/function
# ==============================================================
