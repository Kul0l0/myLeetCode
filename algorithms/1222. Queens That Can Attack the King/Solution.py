from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def distc(x, y):
            return abs(x[0]-y[0])**2 + abs(x[1]-y[1])**2
        def oneline(x, y):
            if x[0]==y[0]:
                if x[1] > y[1]:
                    return 1
                else:
                    return 2
            if x[1]==y[1]:
                if x[0] > y[0]:
                    return 3
                else:
                    return 4
            if (x[0]-y[0])==(x[1]-y[1]):
                if x[1] > y[1]:
                    return 5
                else:
                    return 6
            if (x[0]-y[0])==(x[1]-y[1])*-1:
                if x[1] > y[1]:
                    return 7
                else:
                    return 8
            return 0

        res = {}
        ds = {}
        for q in queens:
            site = oneline(king, q)
            if site != 0:
                d = distc(king, q)
                # print(king, q, site, d)
                if ds.get(site, 999) > d:
                    ds[site] = d
                    res[site] = q
        return list(res.values())

queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]
#Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
print(Solution().queensAttacktheKing(queens, king))
#Output: [[0,1],[1,0],[3,3]]