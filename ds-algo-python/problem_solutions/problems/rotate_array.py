from typing import List, TypeVar

T = TypeVar('T')


def rotate_right(arr: List[T], n: int) -> List[T]:
    left_ptr = (n % len(arr)) - 1
    arr[:left_ptr], arr[left_ptr + 1:] = arr[(n - left_ptr) - 1:], arr[: (n - left_ptr)]
    return arr


if __name__ == '__main__':
    arr: List[int] = [1, 2, 3, 4, 5]
    print(rotate_right(arr=arr, n=3))
