class Solution:
    def isValid(self, s:str) -> bool:
        sym = ("(", "[", "{")
        stack = []
        for i in range(len(s)):
            char = s[i]
            if len(stack) == 0 or char in sym:
                stack.append(char)
                continue
            removed = stack.pop()
            if not ((removed == "(" and char == ")") or (removed == "[" and char == "]") or (removed == "{" and char == "}")):
                return False
        return len(stack) == 0

Solution = Solution()
print(Solution.isValid("()[]{}"))