from typing import List


class Node:
    def __init__(self, item: int, left_node=None, right_node=None):
        self.item: int = item
        self.left: Node = left_node
        self.right: Node = right_node


def construct_segment_tree(arr: List[int], root: Node):
    if root is None:
        left_node = Node(arr[0])
        right_node = Node(arr[1])
        root = Node(left_node.item + right_node.item, left_node, right_node)
        return construct_segment_tree(arr[2:], root)
    elif len(arr) > 0:
        return construct_segment_tree(arr[1:], Node(root.item + arr[0], Node(arr[0])))
    return root


def segment_util(arr: List[int]):
    if len(arr) > 3:
        left_root = construct_segment_tree(arr[0: len(arr) // 2], None)
        right_root = construct_segment_tree(arr[len(arr) // 2:], None)
        return Node(left_root.item + right_root.item, left_root, right_root)
    return construct_segment_tree(arr, None)


if __name__ == '__main__':
    root = segment_util([i + 1 for i in range(10)])


