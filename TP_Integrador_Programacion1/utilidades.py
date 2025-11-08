import csv

def limpiar_texto(texto):
    # Normaliza el texto a minusculas y sin tildes para comparaciones consistentes
    texto = texto.lower()
    texto = texto.replace('á', 'a')
    texto = texto.replace('é', 'e')
    texto = texto.replace('í', 'i')
    texto = texto.replace('ó', 'o')
    texto = texto.replace('ú', 'u')
    return texto

def cargar_paises(ruta):
    # Lee el archivo CSV y carga los paises en una lista de diccionarios
    paises = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Salta el encabezado del CSV

            for fila in lector:
                # Cada fila debe tener exactamente 4 columnas
                if len(fila) != 4:
                    continue

                nombre = fila[0].strip()

                # Convierte poblacion y superficie a enteros
                try:
                    poblacion = int(fila[1])
                    superficie = int(fila[2])
                except ValueError:
                    # Salta filas con valores numericos invalidos
                    continue

                # Normaliza el continente
                continente = limpiar_texto(fila[3].strip())

                # Agrega el pais a la lista
                paises.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente
                })
    except FileNotFoundError:
        # Manejo simple de error si el archivo no existe
        print("Error: archivo CSV no encontrado.")
    return paises

def guardar_paises(ruta, paises):
    # Guarda la lista de paises en el archivo CSV sobrescribiendo el archivo existente
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        # Escribe encabezado fijo
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        # Escribe cada pais del listado
        for p in paises:
            escritor.writerow([p["nombre"], p["poblacion"], p["superficie"], p["continente"]])
