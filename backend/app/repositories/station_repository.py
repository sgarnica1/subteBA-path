import networkx as nx
from app.data.data import ESTACIONES_POSICIONES, CONEXIONES
from app.repositories.graph import MetroGraph

graph = MetroGraph(ESTACIONES_POSICIONES.values(), CONEXIONES)


def get_stations() -> nx.Graph:
    return graph.nodes


def get_station_graph() -> nx.Graph:
    return graph
