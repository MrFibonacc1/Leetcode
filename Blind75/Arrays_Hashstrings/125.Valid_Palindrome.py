class Solution:
    def isPalindrome(self,s:str) ->bool:
        l=0
        r=len(s)-1
        while(l<r):
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        # i=0
        # word=""
        # for i in range(len(s)):
        #     if(s[i].isalnum()):
        #         word+=s[i]
        # j=len(word)-1
        # i=0
        # word = word.lower()

        # while(i<j):

        #     if(word[i]!=word[j]):
        #         return False
        #     i+=1
        #     j-=1
        # return True

solution = Solution()
print(solution.isPalindrome("race a car"))
