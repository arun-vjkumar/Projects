from collections import KeysView


class Node:
    def __init__(self):
        self.children = dict()
        self.value = None


def get_matching_prefix(str1: str, str2: str):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return str2[0: i]
    return str1 if len(str1) < len(str2) else str2


def get_key_with_prefix(value: str, keys: KeysView):
    for key in keys:
        prefix = get_matching_prefix(value, key)
        if prefix:
            return prefix, key
    return None, None


def insert_ang_get_key_range(node: Node, value: str, from_index: int, to_index: int):
    if value[from_index: to_index] in node.children:
        node.children[value[from_index: to_index]] = Node()
        node = node.children[value[from_index: to_index]]
        node.value = value[from_index: to_index]
    else:
        prefix, key = get_key_with_prefix(value[from_index: to_index], node.children.keys())
        if prefix is None:
            node.children[value[from_index: to_index]] = Node()
            node = node.children[value[from_index: to_index]]
            node.value = value[from_index: to_index]
        elif prefix != key:
            del node.children[key]

            node.children[prefix] = Node()
            node = node.children[prefix]
            node.value = prefix
            prev_node = node

            node.children[key[len(prefix):]] = Node()
            node = node.children[key[len(prefix):]]
            node.value = key[len(prefix):]

            return prev_node, from_index + len(prefix), to_index
        elif prefix == key:
            return node.children[prefix], from_index + len(prefix), to_index
    return node, to_index, to_index


def insert(node: Node, value: str):
    from_index, to_index = 0, len(value)
    while from_index < to_index:
        node, from_index, to_index = insert_ang_get_key_range(node, value, from_index, to_index)


def find(node: Node, value: str):
    found_value = ""
    val_to_find = value
    while val_to_find:
        prefix, key = get_key_with_prefix(val_to_find, node.children.keys())
        if prefix is None:
            return found_value if found_value == value else None
        node = node.children[prefix]
        val_to_find = val_to_find[len(prefix):]
        found_value += prefix
    return found_value if found_value == value else None


if __name__ == '__main__':
    head = Node()
    insert(head, 'Apple')
    insert(head, 'Aero')
    insert(head, 'Aeroplane')
    insert(head, 'Aerospace')
    print(find(head, 'Aerospace'))
    print(find(head, 'Aero'))
    print(find(head, 'Air'))
