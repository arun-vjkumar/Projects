from typing import List


def bubble_sort(arr: List[int]):
    for i in range(len(arr) - 1):
        swaps: int = 0
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swaps == 0:
            break
    print(arr)


if __name__ == '__main__':
    bubble_sort([8, 5, 6, 3, 7, 4, 1])
