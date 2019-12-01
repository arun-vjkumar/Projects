"""
Get the max sum of subsequent 2 subarray for size m, n
"""

from typing import List


def get_max_subset_sum(arr: List[int], n: int):
    max_sum_subset = 0
    for i in range(len(arr) - n):
        temp = sum(arr[i: i + n])
        if max_sum_subset < temp:
            max_sum_subset = temp
    return max_sum_subset


def get_max_sum_of_subarray(arr: List[int], m: int, n: int):
    if len(arr) < m + n:
        return -1
    max_sum = 0

    for i in range(0, len(arr) - m + n):
        temp = max(sum(arr[i: i + m]) + get_max_subset_sum(arr[i + m:], n), sum(arr[i: i + n]) + get_max_subset_sum(arr[i + n:], m))
        if max_sum < temp:
            max_sum = temp
    return max_sum


if __name__ == '__main__':
    print(get_max_sum_of_subarray([1, 4, 5, 7, 8, 4, 8, 5], 3, 2))