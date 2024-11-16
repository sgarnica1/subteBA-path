# heuristics.py
from math import sqrt
from typing import Tuple
from app.data.data import VELOCIDAD, ESTACIONES_POSICIONES


def distance_between_points(
    pos1: Tuple[float, float], pos2: Tuple[float, float]
) -> float:
    x1, y1 = pos1
    x2, y2 = pos2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 800


def time_between_stations(
    start_station: str, final_station: str, velocity: float = VELOCIDAD
) -> float:
    start_position = ESTACIONES_POSICIONES[start_station]["position"]
    final_station = ESTACIONES_POSICIONES[final_station]["position"]
    return distance_between_points(start_position, final_station) / velocity
