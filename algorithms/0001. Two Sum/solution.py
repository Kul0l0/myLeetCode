class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        foo = {}
        for i, v in enumerate(nums):
            tmp = foo.get(target-v, None)
            if tmp is not None:
                return [tmp, i]
            foo[v] = i
        return [-1, -1]
