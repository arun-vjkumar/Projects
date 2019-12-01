import sys
from typing import List

"""
This is the "example" module.

The example module supplies one function, get_minimum_coins().  For example,

>>> get_minimum_coins([9, 6, 5, 1], 11)
2
"""


def get_minimum_coins(denominations: List[int], value: int) -> int:
    """ Return the minimum number of denominations required
    where the sum of denominations is equal to value.

    Args:
        denominations (List[int]): the denominations that should be considered which is list of +ve integers
        value (int): value to be considered for the denominations. raises

    Raises:
        'ValueError`: Value should be >= 0

    Returns:
        result: minimum number of denominations where sum is equal to value
    """
    if value < 0:
        raise ValueError("Value should be >= 0")

    if value == 0:
        return 0

    result: int = sys.maxsize

    for i in range(len(denominations)):
        if denominations[i] <= value:
            sub_res = get_minimum_coins(denominations=denominations, value=value - denominations[i])

            if sub_res != sys.maxsize and sub_res + 1 < result:
                result = sub_res + 1

    return result


if __name__ == '__main__':
    coins = [9, 6, 5, 1]
    value = 11
    minimum_coins_required = get_minimum_coins(denominations=coins, value=value)
    print(minimum_coins_required)
