class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if len(stack)>0 and stack[-1]!=i:
                stack.pop(-1)
                if len(stack) == 0:
                    res += 1
            else:
                stack.append(i)
        return res

s = "RLRRLLRLRL"
# s = "RLLLLRRRLR"
# s = "LLLLRRRR"
print(Solution().balancedStringSplit(s))