from typing import List


def get_probe_position(arr: List[int], low: int, high: int, key: int) ->  int:
    return int(low + ((high - low) / (arr[high] - arr[low])) * (key - arr[low]))


def interpolation_search(arr: List[int], key: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    comparsions: int = 0

    while low <= high:
        comparsions += 1
        mid = get_probe_position(arr, low, high, key)

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        return -1


if __name__ == '__main__':
    arr: List[int] = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    key: int = 33
    print(interpolation_search(arr, 33))