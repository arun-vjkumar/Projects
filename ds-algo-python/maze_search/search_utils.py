from typing import TypeVar, List

from maze_search import Node

T = TypeVar('T')


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
