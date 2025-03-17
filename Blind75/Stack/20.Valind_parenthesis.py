class Solution:
    def isValid(self, s:str) -> bool:
        sym = ("(", "[", "{")
        stack = []
        for i in range(len(s)):
            char = s[i]
            if len(stack) == 0 or char in sym:
                stack.append(char)
                continue
            elif (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{") or (char == ")" and stack[-1] == "("):
                stack.pop()
            else: 
                return False
            
        return len(stack) == 0

Solution = Solution()
print(Solution.isValid("(])"))