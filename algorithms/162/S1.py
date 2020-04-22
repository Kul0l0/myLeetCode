from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = 0
        x_odd = set()
        y_odd = set()
        for i in indices:
            if i[0] in x_odd:
                x_odd -= set([i[0]])
            else:
                x_odd = x_odd | set([i[0]])

            if i[1] in y_odd:
                y_odd -= set([i[1]])
            else:
                y_odd = y_odd | set([i[1]])

        return len(x_odd)*m - len(x_odd)*len(y_odd)


28
38
[[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]]