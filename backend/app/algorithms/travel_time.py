import math
from typing import List, Tuple
from app.data.data import TRAIN_FREQUENCIES
from app.config.logger import configure_logger
from app.algorithms.heuristics import time_between_stations


def calculate_travel_time(
    day: str, hour: str, path: List[str], path_details: List[str]
) -> int:
    day_details = TRAIN_FREQUENCIES[day]
    is_rush_hour = hour in day_details["rush_hours"]

    travel_time = 0
    for i in range(len(path) - 1):
        time = time_between_stations(path[i], path[i + 1])

        if path_details[i]["line"] != path_details[i + 1]["line"]:
            time = math.ceil(time * 10)  # Walking time
        elif is_rush_hour:
            time = math.ceil(time * 2)

        path_details[i]["travel_time"] = math.ceil(time)
        travel_time += math.ceil(time)

    path_details[len(path_details) - 1][
        "travel_time"
    ] = 0  # Restart travel time for last station

    return travel_time
