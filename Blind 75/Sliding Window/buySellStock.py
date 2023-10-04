class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        start = 0
        end = 1
        while end<len(prices):
            if prices[start]<prices[end]:
                profit = prices[end]-prices[start]
                maxProfit = max(maxProfit,profit)
            else:
                start=end
            end+=1

        return maxProfit

#[7,1,5,3,6,4]
solution = Solution()

# Test cases
result1 = solution.maxProfit([7,1,5,3,6,4])
print(result1)
