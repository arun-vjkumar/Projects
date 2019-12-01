from typing import List


class LSQ:
    """
    Finding the longest subsequence b/w two string s1 and s2
    """

    @classmethod
    def get_longest_subsquence_iteration_method(cls, s1: str, s2: str) -> int:
        result: List[List[int]] = [[int(0) for _ in range(len(s1))] for _ in range(len(s2))]

        for i in range(0, len(s2)):
            for j in range(0, len(s1)):
                if s2[i] == s1[j]:
                    result[i][j] = result[i - 1][j - 1] + 1
                else:
                    result[i][j] = max(result[i - 1][j],  result[i][j - 1])
        return result[len(s2) - 1][len(s1) - 1]


if __name__ == '__main__':
    print(LSQ.get_longest_subsquence_iteration_method("abkcd", "asbcd"))
