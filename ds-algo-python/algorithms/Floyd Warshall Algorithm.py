# Python Program for Floyd Warshall Algorithm 
from sys import maxsize
from typing import List

v = 4

INF = maxsize

"""Solves all pair shortest path via Floyd Warshall Algorithm

   Args:
        graph List[List]: Represents the dist between two vertex
"""


def floyd_warshall(dist_graph: List[List]):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist_graph[i][j] = min(dist_graph[i][j], dist_graph[i][k] + dist_graph[k][j])

    for row in dist_graph:
        print([col if col != INF else -1 for col in row])


if __name__ == '__main__':
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    floyd_warshall(graph)

