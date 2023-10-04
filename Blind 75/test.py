class Solution:
    def maxArea(self, height: list[int]) -> int:
       left = 0
       right = len(height)-1
       maxArea = 0 
       while left<right:
            value = min(height[left],height[right]) * right-left
            maxArea = max(value,maxArea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
       return maxArea    
        
solution = Solution()

# Test cases
result1 = solution.maxArea([4,4,9,1,9])
print(result1)
