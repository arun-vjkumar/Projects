from typing import List


class MaxSum:
    """
    Finds the max sum of number with constraints not selecting the adjacent numbers
    """

    sum_1 = sum_2 = 0
    @classmethod
    def get_next_two_positive_numbers(cls, nums: List[int]):
        first_pos_index = second_pos_index = None
        for index, num in enumerate(nums):
            if num > 0:
                if first_pos_index is None:
                    first_pos_index = index
                else:
                    second_pos_index = index
                    break
        return [first_pos_index, second_pos_index]

    def get_max_sum(self, nums: List[int]):
        if len(nums) == 1:
            return
            # if nums[0] > 0:
            #     return nums[0]
            # else:
            #     return 0
        else:
            first_pos_index, second_pos_index = self.get_next_two_positive_numbers(nums=nums)
            if first_pos_index:
                self.sum_1 += nums[first_pos_index]
                if first_pos_index < len(nums) - 1:
                    self.get_max_sum(nums[first_pos_index + 1:])

            if second_pos_index:
                self.sum_2 += nums[second_pos_index]
                if second_pos_index < len(nums) - 1:
                    self.get_max_sum(nums[second_pos_index + 1:])

            # return max(sum_1, sum_2)


if __name__ == '__main__':
    max_sum = MaxSum()
    print(max_sum.get_max_sum([-1, 5, 4, -2, 5, -3, -5, 6, 7]))
    print(max_sum.sum_1)
    print(max_sum.sum_2)
