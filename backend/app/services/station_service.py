import networkx as nx
from typing import List, Optional, Tuple
from app.algorithms.a_star import a_star
from app.algorithms.heuristics import time_between_stations
from app.repositories.station_repository import get_stations, get_station_graph, get_lines


def get_stations_with_positions() -> dict:
    """
    Retrieve stations with their respective positions as a graph.
    """
    return {
        "stations": get_stations(),
        "lines": get_lines()
    }


def find_path(start: str, finish: str) -> Optional[Tuple[List[str], List[str], int]]:
    """
    Find the shortest path between two stations.

    Args:
        start (str): The starting station ID.
        finish (str): The destination station ID.

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

    travel_time = sum(
        time_between_stations(path[i], path[i + 1]) for i in range(len(path) - 1)
    )
    change_line_time = 3 * sum(
        1 for i in range(len(lines) - 1) if lines[i] != lines[i + 1]
    )
    total_time = travel_time + change_line_time

    return [path, lines, total_time]
