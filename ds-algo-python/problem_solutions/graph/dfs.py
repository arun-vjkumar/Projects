from collections import defaultdict
from typing import List

"""
Program For Depth First Search
"""


class Graph:

    # This class represents the graph for the DFS

    # Constructor for initialising the graph, queue, traversal list
    def __init__(self):
        self.graph = defaultdict(list)
        self.stack = []
        self.traversal = []

    """Adds the edges to its corresponding vertices
    Args:
        u (int): the source vertex
        v (int): the destination vertex
    """

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)

    """Traverse the graph using DFS method
    Args:
        source (int): Represent the starting vertex
        visited List[bool]: Represents the vertex that is visited and not visited

    Returns:
        traversal (List[int]): The DFS traversed vertex order
    """

    def dfs_traversal(self, source: int, visited: List[bool]) -> List[int]:
        visited[source] = True
        self.traversal.insert(len(self.traversal), source)

        for vertex in self.graph[source]:
            if not visited[vertex]:
                self.dfs_traversal(source=vertex, visited=visited)
        return self.traversal

    def dfs_util(self, vertex_num: int) -> List[int]:
        visited = [False] * vertex_num

        return self.dfs_traversal(source=2, visited=visited)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.dfs_util(4))
