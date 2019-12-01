from typing import TypeVar, Generic, Deque

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T, left_node: 'Node', right_node: 'Node') -> None:
        self.item: T = item
        self.left_node: 'Node' = left_node
        self.right_node: 'Node' = right_node


class BT(Generic[T]):
    def __init__(self):
        self.root: Node[T] = None
        self.path: str = ""

    @classmethod
    def __get_node(cls, item: T) -> Node:
        return Node(item=item, left_node=None, right_node=None)

    def insert(self, item: T) -> None:
        if self.root is None:
            self.root = self.__get_node(item=item)
        else:
            cur: Node[T] = self.root
            queue: Deque[T] = Deque[T]()
            queue.append(cur)
            while queue:
                cur = queue.popleft()
                if cur.left_node is not None:
                    queue.append(cur.left_node)
                if cur.right_node is not None:
                    queue.append(cur.right_node)
                if cur.left_node is None:
                    cur.left_node = self.__get_node(item=item)
                    break
                elif cur.right_node is None:
                    cur.right_node = self.__get_node(item=item)
                    break

    def traverse(self, cur: Node[T]) -> None:
        if cur is not None:
            self.traverse(cur=cur.left_node)
            self.path += "{}->".format(cur.item)
            self.traverse(cur=cur.right_node)


if __name__ == '__main__':
    binary_tree: BT[int] = BT()
    binary_tree.insert(10)
    binary_tree.insert(20)
    binary_tree.insert(30)
    binary_tree.insert(40)
    binary_tree.insert(50)
    binary_tree.insert(60)
    binary_tree.insert(70)
    binary_tree.traverse(binary_tree.root)
    print(binary_tree.path)
