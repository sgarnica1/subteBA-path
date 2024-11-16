from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from app.data.data import STATIONS
from app.services.station_service import get_stations_with_positions, find_path

router = APIRouter()


@router.get("/stations")
async def get_stations():
    """
    Retrieve all stations with their respective positions.

    This endpoint returns a dict of all stations with their positions.
    It fetches the data from the underlying service layer.

    Returns:
        dict: A dictionary containing a dict of stations with positions.
    """
    data = get_stations_with_positions()
    return data


class PathRequest(BaseModel):
    """
    Request model for the shortest path endpoint.
    """

    start_position: str
    final_position: str


@router.get("/path")
async def get_shortest_path(
    start_position: str = Query(..., description="The name of the starting station"),
    final_position: str = Query(..., description="The name of the destination station"),
):
    """
    Find the shortest path between two stations.

    This endpoint calculates the shortest path between a given start and
    end station. It validates the station names and uses the underlying
    service to compute the path, the lines taken, and the total travel time.

    Args:
        start_position (str): The name of the starting station.
        final_position (str): The name of the ending station.

    Returns:
        dict: A dictionary containing the following:
            - start_position: The name of the starting station.
            - final_position: The name of the ending station.
            - path: The list of station names in the shortest path.
            - lines: The list of lines taken in the shortest path.
            - total_time: The total time for the journey, including line changes.

    Raises:
        HTTPException: If the start or end station is invalid, or no path is found.
    """
    try:
        if start_position not in STATIONS.values():
            raise ValueError(f"Start station {start_position} not found")
        if final_position not in STATIONS.values():
            raise ValueError(f"Destination station {final_position} not found")

        start_station = STATIONS[start_position]
        final_station = STATIONS[final_position]

        # Get path result
        path_result = find_path(start_station, final_station)

        if path_result[0] is None:
            raise ValueError("No valid path found between the stations")

        path, lines, total_time = path_result

        response = {
            "start_position": start_position,
            "final_position": final_position,
            "path": path,
            "lines": lines,
            "total_time": total_time,
        }

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid positions provided. {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
