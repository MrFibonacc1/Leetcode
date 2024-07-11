class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        seen = {}
        if len(s) == len(t):
            #O(N)
            for i in s:
                if i not in seen:
                    seen[i] = 1
                else:
                    seen[i] += 1
            #O(N)
            for i in t:
                if i in seen and seen[i]>0:
                    seen[i] -= 1
                else:
                    return False
            return True
        return False
    
Solution = Solution()
print(Solution.isAnagram("apple","ppleaa"))