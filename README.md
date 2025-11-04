🌎 Gestor de Países — TP Integrador Programación 1

🧩 Descripción del programa

Este programa permite gestionar información de países utilizando un archivo CSV (countries.csv) como base de datos.

El sistema carga los datos desde el archivo y ofrece distintas funcionalidades, como listar países, filtrarlos por continente o buscar información específica.

El proyecto fue desarrollado como trabajo integrador para la materia Programación 1, utilizando Python y estructuras de datos básicas como listas y diccionarios.

🚀 Instrucciones de uso

_Asegurarse de que el archivo countries.csv se encuentre en la misma carpeta que el archivo gestor_paises.py.

_Ejecutar el programa principal desde la terminal o VS Code con:

python gestor_paises.py

_Una vez iniciado, el programa mostrará un menú de opciones, por ejemplo:

         GESTOR DE PAÍSES
1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Ver estadísticas
5. Mostrar todos
0. Salir
Elija una opción:

💡 Ejemplos de entradas y salidas
Ejemplo 1: Buscar país por nombre

Entrada:

1

España

Salida:

Nombre                             Población         Superficie        Continente

España                             47351567          505990            Europa

...

Ejemplo 2: Filtrar países por continente

Entrada:

2

1

oceania


Salida:


Nombre                             Población         Superficie        Continente

Australia                          25788214          7692024           Oceania

Nueva Zelanda                      5185288           268021            Oceania

Papúa Nueva Guinea                 10710000          462840            Oceania

Fiyi                               936000            18274             Oceania

Islas Salomón                      740000            28896             Oceania

Vanuatu                            341000            12189             Oceania

Samoa                              225000            2842              Oceania

Tonga                              106000            747               Oceania

Kiribati                           131000            811               Oceania

Micronesia                         115000            702               Oceania

Islas Marshall                     42700             181               Oceania

Palaos                             18000             459               Oceania

Nauru                              12500             21                Oceania

Tuvalu                             11300             26                Oceania

...

Ejemplo 3: Ordenar países por superficie descendente

Entrada:

3

3

s


Salida:


Nombre                             Población         Superficie        Continente

Rusia                              144444359         17098246          Europa

Canadá                             38008005          9984670           America

Estados Unidos                     333287557         9833517           America

China                              1419321278        9596961           Asia

Brasil                             213993437         8515767           America

Australia                          25788214          7692024           Oceania

India                              1428627663        3287263           Asia

Argentina                          45376763          2780400           America

Kazajistán                         19750000          2724900           Asia

Argelia                            46496556          2381741           Africa

República Democrática del Congo    102262808         2344858           Africa

Arabia Saudita                     36947025          2149690           Asia

México                             130262216         1964375           America

Indonesia                          277534122         1904569           Asia

Sudán                              48190000          1861484           Africa

Irán                               89172767          1648195           Asia

Mongolia                           3470000           1564110           Asia

Perú                               33715471          1285216           America

Chad                               18200000          1284000           Africa
(etc...)
...

👥 Participaron los integrantes:

Nicolás Bohm
Gabriel Denis


📂 Estructura del proyecto
TP_Integrador_Programacion1/

│

├── gestor_paises.py        # Código principal del programa

├── countries.csv           # Archivo de datos con todos los países

└── README.md               # Documentación del proyecto


🧠 Tecnologías utilizadas

Lenguaje: Python 3

Archivos de datos: CSV

Entorno: Visual Studio Code / GitHub Desktop

🏁 Conclusión

El proyecto “Gestor de Países” permite poner en práctica conceptos fundamentales de programación estructurada, manejo de archivos y uso de estructuras de datos.

Además, refuerza la importancia del trabajo en equipo y la documentación en proyectos de software.
