from typing import Optional, List, Tuple
import networkx as nx
import heapq
from app.algorithms.heuristics import (
    euclidean_time_with_stops,
    heuristic_between_stations,
)
from app.data.data import TRANSFER_COST


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
    # Dictionary to keep track of g scores (actual distance from start)
    g_scores = {start_node: 0}
    # Set to keep track of the visited nodes
    visited = set()
    # Dictionary to store best parent for each node
    came_from = {}
    # Dictionary to store the line used to reach each node
    line_used = {}

    # Initial heuristic calculation
    initial_f = g_scores[start_node] + heuristic_between_stations(
        start_node, final_node
    )

    # Push initial node into the heap (f_score, current_node)
    heapq.heappush(open_heap, (initial_f, start_node))

    while open_heap:
        _, current_node = heapq.heappop(open_heap)

        if current_node == final_node:
            path = []
            lines = []
            current = final_node

            while current in came_from:
                path.append(current)
                if current in line_used:
                    lines.append(line_used[current])
                current = came_from[current]

            path.append(start_node)
            path.reverse()
            lines.reverse()
            return path, lines

        visited.add(current_node)

        for neighbor in graph[current_node]:
            current_line = graph.nodes[current_node].get("line", "Unknown")
            neighbor_line = graph.nodes[neighbor].get("line", "Unknown")

            transfer_cost = 0
            if current_line != neighbor_line:
                transfer_cost = TRANSFER_COST

            tentative_g = (
                g_scores[current_node]
                + euclidean_time_with_stops(current_node, neighbor)
                + transfer_cost
            )

            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                # This path is better
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic_between_stations(neighbor, final_node)

                # Get line info
                line_used[neighbor] = current_line

                if (f_score, neighbor) not in open_heap:
                    heapq.heappush(open_heap, (f_score, neighbor))

    return None, None
