from typing import List


def get_subset_sum(arr: List[int], n: int, exisiting_subset: List[int]):
    if n >= 0:
        if n == 0:
            print(exisiting_subset)
        else:
            for i in range(len(arr)):
                new_exisiting_subset = exisiting_subset.copy()
                new_exisiting_subset.append(arr[i])
                get_subset_sum(arr[i + 1:], n - arr[i], new_exisiting_subset)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = 7
    get_subset_sum(arr, n, [])
