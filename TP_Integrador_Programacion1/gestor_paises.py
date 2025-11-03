"""
Proyecto Final Integrador - Programación 1
Gestión de Datos de Países en Python

Autores:
- Nicolás Bohm y Gabriel Denis

Descripción:
Este programa permite gestionar un conjunto de países cargados desde un archivo CSV.
Incluye búsqueda, filtrado, ordenamiento y cálculo de estadísticas.
El trabajo aplica los conceptos de listas, diccionarios, funciones, estructuras de control,
archivos CSV y manejo básico de errores.
"""

import csv
import os

# ==============================================================
# Funciones de Utilidad
# ==============================================================

def limpiar_texto(texto):
    """Convierte el texto a minúsculas y elimina manualmente las tildes."""
    # Convertir a minúsculas
    texto = texto.lower()
    # Reemplazo de tildes
    texto = texto.replace('á', 'a')
    texto = texto.replace('é', 'e')
    texto = texto.replace('í', 'i')
    texto = texto.replace('ó', 'o')
    texto = texto.replace('ú', 'u')
    return texto

# ==============================================================
# Funciones de Carga de Datos
# ==============================================================

def cargar_paises(nombre_archivo):
    """
    Carga los países desde un archivo CSV.
    Usa el módulo 'csv' de la biblioteca estándar de Python.
    Retorna una lista de diccionarios, donde cada diccionario representa un país.
    """
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Salta el encabezado
            for fila in lector:
                # Validación básica de estructura
                if len(fila) == 4:
                    nombre = fila[0].strip()
                    try:
                        poblacion = int(fila[1])
                        superficie = int(fila[2])
                    except ValueError:
                        continue
                        
                    # Aplicar normalización al nombre del continente al cargar
                    continente = limpiar_texto(fila[3].strip())
                    
                    paises.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    })
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'countries.csv'.")
    return paises


# ==============================================================
# Funciones de Búsqueda
# ==============================================================

def buscar_pais(paises, texto):
    """
    Devuelve una lista de países cuyo nombre contenga el texto ingresado.
    La búsqueda no distingue mayúsculas, minúsculas ni tildes.
    """
    texto_limpio = limpiar_texto(texto) # Limpia la entrada del usuario
    return [
        p for p in paises 
        if texto_limpio in limpiar_texto(p["nombre"]) # Limpia el nombre del país
    ]


# ==============================================================
# Funciones de Filtro
# ==============================================================

def filtrar_por_continente(paises, continente):
    """Filtra los países por continente. Ignora mayúsculas y acentos."""
    continente_limpio = limpiar_texto(continente)
    return [
        p for p in paises 
        if p["continente"] == continente_limpio # Compara con el dato ya normalizado
    ]


def filtrar_por_poblacion(paises, minimo, maximo):
    """Filtra países dentro de un rango de población."""
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]


def filtrar_por_superficie(paises, minimo, maximo):
    """Filtra países dentro de un rango de superficie."""
    return [p for p in paises if minimo <= p["superficie"] <= maximo]


# ==============================================================
# Funciones de Ordenamiento
# ==============================================================

def ordenar_paises(paises, campo, descendente=False):
    """
    Ordena la lista de países según el campo indicado.
    Usa la función 'sorted' con una función lambda como clave.
    """
    return sorted(paises, key=lambda p: p[campo], reverse=descendente)


# ==============================================================
# Funciones de Estadísticas
# ==============================================================

def mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales de los países cargados.
    Calcula máximos, mínimos y promedios usando funciones integradas.
    """
    if not paises:
        print("No hay datos cargados.")
        return

    max_pop = max(paises, key=lambda p: p["poblacion"])
    min_pop = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print(f"País con mayor población: {max_pop['nombre']} - {max_pop['poblacion']}")
    print(f"País con menor población: {min_pop['nombre']} - {min_pop['poblacion']}")
    print(f"Promedio de población: {int(prom_pob)}")
    print(f"Promedio de superficie: {int(prom_sup)}")

    print("\nCantidad de países por continente:")
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1
        
    for cont, cant in continentes.items():
        # Usa .capitalize() para mostrar el continente correctamente
        print(f"{cont.capitalize()}: {cant}")


# ==============================================================
# Funciones de Presentación
# ==============================================================

def mostrar_paises(paises):
    """
    Muestra los países en formato tabular con ancho de columna fijo.
    """
    if not paises:
        print("No hay países para mostrar.")
        return
        
    # Definir anchos fijos para la alineación
    ANCHO_NOMBRE = 35
    ANCHO_CIFRA = 18
    ANCHO_CONTINENTE = 15

    # 1. Imprimir encabezado con anchos fijos y alineación
    print("\n" + "=" * 90)
    print(
        f"{'Nombre':<{ANCHO_NOMBRE}}{'Población':<{ANCHO_CIFRA}}"
        f"{'Superficie':<{ANCHO_CIFRA}}{'Continente':<{ANCHO_CONTINENTE}}"
    )
    print("-" * 90)

    # 2. Imprimir datos
    for p in paises:
        # Usamos .capitalize() para que el continente se vea bien
        continente_mostrar = p['continente'].capitalize() 
        
        print(
            f"{p['nombre']:<{ANCHO_NOMBRE}}"
            f"{p['poblacion']:<{ANCHO_CIFRA}}"
            f"{p['superficie']:<{ANCHO_CIFRA}}"
            f"{continente_mostrar:<{ANCHO_CONTINENTE}}" # Usamos la versión con mayúscula
        )
    print("=" * 90)


# ==============================================================
# Submenús
# ==============================================================

def menu_buscar(paises):
    texto = input("Ingrese nombre o parte del nombre: ").strip()
    if not texto:
        print("Debe ingresar un texto para buscar.")
        return
    encontrados = buscar_pais(paises, texto)
    if encontrados:
        mostrar_paises(encontrados)
    else:
        print("No se encontraron países con ese nombre.")


def menu_filtros(paises):
    print("\n1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    sub = input("Elija una opción: ").strip()

    if sub == "1":
        cont = input("Ingrese continente: ").strip()
        resultado = filtrar_por_continente(paises, cont)
        mostrar_paises(resultado) if resultado else print("No se encontraron países en ese continente.")

    elif sub == "2":
        try:
            minp = int(input("Población mínima: "))
            maxp = int(input("Población máxima: "))
            if minp > maxp:
                print("El mínimo no puede ser mayor que el máximo.")
                return
            resultado = filtrar_por_poblacion(paises, minp, maxp)
            mostrar_paises(resultado) if resultado else print("No hay países en ese rango.")
        except ValueError:
            print("Debe ingresar números válidos.")

    elif sub == "3":
        try:
            mins = int(input("Superficie mínima: "))
            maxs = int(input("Superficie máxima: "))
            if mins > maxs:
                print("El mínimo no puede ser mayor que el máximo.")
                return
            resultado = filtrar_por_superficie(paises, mins, maxs)
            mostrar_paises(resultado) if resultado else print("No hay países en ese rango.")
        except ValueError:
            print("Debe ingresar números válidos.")
    else:
        print("Opción inválida.")


def menu_ordenamientos(paises):
    print("\n1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    sub = input("Elija una opción: ").strip()
    desc = input("¿Descendente? (s/n): ").lower().strip() == "s"

    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    if sub in campos:
        ordenados = ordenar_paises(paises, campos[sub], desc)
        mostrar_paises(ordenados)
    else:
        print("Opción inválida.")


# ==============================================================
# Menú Principal
# ==============================================================

def menu():
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_script, "countries.csv")
    paises = cargar_paises(ruta_csv)
    if not paises:
        print("No se pudieron cargar los datos. Revisá el archivo CSV.")
        return

    while True:
        print("\n" + "=" * 40)
        print("         GESTOR DE PAÍSES")
        print("=" * 40)
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Ver estadísticas")
        print("5. Mostrar todos")
        print("0. Salir")
        print("=" * 40)

        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            menu_buscar(paises)
        elif opcion == "2":
            menu_filtros(paises)
        elif opcion == "3":
            menu_ordenamientos(paises)
        elif opcion == "4":
            mostrar_estadisticas(paises)
        elif opcion == "5":
            mostrar_paises(paises)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ==============================================================
# Ejecución Principal
# ==============================================================

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