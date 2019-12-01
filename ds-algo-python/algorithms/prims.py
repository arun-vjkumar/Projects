import sys
from typing import List


def get_min_key(key, is_visited: List[bool]):
    max_index = -1
    max_val = sys.maxsize

    for i in range(v):
        if key[i] < max_val and not is_visited[i]:
            max_val = key[i]
            max_index = i
    return max_index


def print_mst(parent):
        print("Edge \tWeight")
        for i in range(1, v):
            print(parent[i], "-", i, "\t", adjancancy_mat[i][parent[i]])


def prims(src: int):
    key = [sys.maxsize] * v
    parent = [None] * v
    key[0] = 0
    parent[0] = -1
    mstSet = [False] * v

    for node in range(v):
        u = get_min_key(key, mstSet)
        mstSet[u] = True

        for i in range(v):
            if 0 < adjancancy_mat[u][i] < key[i] and not mstSet[i]:
                key[i] = adjancancy_mat[u][i]
                parent[i] = u

    print_mst(parent)


if __name__ == '__main__':
    v = 5
    adjancancy_mat = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    prims(0)

