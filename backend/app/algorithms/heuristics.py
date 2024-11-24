from math import sqrt
from app.data.data import VELOCITY, STATIONS_POSITION, STOP_TIME


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


def euclidean_time(
    start_station: str, final_station: str, velocity: float = VELOCITY
) -> float:
    """
    Calculate the time it takes to travel between two stations, given their positions.

    Args:
        start_station (str): The identifier for the starting station.
        final_station (str): The identifier for the destination station.
        velocity (float): The velocity at which the train is traveling (default is VELOCITY).

    Returns:
        float: The time required to travel between the two stations, in minutes.
    """

    return distance_between_stations(start_station, final_station) / velocity


def euclidean_time_with_stops(
    start_station: str,
    final_station: str,
    stop_time: float = STOP_TIME,
    velocity: float = VELOCITY,
) -> float:
    """
    Calculate the time it takes to travel between two stations, given their positions, and considering stop time before leaving in start station

    Args:
        start_station (str): The identifier for the starting station.
        final_station (str): The identifier for the destination station.
        stop_time (float): The stop time at the station.
        velocity (float): The velocity at which the train is traveling (default is VELOCITY).

    Returns:
        float: The time required to travel between the two stations, in minutes.
    """
    return euclidean_time(start_station, final_station, velocity) + stop_time


def heuristic_between_stations(start_station: str, final_station: str) -> float:
    """
    Calculate the time it takes to travel between two stations, given their positions

    Args:
        start_station (str): The identifier for the starting station.
        final_station (str): The identifier for the destination station.

    Returns:
        float: The time required to travel between the two stations, in minutes.
    """
    time = euclidean_time(start_station, final_station)
    return time
