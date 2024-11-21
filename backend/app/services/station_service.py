import math
import networkx as nx
from typing import List, Optional, Tuple
from app.algorithms.a_star import a_star
from app.algorithms.travel_time import calculate_travel_time
from app.repositories.station_repository import (
    get_stations,
    get_station_graph,
    get_lines,
)


def get_stations_with_positions() -> dict:
    """
    Retrieve stations with their respective positions as a graph.
    """
    return {"stations": get_stations(), "lines": get_lines()}


def find_path(
    start: str, finish: str, day: str, hour: str
) -> Optional[Tuple[List[str], List[str], int]]:
    """
    Find the shortest path between two stations.

    Args:
        start (str): The starting station ID.
        finish (str): The destination station ID.
        day (str): The selected day.
        hour (int): The selected hour.

    Returns:
        Optional[Tuple[List[str], List[str], int]]:
            - List of station names in the path.
            - List of lines used in the path.
            - Total time for the journey.
        Returns None if no path is found.
    """

    graph: nx.Graph = get_station_graph()

    path, lines = a_star(start, finish, graph)

    if not path:
        return None

    path_details = [graph.nodes[station] for station in path]

    travel_time = calculate_travel_time(day, hour, path, path_details)

    return [path_details, lines, travel_time]
