import math
from typing import List
from app.data.data import TRAIN_FREQUENCIES, TRANSFER_COST, ENTRY_EXIT_TIME
from app.algorithms.heuristics import euclidean_time_with_stops


def calculate_travel_time(
    day: str, hour: str, path: List[str], path_details: List[str]
) -> int:
    day_details = TRAIN_FREQUENCIES[day]
    is_rush_hour = hour in day_details["rush_hours"]

    travel_time = 0
    for i in range(len(path) - 1):
        time = euclidean_time_with_stops(path[i], path[i + 1])

        if path_details[i]["line"] != path_details[i + 1]["line"]:
            time = TRANSFER_COST  # Transfer time
        elif is_rush_hour:
            time = round(time * 2)

        if i == 0:
            time += ENTRY_EXIT_TIME

        path_details[i]["travel_time"] = round(time)
        travel_time += round(time)

    path_details[len(path_details) - 1][
        "travel_time"
    ] = 0  # Restart travel time for last station

    return travel_time
