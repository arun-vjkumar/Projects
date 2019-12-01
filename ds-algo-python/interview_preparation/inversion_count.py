"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
"""

# inversion count using bubble sort
from typing import List


def bubble_sort_inversion_count(arr: List[int]) -> int:
    inversion_count: int = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                inversion_count += 1
    return inversion_count


if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    print("Number of inversions are", bubble_sort_inversion_count(arr))
