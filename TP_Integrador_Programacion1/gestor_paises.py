import csv

# ---------------------------------------
# Cargar países desde un archivo CSV
# ---------------------------------------
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltear el encabezado
            for fila in lector:
                if len(fila) == 4:
                    nombre = fila[0]
                    poblacion = int(fila[1])
                    superficie = int(fila[2])
                    continente = fila[3]
                    paises.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    })
    except FileNotFoundError:
        print("No se encontró el archivo. Asegúrate de tener 'countries.csv' en la carpeta.")
    return paises


# ---------------------------------------
# Buscar país por nombre
# ---------------------------------------
def buscar_pais(paises, texto):
    resultado = []
    for pais in paises:
        if texto.lower() in pais["nombre"].lower():
            resultado.append(pais)
    return resultado


# ---------------------------------------
# Filtrar países
# ---------------------------------------
def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def filtrar_por_poblacion(paises, minimo, maximo):
    resultado = []
    for p in paises:
        if (p["poblacion"] >= minimo) and (p["poblacion"] <= maximo):
            resultado.append(p)
    return resultado


def filtrar_por_superficie(paises, minimo, maximo):
    resultado = []
    for p in paises:
        if (p["superficie"] >= minimo) and (p["superficie"] <= maximo):
            resultado.append(p)
    return resultado


# ---------------------------------------
# Ordenamientos
# ---------------------------------------
def ordenar_paises(paises, campo, descendente=False):
    return sorted(paises, key=lambda p: p[campo], reverse=descendente)


# ---------------------------------------
# Estadísticas
# ---------------------------------------
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return

    max_pop = max(paises, key=lambda p: p["poblacion"])
    min_pop = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print("País con mayor población:", max_pop["nombre"], "-", max_pop["poblacion"])
    print("País con menor población:", min_pop["nombre"], "-", min_pop["poblacion"])
    print("Promedio de población:", int(prom_pob))
    print("Promedio de superficie:", int(prom_sup))

    print("\nCantidad de países por continente:")
    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont not in continentes:
            continentes[cont] = 0
        continentes[cont] += 1
    for cont, cant in continentes.items():
        print(cont, ":", cant)


# ---------------------------------------
# Mostrar tabla simple
# ---------------------------------------
def mostrar_paises(paises):
    if not paises:
        print("No hay países para mostrar.")
        return
    print("\nNombre\t\tPoblación\tSuperficie\tContinente")
    print("-" * 60)
    for p in paises:
        print(f"{p['nombre']:<15}{p['poblacion']:<15}{p['superficie']:<15}{p['continente']}")
    print()


# ---------------------------------------
# Menú principal
# ---------------------------------------
def menu():
    paises = cargar_paises("countries.csv")
    if not paises:
        return

    while True:
        print("===== GESTOR DE PAÍSES =====")
        print("1. Buscar país por nombre")
        print("2. Filtrar países")
        print("3. Ordenar países")
        print("4. Ver estadísticas")
        print("5. Mostrar todos")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            texto = input("Ingrese nombre o parte del nombre: ")
            encontrados = buscar_pais(paises, texto)
            mostrar_paises(encontrados)

        elif opcion == "2":
            print("\n1. Por continente")
            print("2. Por rango de población")
            print("3. Por rango de superficie")
            sub = input("Elija una opción: ")

            if sub == "1":
                cont = input("Ingrese continente: ")
                mostrar_paises(filtrar_por_continente(paises, cont))
            elif sub == "2":
                minp = int(input("Población mínima: "))
                maxp = int(input("Población máxima: "))
                mostrar_paises(filtrar_por_poblacion(paises, minp, maxp))
            elif sub == "3":
                mins = int(input("Superficie mínima: "))
                maxs = int(input("Superficie máxima: "))
                mostrar_paises(filtrar_por_superficie(paises, mins, maxs))
            else:
                print("Opción inválida.")

        elif opcion == "3":
            print("\n1. Por nombre")
            print("2. Por población")
            print("3. Por superficie")
            sub = input("Elija una opción: ")
            desc = input("¿Descendente? (s/n): ").lower() == "s"

            if sub == "1":
                mostrar_paises(ordenar_paises(paises, "nombre", desc))
            elif sub == "2":
                mostrar_paises(ordenar_paises(paises, "poblacion", desc))
            elif sub == "3":
                mostrar_paises(ordenar_paises(paises, "superficie", desc))
            else:
                print("Opción inválida.")

        elif opcion == "4":
            mostrar_estadisticas(paises)

        elif opcion == "5":
            mostrar_paises(paises)

        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente otra vez.")


# ---------------------------------------
# Inicio del programa
# ---------------------------------------
menu()
