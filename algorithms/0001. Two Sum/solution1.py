class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            if target-v in nums and i != nums.index(target-v):
                return sorted([nums.index(target-v), i])
        return [-1, -1]