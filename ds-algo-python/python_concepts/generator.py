from collections import Generator


def fibonacci(n: int) -> Generator:
    yield 0
    if n > 0:
        yield 1

    prev_val: int = 0
    next_val: int = 1

    for i in range(1, n):
        prev_val, next_val = next_val, prev_val + next_val
        yield next_val


if __name__ == '__main__':
    for val in fibonacci(10):
        print(val)
