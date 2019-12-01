from typing import TypeVar, Generic

from data_structures.linked_list import LinkedList, Node

T = TypeVar('T')


class BST(Generic[T]):
    def __init__(self):
        self.tree: LinkedList[T] = LinkedList()

    @classmethod
    def __insert_left(cls, node: Node, new_node: Node):
        node.prev = new_node

    @classmethod
    def __insert_right(cls, node: Node, new_node: Node):
        node.next = new_node

    def insert(self, item: T):
        new_node = Node(item=item, previous_node=None, next_node=None)
        if self.tree.get_size() == 0:
            self.tree.head = new_node
        else:
            curr, prev = self.tree.head, None
            while curr:
                prev = curr
                if curr.item <= item:
                    curr = curr.next
                else:
                    curr = curr.prev
            if prev.item >= item:
                self.__insert_left(prev, new_node)
            else:
                self.__insert_right(prev, new_node)

    def inorder_traversal(self, head: Node) -> None:
        if head:
            self.inorder_traversal(head.prev)
            print(head.item)
            self.inorder_traversal(head.next)


if __name__ == '__main__':
    bst: BST[int] = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bst.inorder_traversal(bst.tree.head)


