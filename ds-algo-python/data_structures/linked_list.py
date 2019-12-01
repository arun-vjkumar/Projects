from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T, previous_node: 'Node', next_node: 'Node') -> None:
        self.item: T = item
        self.next = next_node
        self.prev = previous_node

    def __repr__(self):
        return repr(self.item)


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self.head = None

    def prepend(self, item: T) -> None:
        self.head = Node(item=item, previous_node=None, next_node=self.head)

    def append(self, item: T) -> None:
        if not self.head:
            self.head = Node(item=item, previous_node=None, next_node=self.head)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(item=item, previous_node=curr, next_node=None)

    def get_size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_previous_of_item(self, key: T, item: T) -> str:
        curr = self.head
        while curr:
            if curr.item == key:
                temp = Node(item=item, previous_node=curr.prev, next_node=next)
                if curr.prev:
                    curr.prev.next = temp
                    temp.next = curr
                else:
                    curr.prev = temp
                    self.head = temp
                return "Inserted Successfully"
            curr = curr.next
        return "Item Not Found"

    def insert_next_of_item(self, key: T, item: T) -> str:
        curr = self.head
        while curr:
            if curr.item == key:
                curr.next = Node(item=item, previous_node=curr, next_node=curr.next)
                return "Inserted Successfully"
            curr = curr.next
        return "Item Not Found"

    def __repr__(self):
        curr = self.head
        linked_list_str = '['
        while curr:
            linked_list_str += ' {}'.format(curr.item)
            curr = curr.next
        linked_list_str += ']'
        return linked_list_str


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.prepend(5)
    ll.insert_next_of_item(5, 7)
    ll.insert_previous_of_item(7, 3)
    print(ll)
