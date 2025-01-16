class Solution:
    def maxArea(self, height:list[int]) ->int:
        highest = 0
        n = len(height)-1
        lp = 0
        rp = n
        while lp < rp:
            minNum = min(height[lp],height[rp])
            if minNum*n > highest:
                highest = minNum*n
            if height[lp] < height[rp]:
                lp +=1
                n -= 1
            elif height[lp] > height[rp]:
                rp-=1
                n-=1
            else:
                rp-=1
                lp+=1
                n-=2
        return highest
            
Solution = Solution()
print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))