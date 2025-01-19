class Solution:
    def maxProfit(self, prices:list[int])->int:
        if len(prices) <= 1:
            return 0
        maxProfit = 0
        n = len(prices)-1
        lp = 0
        rp = 1
        for i in range(len(prices)-1):
            if lp > n or rp > n:
                break

            if prices[lp] > prices[rp]:
                lp = rp
                rp+=1
            else:

                maxProfit = max(maxProfit, prices[rp]-prices[lp])
                rp+=1
        return maxProfit
    
Solution = Solution()
print(Solution.maxProfit([2,1,2,1,0,1,2]))