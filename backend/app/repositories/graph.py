from typing import List, Tuple
import networkx as nx


class MetroGraph(nx.Graph):
    def __init__(self, stations=None, connections=None, *args, **kwargs):
        """
        Initializes a MetroGraph with optional nodes (stations), edges (connections),
        and line color attributes for each node.

        :param stations: List of station names (nodes).
        :param connections: List of tuples representing connections (edges).
        """
        super().__init__(*args, **kwargs)

        if stations:
            self.add_stations(stations)
            self.stations = self.nodes

        if connections:
            self.add_connections(connections)

    def add_stations(self, stations: List[str]):
        """Adds a list of stations (nodes) to the graph."""
        for station in stations:
            self.add_node(
                station["id"],
                id=station["id"],
                name=station["name"],
                position=station["position"],
                line=station["line"],
            )

    def add_connections(self, connections: List[Tuple[str, str]]):
        """Adds a list of connections (edges) between stations."""
        self.add_edges_from(connections)
