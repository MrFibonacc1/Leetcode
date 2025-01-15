class Solution:
    def isPalindrome(self, s:str) -> bool:
        s = s.lower()
        lp = 0
        rp = len(s)-1
        while (lp < rp):
            if not s[lp].isalnum():
                lp+=1 
                continue
            if not s[rp].isalnum():
                rp -= 1
                continue
            if s[lp] != s[rp]:
                return False
            lp+=1
            rp-=1
        return True

        # word = []
        # for char in s:
        #     if char.isalnum():
        #         word.append(char.lower())
        # return word == word[::-1]

Solution = Solution()
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))