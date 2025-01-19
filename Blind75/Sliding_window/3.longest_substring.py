class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        charSet = set()
        lp = 0
        length = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[lp])
                lp+=1
            charSet.add(s[r])
            length = max(length,r-lp+1)
        return length

Solution = Solution()
print(Solution.lengthOfLongestSubstring("abcasaa"))