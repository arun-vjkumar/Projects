from typing import TypeVar, Callable, List, Optional, Set

from maze_search import Queue, Node
from maze_search.maze import Maze, MazeLocation
from maze_search.search_utils import node_to_path

T = TypeVar('T')


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored: Set[T] = {initial}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


if __name__ == '__main__':
    # Test BFS
    m: Maze = Maze(10, 10, 0.2, MazeLocation(0, 0), MazeLocation(9, 9))
    print(m)
    solution1: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.get_all_successors)
    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)




