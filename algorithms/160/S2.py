from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        for i in range(2**n):
            res.append(i^(i>>1))
        flag = res.index(start)
        return res[flag:] + res[:flag]

print(Solution().circularPermutation(3,1))