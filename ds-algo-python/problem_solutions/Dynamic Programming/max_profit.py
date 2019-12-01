from typing import List


class MaxWineProfit:

    @classmethod
    def get_max_profit(cls, nums: List[int], year: int, begin: int, end: int) -> int:
        if begin > end:
            return 0

        num1 = (cls.get_max_profit(nums, year + 1, begin + 1, end) + (year * nums[begin])) if begin < len(nums) - 1 else 0
        num2 = (cls.get_max_profit(nums, year + 1, begin, end + 1) + (year * nums[end])) if end < len(nums) - 1 else 0
        return max(num1, num2)


if __name__ == '__main__':
    nums: List[int] = [2, 3, 5, 1, 4]
    print(MaxWineProfit.get_max_profit(nums, 1, 0, 0))
