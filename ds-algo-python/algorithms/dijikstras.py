import sys
from typing import List


def get_min_dist_vertex(dist: List[int], is_visited: List[bool]):
    min_val = sys.maxsize
    min_index = -1

    for i in range(v):
        if dist[i] < min_val and not is_visited[i]:
            min_val = dist[i]
            min_index = i
    return min_index


def dijkstra(src: int):
    is_visited = [False] * v
    dist = [sys.maxsize] * v
    dist[src] = 0

    for node in range(v):
        u = get_min_dist_vertex(dist, is_visited)
        is_visited[u] = True

        for i in range(v):
            if adjancancy_mat[u][i] > 0 and not is_visited[i] and dist[i] > dist[u] + adjancancy_mat[u][i]:
                dist[i] = dist[u] + adjancancy_mat[u][i]
    print(dist)


if __name__ == '__main__':
    v: int = 9
    adjancancy_mat = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    dijkstra(0)