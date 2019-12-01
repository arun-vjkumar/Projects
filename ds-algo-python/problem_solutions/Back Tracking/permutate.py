from typing import List


class Permutate:
    @classmethod
    def create_permutation(cls, n: int, objs: List[str]):
        if n == 1:
            return objs

        return [x + y
                for x in cls.create_permutation(1, objs)
                for y in cls.create_permutation(n - 1, objs)]


if __name__ == '__main__':
    print(Permutate.create_permutation(2, ["a", "b", "c"]))
