from typing import List, Optional, Union
import networkx as nx
from app.repositories.station_repository import get_stations, get_station_graph
from app.algorithms.a_star import a_star
from app.algorithms.heuristics import time_between_stations
from app.data.data import (
    ESTACIONES,
)


def get_stations_with_positions() -> nx.Graph:
    return get_stations()


def find_path(
    start: str, finish: str
) -> Optional[List[Union[List[str], List[str], int]]]:

    graph: nx.Graph = get_station_graph()

    path, lines = a_star(start, finish, graph)
    if path:
        total_time = sum(
            time_between_stations(path[i], path[i + 1]) for i in range(len(path) - 1)
        )
        change_line_time = 3 * sum(
            1 for i in range(len(lines) - 1) if lines[i] != lines[i + 1]
        )
        total_time += change_line_time

        return [path, lines, total_time]
    else:
        return None


def run():
    initial_station = ESTACIONES["ALBERTI"]
    final_station = ESTACIONES["PERU"]
    find_path(initial_station, final_station)


if __name__ == "__main__":
    run()
