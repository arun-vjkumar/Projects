class Node:
    def __init__(self, item: int):
        self.item: int = item
        self.left: Node = None
        self.right: Node = None


def __get_height(node: Node):
    if node is None:
        return 0
    ldepth = __get_height(node.left)
    rdepth = __get_height(node.right)

    return ldepth + 1 if ldepth >= rdepth else rdepth + 1


def get_balance_factor(root: Node):
    return __get_height(root.right) - __get_height(root.left)


def __rotate_right(root: Node):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root


def __rotate_left(root: Node):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root


def balance_tree(root: Node):
    bal_fact = get_balance_factor(root)
    if bal_fact == 2:
        return __rotate_left(root)
    elif bal_fact == -2:
        return __rotate_right(root)
    return root


def insert(root: Node, item: int) -> Node:
    temp = Node(item=item)
    if root is None:
        return temp
    cur = root
    while cur:
        if item < cur.item:
            if cur.left is None:
                cur.left = temp
                break
            cur = cur.left

        if item >= cur.item:
            if cur.right is None:
                cur.right = temp
                break
            cur = cur.right

    return balance_tree(root)


def __in_order(root: Node):
    if root:
        __in_order(root.left)
        print(root.item)
        __in_order(root.right)


if __name__ == '__main__':
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)
    print(__in_order(root))