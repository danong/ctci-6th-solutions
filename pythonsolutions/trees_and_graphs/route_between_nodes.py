from __future__ import annotations

from collections import deque
from typing import List


class Node:
    def __init__(self, val: object) -> None:
        self.val = val
        self.neighbors = set()

    def add_neighbor(self, node: Node) -> None:
        self.neighbors.add(node)


class Graph:
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes


def find_route(graph: Graph, start_node: Node, end_node: Node) -> bool:
    """Determine if a route exists between two nodes in a graph

    Args:
        graph:
        start_node:
        end_node:

    Returns:
        Whether a route exists or not
    """
    # easy edge cases
    if start_node is end_node:  # making an assumption
        return True
    if end_node not in graph.nodes or start_node not in graph.nodes:
        return False

    visited = set()
    to_visit = deque()
    to_visit.append(start_node)

    while to_visit:
        curr_node = to_visit.popleft()
        visited.add(curr_node)
        for neighbor in curr_node.neighbors:
            if neighbor not in visited:
                if neighbor is end_node:
                    return True
                to_visit.append(neighbor)

    return False
