from typing import List, Tuple
import networkx as nx


class MetroGraph(nx.Graph):
    def __init__(
        self, stations=None, connections=None, line_colors=None, *args, **kwargs
    ):
        """
        Initializes a MetroGraph with optional nodes (stations), edges (connections),
        and line color attributes for each node.

        :param stations: List of station names (nodes).
        :param connections: List of tuples representing connections (edges).
        :param line_colors: Dictionary mapping station names to line colors.
        """
        super().__init__(*args, **kwargs)

        if stations:
            self.add_stations(stations)
            self.stations = self.nodes

        if connections:
            self.add_connections(connections)

    def add_stations(self, stations: List[str]):
        """Adds a list of stations (nodes) to the graph."""
        self.add_nodes_from(stations)

    def add_connections(self, connections: List[Tuple[str, str]]):
        """Adds a list of connections (edges) between stations."""
        self.add_edges_from(connections)

    def add_line_to_stations(self, stations, line_name: str):
        for station in stations:
            self.stations[station]["linea"] = line_name

    def get_station_line(self, station):
        """
        Returns the line color of a station.

        :param station: Name of the station node.
        :return: Line color of the station.
        """
        return self.nodes[station].get("color", "Unknown")
