from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper+lower != sum(colsum):
            return []

        res = [[0]*len(colsum), [0]*len(colsum)]

        for i, val in enumerate(colsum):
            if val == 2:
                upper -= 1
                lower -= 1
                res[0][i] = 1
                res[1][i] = 1

        for i, val in enumerate(colsum):
            if val == 1:
                if upper > 0:
                    upper -= 1
                    res[0][i] = 1
                else:
                    lower -= 1
                    res[1][i] = 1

            if lower < 0:
                return []

        return res