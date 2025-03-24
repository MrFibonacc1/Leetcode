class Solution:
    def dailyTemperatures(self, temperatures: list[int]) ->list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for index, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                i, num = stack.pop()
                answer[i] = index - i
            stack.append([index,val]) 
        return answer

Solution = Solution()
print(Solution.dailyTemperatures([73,74,75,71,69,72,76,73]))