from typing import TypeVar, List

T = TypeVar('T')


def merge_sort(list_to_sort: List[T]):
    if len(list_to_sort) > 1:
        mid_index = len(list_to_sort) // 2
        left_arr = list_to_sort[: mid_index]
        right_arr = list_to_sort[mid_index:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                list_to_sort[k] = left_arr[i]
                i += 1
            else:
                list_to_sort[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            list_to_sort[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            list_to_sort[k] = right_arr[j]
            j += 1
            k += 1
