class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        hash2 = {}
        for i in s:
            if i in hash:
                hash[i] = hash[i]+1
            else:
                hash[i] = 1
        for i in t:
            if i in hash2:
                hash2[i] = hash2[i]+1
            else:
                hash2[i] = 1
        return hash == hash2
        
                    