class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        maxString = 0
        cur = 0
        l,r = 0,0
        while r<len(s):
            while(s[r] in map):
                cur-=1
                map.remove(s[l])
                l+=1
            map.add(s[r])
            cur+=1
            r+=1
            maxString = max(cur,maxString)

        return maxString

solution = Solution()

# Test cases
result1 = solution.lengthOfLongestSubstring("tearthe")
print(result1)