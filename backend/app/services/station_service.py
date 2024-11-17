import math
import networkx as nx
from typing import List, Optional, Tuple
from app.algorithms.a_star import a_star
from app.algorithms.heuristics import time_between_stations, distance_between_stations
from app.repositories.station_repository import (
    get_stations,
    get_station_graph,
    get_lines,
)
from app.config.logger import configure_logger

logger = configure_logger()


def get_stations_with_positions() -> dict:
    """
    Retrieve stations with their respective positions as a graph.
    """
    return {"stations": get_stations(), "lines": get_lines()}


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

    path_details = [graph.nodes[station] for station in path]

    travel_time = 0
    for i in range(len(path) - 1):
        time = time_between_stations(path[i], path[i + 1])

        if path_details[i]["line"] != path_details[i + 1]["line"]:
            time = math.ceil(time * 10)  # Walking time

        path_details[i]["travel_time"] = math.ceil(time)
        travel_time += math.ceil(time)

    path_details[len(path_details) - 1][
        "travel_time"
    ] = 0  # Restart travel time for last station

    logger.info(f"Travel time {travel_time}")

    return [path_details, lines, travel_time]
