from data_structures.stack import Stack


class TOH:
    def hanoi(self, begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
        if n == 1:
            end.push(begin.pop())
        else:
            self.hanoi(begin, temp, end, n-1)
            self.hanoi(begin, end, temp, 1)
            self.hanoi(temp, end, begin, n-1)


if __name__ == '__main__':
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    toh = TOH()
    toh.hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
