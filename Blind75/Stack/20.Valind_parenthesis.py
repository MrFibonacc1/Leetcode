class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        coll = {"(", "{", "["}
        for i in range(len(s)):
            if s[i] in coll:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
            char = stack.pop()
            if not ((s[i] == ")" and char == "(") or (s[i] == "}" and char == "{") or (s[i] == "]" and char == "[")):
                return False
        return len(stack) == 0

Solution = Solution()
print(Solution.isValid("([])"))