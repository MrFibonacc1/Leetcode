class Solution:
    def characterReplacement(self, s:str, k:int) -> int:
        highest = 0
        val = k
        lp = 0
        for rp in range(len(s)):
            if s[rp] != s[lp]:
                if k == 0:
                    while s[lp] != s[rp]:
                        # k+=1
                        # if k > val:
                        #     k = val
                        lp +=1
                else:
                    k -= 1
                # print(k)
            highest = max(highest, rp-lp+1)
        return highest
    
Solution = Solution()
print(Solution.characterReplacement("ABBB",2))


# AABABBA
# rp -lp -1