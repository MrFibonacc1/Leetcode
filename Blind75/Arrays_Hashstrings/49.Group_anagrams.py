class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        if len(strs) <= 1:
            return [strs]
        dict = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word in dict:
                dict[word].append(i)
            else:
                dict[word] = [i]
        returnVal = []
        for val in dict.values():
            returnVal.append(val)
        return returnVal

solution = Solution()
print(solution.groupAnagram([""]))