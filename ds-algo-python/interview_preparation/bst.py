from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T, left_node: 'Node', right_node: 'Node') -> None:
        self.item: T = item
        self.left_node: 'Node' = left_node
        self.right_node: 'Node' = right_node


class BST(Generic[T]):
    def __init__(self):
        self.root: Node[T] = None
        self.traversed: str = ''

    @classmethod
    def __get_node(cls, item: T) -> Node[T]:
        return Node(item=item, left_node=None, right_node=None)

    def insert(self,  item: T) -> None:
        if self.root is None:
            self.root = self.__get_node(item=item)

        cur_node = self.root
        previous_node = None

        while cur_node:
            previous_node = cur_node
            if item < cur_node.item:
                cur_node = cur_node.left_node
            else:
                cur_node = cur_node.right_node

        if item < previous_node.item:
            previous_node.left_node = self.__get_node(item=item)
        else:
            previous_node.right_node = self.__get_node(item=item)

    def traversal(self, cur: Node[T]) -> None:
        if cur is not None:
            self.traversal(cur=cur.left_node)
            self.traversed += "{}->".format(cur.item)
            self.traversal(cur=cur.right_node)


if __name__ == '__main__':
    bst: BST[int] = BST()
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)
    bst.insert(40)
    bst.insert(35)
    bst.insert(50)
    bst.traversal(bst.root)
    print(bst.traversed)
