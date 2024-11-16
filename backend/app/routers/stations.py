from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data.data import ESTACIONES
from app.services.station_service import get_stations_with_positions, find_path

router = APIRouter()


@router.get("/stations")
async def get_stations():
    """
    Exposes all stations.
    """
    stations = get_stations_with_positions()
    return {"stations": stations}


class PathRequest(BaseModel):
    start_position: str
    final_position: str


@router.get("/path")
async def get_shortest_path(request: PathRequest):
    try:
        if request.start_position not in ESTACIONES.values():
            raise ValueError(f"Start station {request.start_position} not found")
        if request.final_position not in ESTACIONES:
            raise ValueError(f"Start station {request.start_position} not found")

        start_station = ESTACIONES[request.start_position]
        final_station = ESTACIONES[request.final_position]

        # Get path result
        path_result = find_path(start_station, final_station)

        if path_result[0] == None:
            raise ValueError("No valid path found between the stations")

        path, lines, total_time = path_result

        response = {
            "start_position": request.start_position,
            "final_position": request.final_position,
            "path": path,
            "lines": lines,
            "total_time": total_time,
        }

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid positions provided. {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
