from typing import List


def get_str_permutations(n: int, objs: List[str]) -> List[str]:
    if n == 1:
        return objs

    return [x + y
            for x in get_str_permutations(1, objs)
            for y in get_str_permutations(n - 1, objs)]


def __should_swap(string: List[str], start: int, curr: int) -> bool:
    for i in range(start, curr):
        if string[i] == string[curr]:
            return False
    return True


def find_permutations(string: List[str], index: int, size: int):
    if index >= size:
        print(''.join(string))
        return

    for i in range(index, size):
        if __should_swap(string, index, i):
            string[index], string[i] = string[i], string[index]
            find_permutations(string, index + 1, size)
            string[index], string[i] = string[i], string[index]
