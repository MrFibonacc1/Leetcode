class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}
        for i in s:
            dict[i] = 1 + dict.get(i,0)
        for i in t:
            if i in dict and dict[i] > 0:
                dict[i] -= 1
            else:
                return False
        return True

        #Another way can be to sort each word and compare them
        #Test
solution = Solution()
print(solution.isAnagram("anagram","nagaram"))