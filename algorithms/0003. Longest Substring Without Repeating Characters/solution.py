class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def maxlen(s, l, r):
            if l+1 == r:
                return 1
            maxl = 0
            loop = {}
            i = l
            while i < r:
                if loop.get(s[i], None) is None:
                    loop[s[i]] = i
                    maxl += 1
                    i += 1
                else:
                    break
            # print(maxl, s[l:i])
            if i == r:
                return maxl
            else:
                return max(maxl, maxlen(s, loop[s[i]] + 1, len(s)))

        return maxlen(s, 0, len(s))

foo = Solution()
print(foo.lengthOfLongestSubstring('pwwkew'))