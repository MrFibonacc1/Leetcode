class Solution:
    def productExceptSelf(self, nums:list[int]) ->list[int]:
        n = len(nums)
        preRun = 1
        result = [1] * n
        for i in range(n):
            result[i] = preRun
            preRun *= nums[i]
        postRun = 1
        for i in range(n-1,-1,-1):
            result[i]*=postRun
            postRun*=nums[i]
        return result

Solution = Solution()
print(Solution.productExceptSelf([-1,1,0,-3,3]))
