class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i,seen[target-nums[i]]]
            if nums[i] not in seen:
                seen[nums[i]] = i 
            
Solution = Solution()
print(Solution.twoSum([1,2,3],5))