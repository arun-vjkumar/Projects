from collections import defaultdict


class Combinations:
    dp = defaultdict()

    def get_num_combinations(self, n: int, r: int) -> int:
        """ The method gets the number of combinations (nCr)
        :param n: number of items
        :param r: number of items to be selected
        :return: number of possible combinations
        nCr = n-1Cr + n-1Cr-1
        """

        if r > n:
            raise AttributeError("Illegal Value r can't be > n")

        if r == 1:
            return n
        if r == n:
            return 1

        if n not in self.dp:
            self.dp[n] = defaultdict()
        self.dp[n][r] = self.get_num_combinations(n-1, r) + self.get_num_combinations(n-1, r-1)
        return self.dp[n][r]


if __name__ == '__main__':
    combination = Combinations()
    print(combination.get_num_combinations(3, 3))
