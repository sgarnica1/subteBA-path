from math import sqrt
from typing import Tuple
from app.data.data import VELOCITY, STATIONS_POSITION


def distance_between_stations(pos1: str, pos2: str) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        start_station (str): The identifier for the starting station.
        final_station (str): The identifier for the destination station.

    Returns:
        float: The distance between the two points in meters (Multiplied by 100,000 to scale to meters in Google Maps).
    """
    start_station = STATIONS_POSITION[pos1]["position"]
    final_station = STATIONS_POSITION[pos2]["position"]
    x1, y1 = start_station
    x2, y2 = final_station

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 100000


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

    return distance_between_stations(start_station, final_station) / velocity
