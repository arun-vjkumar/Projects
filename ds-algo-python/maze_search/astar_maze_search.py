
from typing import List, Optional, TypeVar, Dict, Callable

from maze_search import PriorityQueue, Node
from maze_search.maze import MazeLocation, Maze
from maze_search.search_utils import node_to_path

T = TypeVar('T')


def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        x_dist: int = abs(ml.column - goal.column)
        y_dist: int = abs(ml.row - goal.row)
        return x_dist + y_dist
    return distance


def astar(initial: T, goal_test: Callable[[T], bool],
          successors: Callable[[T], List[T]],
          heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))

    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            new_cost: float = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


if __name__ == '__main__':
    m: Maze = Maze(10, 10, 0.2, MazeLocation(0, 0), MazeLocation(9, 9))
    distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.get_all_successors, distance)
    if solution3 is None:
        print("No solution found using A*!")
    else:
        path3: List[MazeLocation] = node_to_path(solution3)
        m.mark(path3)
        print(m)