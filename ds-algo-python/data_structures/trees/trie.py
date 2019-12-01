class Node:
    def __init__(self):
        self.children = dict()
        self.value = None


def insert(node: Node, key: str):
    for char in key:
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
    node.value = key


def find(node: Node, key: str):
    for char in key:
        if char not in node.children:
            return None
        node = node.children[char]
    return node.value


if __name__ == '__main__':
    head = Node()
    insert(head, 'Apple')
    print(find(head, 'Apple'))
