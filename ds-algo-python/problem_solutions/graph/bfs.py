from collections import defaultdict
from typing import List

"""
Program For Breadth First Search
"""


class Graph:

    # This class represents the graph for the BFS

    # Constructor for initialising the graph, queue, traversal list
    def __init__(self):
        self.graph = defaultdict(list)
        self.queue = []
        self.traversal = []

    """Adds the edges to its corresponding vertices
    Args:
        u (int): the source vertex
        v (int): the destination vertex
    """
    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)

    """Traverse the graph using BFS method
    Args:
        source (int): Represent the starting vertex
        vertex_num (int): Represents the number of vertex in the graph
        
    Returns:
        traversal (List[int]): The BFS traversed vertex order
    """
    def bfs_traversal(self, source: int, vertex_num: int) -> List[int]:
        visited = [False] * vertex_num
        visited[source] = True
        self.queue.append(source)

        while len(self.queue):
            s = self.queue.pop(0)
            self.traversal.append(s)

            for i in self.graph[s]:
                if not visited[i]:
                    self.queue.append(i)
                    visited[i] = True
        return self.traversal


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.bfs_traversal(2, 4))
