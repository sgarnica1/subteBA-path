from typing import List
from app.data.data import TRAIN_FREQUENCIES, TRANSFER_COST
from app.algorithms.heuristics import euclidean_time_with_stops


def calculate_travel_time(path: List[str], path_details: List[str]) -> int:
    travel_time = 0
    for i in range(len(path) - 1):
        time = euclidean_time_with_stops(path[i], path[i + 1])

        if path_details[i]["line"] != path_details[i + 1]["line"]:
            time = TRANSFER_COST  # Transfer time

        path_details[i]["travel_time"] = round(time)
        travel_time += round(time)

    path_details[len(path_details) - 1][
        "travel_time"
    ] = 0  # Restart travel time for last station

    return travel_time
