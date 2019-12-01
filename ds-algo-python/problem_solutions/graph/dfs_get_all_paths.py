from collections import defaultdict
from typing import List, Generator


class DFSPathTraversal:

    def __init__(self, vertices_count: int) -> None:
        self.vertices_count = vertices_count
        self.edges = defaultdict(list)
        self.paths = defaultdict(list)

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self.edges[from_vertex].append(to_vertex)

    def get_all_dfs_path(self, src: int, dest: int) -> None:
        is_visited: List[bool] = [False] * self.vertices_count
        exisiting_paths = []
        self.find_all_dfs_path(src=src, dest=dest, from_vertex=src, to_vertex=dest, is_visited=is_visited,
                               existing_path=exisiting_paths)
        for path in self.paths['{}->{}'.format(src, dest)]:
            print(path.__repr__())

    def find_all_dfs_path(self, src: int, dest: int, from_vertex: int, to_vertex: int, is_visited: List[bool], existing_path: List[int]):
        is_visited[from_vertex] = True
        existing_path.append(from_vertex)

        if from_vertex == to_vertex:
            self.paths['{}->{}'.format(src, dest)].append(existing_path.copy())
        else:
            for vertex in self.edges[from_vertex]:
                if not is_visited[vertex]:
                    self.find_all_dfs_path(src=src, dest=dest, from_vertex=vertex, to_vertex=to_vertex,
                                           is_visited=is_visited, existing_path=existing_path)

        existing_path.pop()
        is_visited[from_vertex] = False


if __name__ == '__main__':
    # Create a graph given in the above diagram
    g = DFSPathTraversal(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(1, 3)

    s = 2
    d = 3
    print("Following are all different paths from %d to %d :" % (s, d))
    g.get_all_dfs_path(s, d)
