import networkx as nx
from app.repositories.graph import MetroGraph
from app.data.data import STATIONS_POSITION, CONNECTIONS, LINE_NAMES

graph = MetroGraph(STATIONS_POSITION.values(), CONNECTIONS)


def get_stations() -> dict:
    """
    Retrieve a list of all station nodes in the metro graph.

    Returns:
        list: A list of station nodes.
    """
    return graph.nodes

def get_lines() -> list:
    return LINE_NAMES


def get_station_graph() -> nx.Graph:
    """
    Retrieve the entire metro graph.

    Returns:
        nx.Graph: The metro graph object.
    """
    return graph
