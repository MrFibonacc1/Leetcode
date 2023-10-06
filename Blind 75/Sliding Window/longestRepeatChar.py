class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCons = 0
        if len(s)>0:
            char = s[0]
        l,r = 0,1
        cur = 1
        space = k
        while r<len(s):
            if s[r]==char:
                cur+=1
                r+=1
            else:
                space-=1
                if space<0:
                    while s[l]!=:
                        continue

                cur+=1
                maxCons = max(cur,maxCons)
                r+=1

                
        return maxCons

solution = Solution()

# Test cases
result1 = solution.characterReplacement("ABAB",1)
print(result1)