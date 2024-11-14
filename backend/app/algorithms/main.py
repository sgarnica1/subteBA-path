# ui.py

import ipywidgets as widgets
import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import display
from graph import MetroGraph
from a_star import a_star
from heuristics import time_between_stations
from config import (
    ESTACIONES,
    CONEXIONES,
    LINEAS,
)

# Crear el grafo
graph = MetroGraph(ESTACIONES, CONEXIONES)
graph.add_line_to_stations(LINEAS["LINEA_A"], "Línea A")
graph.add_line_to_stations(LINEAS["LINEA_B"], "Línea B")
graph.add_line_to_stations(LINEAS["LINEA_C"], "Línea C")
graph.add_line_to_stations(LINEAS["LINEA_D"], "Línea D")
graph.add_line_to_stations(LINEAS["LINEA_E"], "Línea E")


# Dropdowns interactivos
inicio_dropdown = widgets.Dropdown(options=graph.stations, description="Inicio:")
fin_dropdown = widgets.Dropdown(options=graph.stations, description="Fin:")


# Función para manejar el evento de búsqueda
def find_path(start, finish, graph):
    camino, lineas = a_star(start, finish, graph)
    if camino:
        tiempo_total = sum(
            time_between_stations(camino[i], camino[i + 1])
            for i in range(len(camino) - 1)
        )
        tiempo_cambio_linea = 3 * sum(
            1 for i in range(len(lineas) - 1) if lineas[i] != lineas[i + 1]
        )
        tiempo_total += tiempo_cambio_linea

        print(f"Camino encontrado: {camino}")
        print(f"Líneas: {lineas}")
        print(f"Tiempo estimado de la ruta: {tiempo_total} minutos")
    else:
        print("No se encontró camino válido.")


def run():
    initial_station = ESTACIONES["ALBERTI"]
    final_station = ESTACIONES["PERU"]
    find_path(initial_station, final_station, graph)


if __name__ == "__main__":
    run()
