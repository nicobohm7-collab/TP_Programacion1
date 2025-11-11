from utilidades import limpiar_texto

def buscar_pais(paises, texto):
    # Normaliza el texto buscado
    texto_limpio = limpiar_texto(texto)
    # Devuelve paises cuyo nombre contenga el texto buscado
    return [
        p for p in paises
        if texto_limpio in limpiar_texto(p["nombre"])
    ]

def filtrar_por_continente(paises, cont):
    # Normaliza el continente ingresado
    clave = limpiar_texto(cont)
    # Filtra por coincidencia exacta de continente
    return [p for p in paises if p["continente"] == clave]

def filtrar_por_poblacion(paises, minimo, maximo):
    # Filtra paises dentro del rango de poblacion
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]

def filtrar_por_superficie(paises, minimo, maximo):
    # Filtra paises dentro del rango de superficie
    return [p for p in paises if minimo <= p["superficie"] <= maximo]

def ordenar_paises(paises, campo, desc=False):
    # Ordena segun el campo indicado y en orden descendente si se solicita
    return sorted(paises, key=lambda p: p[campo], reverse=desc)

def agregar_pais(paises):
    # Lee el nombre del pais y valida no estar vacio
    nombre = input("Nombre del pais: ").strip()
    if not nombre:
        print("Nombre invalido.")
        return

    # Evita duplicados por nombre normalizado
    for p in paises:
        if limpiar_texto(p["nombre"]) == limpiar_texto(nombre):
            print("El pais ya existe.")
            return

    # Pide valores numericos obligatorios
    try:
        poblacion = int(input("Poblacion: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Valores invalidos.")
        return

    # Obtiene y normaliza continente
    continente = input("Continente: ").strip()
    continente = limpiar_texto(continente)

    # Crea el nuevo registro
    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Agrega a la lista en memoria
    paises.append(nuevo)
    print("Pais agregado.")

def actualizar_pais(paises):
    # Solo actualiza si el nombre coincide
    nombre = input("Ingrese el pais a actualizar: ").strip()
    nombre_limpio = limpiar_texto(nombre)

    for p in paises:
        if limpiar_texto(p["nombre"]) == nombre_limpio:
            # Muestra valores actuales y permite dejarlos sin cambiar
            print("Deje el campo vacio para no modificarlo.")
            nuevo_nombre = input(f"Nombre ({p['nombre']}): ").strip()
            nueva_pob = input(f"Poblacion ({p['poblacion']}): ").strip()
            nueva_sup = input(f"Superficie ({p['superficie']}): ").strip()
            nuevo_cont = input(f"Continente ({p['continente']}): ").strip()

            # Actualiza nombre si corresponde
            if nuevo_nombre:
                p["nombre"] = nuevo_nombre

            # Actualiza poblacion validando numero
            if nueva_pob:
                try:
                    p["poblacion"] = int(nueva_pob)
                except ValueError:
                    print("Poblacion invalida. Sin cambios.")

            # Actualiza superficie validando numero
            if nueva_sup:
                try:
                    p["superficie"] = int(nueva_sup)
                except ValueError:
                    print("Superficie invalida. Sin cambios.")

            # Actualiza continente normalizado
            if nuevo_cont:
                p["continente"] = limpiar_texto(nuevo_cont)

            print("Pais actualizado.")
            return

    # Si no encuentra coincidencia
    print("El pais no existe.")

def mostrar_estadisticas(paises):
    # No procesa si no hay datos
    if not paises:
        print("No hay datos.")
        return

    # Obtiene maximos y minimos por poblacion
    max_pop = max(paises, key=lambda p: p["poblacion"])
    min_pop = min(paises, key=lambda p: p["poblacion"])

    # Calcula promedios
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\n--- Estadisticas ---")
    print("Mayor poblacion:", max_pop["nombre"], max_pop["poblacion"])
    print("Menor poblacion:", min_pop["nombre"], min_pop["poblacion"])
    print("Promedio poblacion:", int(prom_pob))
    print("Promedio superficie:", int(prom_sup))

    # Cuenta paises por continente
    print("\nPaises por continente:")
    conts = {}
    for p in paises:
        conts[p["continente"]] = conts.get(p["continente"], 0) + 1

    # Muestra totales por continente
    for c, cant in conts.items():
        print(c.capitalize(), ":", cant)

def mostrar_paises(paises):
    # Maneja lista vacia
    if not paises:
        print("No hay paises.")
        return

    # Anchos fijos para formato de tabla
    AN_NOMBRE = 35
    AN_NUM = 18
    AN_CONT = 15

    # Encabezado de tabla
    print("=" * 90)
    print(
        f"{'Nombre':<{AN_NOMBRE}}{'Poblacion':<{AN_NUM}}"
        f"{'Superficie':<{AN_NUM}}{'Continente':<{AN_CONT}}"
    )
    print("-" * 90)

    # Imprime cada pais con formato alineado
    for p in paises:
        print(
            f"{p['nombre']:<{AN_NOMBRE}}"
            f"{p['poblacion']:<{AN_NUM}}"
            f"{p['superficie']:<{AN_NUM}}"
            f"{p['continente'].capitalize():<{AN_CONT}}"
        )

    print("=" * 90)


def eliminar_pais(paises):
    """Elimina un país de la lista por su nombre."""
    nombre_eliminar = input("Ingrese el pais a eliminar: ").strip()
    
    if not nombre_eliminar:
        print("Nombre inválido.")
        return

    nombre_limpio = limpiar_texto(nombre_eliminar)
    indice_a_eliminar = -1 
    
    for i, p in enumerate(paises):
        if limpiar_texto(p["nombre"]) == nombre_limpio:
            indice_a_eliminar = i
            break
    
    if indice_a_eliminar != -1:
        # Confirmación
        confirmacion = input(f"¿Seguro que desea eliminar {paises[indice_a_eliminar]['nombre']}? (s/n): ").lower()
        if confirmacion == 's':
            paises.pop(indice_a_eliminar)
            print("Pais eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("El pais no existe.")