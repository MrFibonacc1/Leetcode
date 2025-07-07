class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        hash = {}

        for index, val in enumerate(nums):
            if target - val in hash:
                return [index, hash[target-val]]
            hash[val] = index
        return [0,0]
