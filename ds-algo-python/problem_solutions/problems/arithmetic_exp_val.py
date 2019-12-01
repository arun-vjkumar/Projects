import ast


def eval_exp(op: str, num1: int, num2: int) -> int:
    return ast.literal_eval(f'{num1} op {num2}')


def find_max_min(expression: str):
    min_mat = [[0 for _ in range(len(expression) // 2 + 1)] for _ in range(len(expression) // 2 + 1)]
    max_mat = [[0 for _ in range(len(expression) // 2 + 1)] for _ in range(len(expression) // 2 + 1)]

