# Gestión de Datos de Países en Python

**Autores**
- Gabriel Denis
- Nicolás Bohm

## Descripción
Aplicación de consola en Python para gestionar un conjunto de datos de países. Permite buscar países, filtrar por continente, rango de población y superficie, ordenar por distintos campos y mostrar estadísticas básicas. El objetivo del trabajo es practicar estructuras de datos (listas y diccionarios), funciones, modularización, manejo de archivos CSV y validaciones de entradas.

## Requisitos
- Python 3.8+
- Módulos estándar: `csv`, `os`

## Estructura del proyecto
```
tpi-paises/
├── .gitignore           # Ignora archivos de caché .pyc
├── countries.csv        # Dataset base (nombre,poblacion,superficie,continente)
├── main.py              # Punto de entrada (menu)
├── utilidades.py        # Funciones para carga/guardado y normalización
├── funciones.py         # Lógica: filtros, busquedas, ordenamientos, estadisticas y CRUD
├── README.md            # Este archivo
```

## Diseño y decisiones técnicas (resumen)
- **Una función = una responsabilidad.** Cada módulo contiene funciones con responsabilidad única para facilitar pruebas y lectura.
- **Modelo en memoria.** Los países se cargan en memoria como una lista de diccionarios:
  ```py
  {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "america"
  }
  ```
- **Normalización.** Se normaliza texto a minúsculas y se eliminan tildes para comparaciones consistentes.
- **CSV robusto.** Verificación de filas con columnas esperadas y manejo de errores al convertir números.
- **Validaciones de entrada.** Comprobación de entradas numéricas y mensajes claros ante errores.

## Diagrama de flujo (resumen)
1. `main.py` carga `countries.csv` con `cargar_paises`.
2. Muestra menú con opciones: buscar, filtrar, ordenar, estadísticas, mostrar todo, agregar, actualizar.
3. Acciones que modifican datos llaman a `guardar_paises` para persistir cambios.
4. Funciones puras (`filtrar_por_continente`, `ordenar_paises`, ...) retornan listas que `main.py` muestra con `mostrar_paises`.

## Cómo ejecutar
1. Desde la consola en la carpeta del proyecto:
```bash
python main.py
```
2. Usar el menú interactivo:
- Buscar por texto (coincidencia parcial).
- Filtrar por continente o por rangos numéricos.
- Ordenar por nombre, población o superficie (asc/desc).
- Agregar o actualizar países. Después de agregar/actualizar el CSV se sobrescribe con los cambios.

## Formato del CSV
El archivo debe tener la primera fila con encabezado:
```
nombre,poblacion,superficie,continente
```
Ejemplo:
```
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```
Notas:
- `poblacion` y `superficie` deben ser enteros.
- `continente` se normaliza a minúsculas sin tildes para filtros.

## Ejemplos de uso (entrada/salida)
- Buscar "ar" devuelve "Argentina" y "Brasil" si aplicable.
- Filtrar por continente "america" devuelve solo países cuyo campo continente coincida.
- Filtrar por población: Min 1000000 Max 10000000 devuelve países en ese rango.

## Validaciones implementadas
- Manejo de archivo inexistente con mensaje claro.
- Ignora filas CSV con columnas o valores numéricos incorrectos.
- Valida conversiones a `int` al agregar/actualizar.
- Evita agregar países con nombre duplicado (comparación normalizada).

## Fuentes bibliográficas
- Documentación oficial de Python: https://docs.python.org/3/library/csv.html
- Real Python - Sort Data in Python: https://realpython.com/sort-python/
- Programiz - Python Functions: https://www.programiz.com/python-programming/function

## Licencia
Proyecto entregado como trabajo práctico. Libre para uso académico.

