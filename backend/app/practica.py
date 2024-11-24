# import mplleaflet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import warnings
from math import sqrt
from IPython.display import display
import ipywidgets as widgets
import heapq

# creamos grafo
v = 400  # hemos pasado la v.media de 24 km/h a m/minutos

G = nx.Graph()
estaciones = [
    "Alberti",
    "Pasco",
    "Congreso",
    "Saenz Peña",
    "Lima",
    "Piedras",
    "Perú",
    "Plaza de Mayo",
    "Pasteur",
    "Callao_B",
    "Uruguay",
    "Carlos Pellegrini",
    "Florida",
    "Leandro N. Alem",
    "Retiro",
    "General San Martín",
    "Lavalle",
    "Diagonal Norte",
    "Avenida de Mayo",
    "Moreno",
    "Independencia_C",
    "San Juan",
    "Constitución",
    "Facultad de Medicina",
    "Callao_D",
    "Tribunales",
    "9 de Julio",
    "Catedral",
    "Pichincha",
    "Entre Rios",
    "San Jose",
    "Independencia_E",
    "Belgrano",
    "Bolivar",
]

G.add_nodes_from(estaciones)
conexiones = [
    ("Alberti", "Pasco"),
    ("Pasco", "Congreso"),
    ("Congreso", "Saenz Peña"),
    ("Saenz Peña", "Lima"),
    ("Lima", "Piedras"),
    ("Piedras", "Perú"),
    ("Perú", "Plaza de Mayo"),  # Línea A
    ("Pasteur", "Callao_B"),
    ("Callao_B", "Uruguay"),
    ("Uruguay", "Carlos Pellegrini"),
    ("Carlos Pellegrini", "Florida"),
    ("Florida", "Leandro N. Alem"),  # Línea B
    ("Retiro", "General San Martín"),
    ("General San Martín", "Lavalle"),
    ("Lavalle", "Diagonal Norte"),
    ("Diagonal Norte", "Avenida de Mayo"),
    ("Avenida de Mayo", "Moreno"),
    ("Moreno", "Independencia_C"),
    ("Independencia_C", "San Juan"),
    ("San Juan", "Constitución"),  # Línea C
    ("Facultad de Medicina", "Callao_D"),
    ("Callao_D", "Tribunales"),
    ("Tribunales", "9 de Julio"),
    ("9 de Julio", "Catedral"),  # Línea D
    ("Pichincha", "Entre Rios"),
    ("Entre Rios", "San Jose"),
    ("San Jose", "Independencia_E"),
    ("Independencia_E", "Belgrano"),
    ("Belgrano", "Bolivar"),  # Línea E
    ("Bolivar", "Perú"),
    ("Bolivar", "Catedral"),
    ("Catedral", "Perú"),
    ("Independencia_C", "Independencia_E"),
    ("Lima", "Avenida de Mayo"),
    ("Diagonal Norte", "9 de Julio"),
    ("Diagonal Norte", "Carlos Pellegrini"),
    ("9 de Julio", "Carlos Pellegrini"),  # Transbordos
]

G.add_edges_from(conexiones)

linea_A = [
    "Alberti",
    "Pasco",
    "Congreso",
    "Saenz Peña",
    "Lima",
    "Piedras",
    "Perú",
    "Plaza de Mayo",
]
linea_B = [
    "Pasteur",
    "Callao_B",
    "Uruguay",
    "Carlos Pellegrini",
    "Florida",
    "Leandro N. Alem",
]
linea_C = [
    "Retiro",
    "General San Martín",
    "Lavalle",
    "Diagonal Norte",
    "Avenida de Mayo",
    "Moreno",
    "Independencia_C",
    "San Juan",
    "Constitución",
]
linea_D = ["Facultad de Medicina", "Callao_D", "Tribunales", "9 de Julio", "Catedral"]
linea_E = [
    "Pichincha",
    "Entre Rios",
    "San Jose",
    "Independencia_E",
    "Belgrano",
    "Bolivar",
]

for estacion in linea_A:
    G.nodes[estacion]["linea"] = "Línea A"

for estacion in linea_B:
    G.nodes[estacion]["linea"] = "Línea B"

for estacion in linea_C:
    G.nodes[estacion]["linea"] = "Línea C"

for estacion in linea_D:
    G.nodes[estacion]["linea"] = "Línea D"

for estacion in linea_E:
    G.nodes[estacion]["linea"] = "Línea E"

posiciones_estaciones = {
    "Alberti": (0, 9),
    "Pasco": (1, 9),
    "Congreso": (2, 9),
    "Saenz Peña": (3, 9),
    "Lima": (4, 9),
    "Piedras": (5, 9),
    "Perú": (6, 9),
    "Plaza de Mayo": (7, 9),
    "Pasteur": (0.5, 11.5),
    "Callao_B": (2, 11.5),
    "Uruguay": (3, 11.5),
    "Carlos Pellegrini": (5, 11.5),
    "Florida": (6, 11.5),
    "Leandro N. Alem": (7, 11.5),
    "Retiro": (7, 15),
    "General San Martín": (6.5, 14),
    "Lavalle": (5.5, 12),
    "Diagonal Norte": (5, 10.5),
    "Avenida de Mayo": (4.5, 9),
    "Moreno": (4.5, 7.5),
    "Independencia_C": (4.5, 5),
    "San Juan": (4.5, 3),
    "Constitución": (4.5, 0),
    "Facultad de Medicina": (0, 13),
    "Callao_D": (2, 13),
    "Tribunales": (3, 12),
    "9 de Julio": (5, 11),
    "Catedral": (6, 10),
    "Pichincha": (0.5, 3),
    "Entre Rios": (2, 3),
    "San Jose": (3, 3),
    "Independencia_E": (3.5, 5),
    "Belgrano": (5, 7),
    "Bolivar": (6, 8),
}


colores = {
    "Línea A": "#ADD8E6",  # Azul claro
    "Línea B": "red",  # Rojo
    "Línea C": "#00008B",  # Azul oscuro
    "Línea D": "#006400",  # Verde oscuro
    "Línea E": "purple",  # Púrpura
}

# Usar el método .get() para acceder de forma segura a los atributos del diccionario
colores_estaciones = [
    colores.get(G.nodes[estacion].get("linea"), "default_color") for estacion in G.nodes
]
colores_lineas = {
    estacion: colores.get(G.nodes[estacion].get("linea"), "default_color")
    for estacion in G.nodes
}


def calcDis(pos1, pos2):
    x1, y1 = posiciones_estaciones[pos1]
    x2, y2 = posiciones_estaciones[pos2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 800


def calcTiempo(pos1, pos2):
    return calcDis(pos1, pos2) / v


def a_estrella(inicio, fin, grafo, posiciones, calcTiempo, colores_lineas):
    heap_abierto = []
    heapq.heappush(heap_abierto, (0, inicio, [], []))
    visitados = set()

    while heap_abierto:
        tiempo, nodo_actual, camino, lineas = heapq.heappop(heap_abierto)
        if nodo_actual == fin:
            return camino + [nodo_actual], lineas

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            vecinos = grafo[nodo_actual]
            for vecino in vecinos:
                if vecino not in visitados:
                    tiempo_recorrido = calcTiempo(nodo_actual, vecino)  # g
                    nuevo_tiempo = tiempo + tiempo_recorrido  # g + g nuevo
                    heuristica = calcTiempo(vecino, fin)  # h
                    linea_actual = G.nodes[nodo_actual].get(
                        "linea", "Desconocida"
                    )  # Cambio aquí
                    if len(lineas) == 0 or lineas[-1] != linea_actual:
                        lineas_nuevas = lineas + [linea_actual]
                    else:
                        lineas_nuevas = lineas.copy()
                    nuevo_nodo = (
                        nuevo_tiempo + heuristica,
                        vecino,
                        camino + [nodo_actual],
                        lineas_nuevas,
                    )
                    heapq.heappush(heap_abierto, nuevo_nodo)

    return None, None


# Crear dropdowns interactivos para seleccionar estaciones
inicio_dropdown = widgets.Dropdown(
    options=estaciones, description="Estación de inicio:"
)
fin_dropdown = widgets.Dropdown(options=estaciones, description="Estación de fin:")


# Función para manejar el evento del botón
def encontrar_camino(event):
    inicio = inicio_dropdown.value
    fin = fin_dropdown.value
    camino, lineas = a_estrella(
        inicio, fin, G, posiciones_estaciones, calcTiempo, colores_lineas
    )
    if camino:
        tiempo_total = sum(
            calcTiempo(camino[i], camino[i + 1]) for i in range(len(camino) - 1)
        )
        tiempo_cambio_linea = 3 * sum(
            1 for i in range(len(lineas) - 1) if lineas[i] != lineas[i + 1]
        )
        tiempo_total += tiempo_cambio_linea

        print(f"Camino encontrado: {camino}")
        print(f"Líneas: {lineas}")
        print(f"Tiempo estimado de la ruta: {tiempo_total} minutos")
        # Aquí sigue tu código de visualización

        # Crear un subgrafo con el camino encontrado
        path_edges = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
        subgrafo = G.edge_subgraph(path_edges)
        # Dibujar el grafo con el camino resaltado
        nx.draw(
            G,
            posiciones_estaciones,
            node_color=colores_estaciones,
            with_labels=True,
            node_size=100,
            font_size=6,
        )
        nx.draw(
            subgrafo, posiciones_estaciones, edge_color="red", node_size=100, width=3
        )
        # Mostrar el grafo
        plt.axis("off")
        plt.title("Camino más corto desde {} hasta {}".format(inicio, fin))
        plt.show()
    else:
        print("No se encontró un camino válido.")


# Crear un botón para iniciar la búsqueda
boton_buscar = widgets.Button(description="Buscar camino")
boton_buscar.on_click(encontrar_camino)

# Mostrar widgets interactivos
widgets.VBox([inicio_dropdown, fin_dropdown, boton_buscar])
