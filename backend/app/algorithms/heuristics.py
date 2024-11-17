from math import sqrt
from typing import Tuple
from app.data.data import VELOCITY, STATIONS_POSITION


def distance_between_points(
    pos1: Tuple[float, float], pos2: Tuple[float, float]
) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        pos1 (Tuple[float, float]): The coordinates of the first point (x1, y1).
        pos2 (Tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The distance between the two points, scaled by 800 (to match your system's units).
    """
    x1, y1 = pos1
    x2, y2 = pos2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 800


def time_between_stations(
    start_station: str, final_station: str, velocity: float = VELOCITY
) -> float:
    """
    Calculate the time it takes to travel between two stations, given their positions.

    Args:
        start_station (str): The identifier for the starting station.
        final_station (str): The identifier for the destination station.
        velocity (float): The velocity at which the train is traveling (default is VELOCIDAD).

    Returns:
        float: The time required to travel between the two stations, in minutes.
    """
    start_position = STATIONS_POSITION[start_station]["position"]
    final_station = STATIONS_POSITION[final_station]["position"]
    return distance_between_points(start_position, final_station) / velocity
