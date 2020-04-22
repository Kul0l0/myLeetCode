from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def roll(n, now, before, rollMax):
            if n == 1:
                r = 0
                for i in now:
                    if i!=0:
                        r += 1
                return r

            res = 0
            for i in range(6):
                if now[i] >= 1:
                    if i==before:
                        rm = now[:]
                    else:
                        rm = rollMax[:]
                    rm[i] -= 1
                    # print(n, i+1, rm)
                    res += roll(n-1, rm, i, rollMax)
                    # print(res)
            return res
        return roll(n, rollMax, 0, rollMax)

n = 10
rollMax = [2,7,1,2,6,5]
print(Solution().dieSimulator(n, rollMax))

a = dict()
a.update()