from typing import Optional, List, Tuple
import networkx as nx
import heapq
from app.algorithms.heuristics import time_between_stations
from app.config.logger import configure_logger

logger = configure_logger()


def a_star(
    start_node: str, final_node: str, graph: nx.Graph
) -> Optional[Tuple[List[str], List[str]]]:
    """
    A* search algorithm to find the shortest path between two nodes in a graph.

    Args:
        start_node (str): The starting node identifier.
        final_node (str): The destination node identifier.
        graph (nx.Graph): A NetworkX graph where nodes represent stations.

    Returns:
        Optional[Tuple[List[str], List[str]]]:
            - If a path is found, returns a tuple containing:
              1. List of nodes representing the path.
              2. List of lines corresponding to each segment of the path.
            - If no path is found, returns (None, None).
    """
    # Priority queue to hold nodes to explore
    open_heap = []
    # Set to keep track of visited nodes
    visited = set()
    # Push initial node into the heap (time, current_node, path, lines)
    heapq.heappush(open_heap, (0, start_node, [], []))

    while open_heap:
        time, current_node, path, lines = heapq.heappop(open_heap)
        if current_node == final_node:
            return path + [current_node], lines

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    total_time = time_between_stations(current_node, neighbor)
                    new_time = time + total_time
                    heuristic = time_between_stations(neighbor, final_node)
                    current_line = graph.nodes[current_node].get(
                        "line", "Unknown"
                    )  # Cambio aquí
                    if len(lines) == 0 or lines[-1] != current_line:
                        new_lines = lines + [current_line]
                    else:
                        new_lines = lines.copy()
                    new_node = (
                        new_time + heuristic,
                        neighbor,
                        path + [current_node],
                        new_lines,
                    )
                    heapq.heappush(open_heap, new_node)

    return None, None
