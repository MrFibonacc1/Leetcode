#Finished in 5 min

class Solution:
    def search(self, nums:list[int], target:int)->int:
        startIndex = 0
        endIndex = len(nums)-1

        while endIndex >= startIndex:
            midpoint = startIndex + (endIndex-startIndex)//2
            midpointValue = nums[midpoint]

            if midpointValue == target:
                return midpoint
            elif midpointValue>target:
                endIndex = midpoint - 1
            elif midpointValue < target:
                startIndex = midpoint + 1
            
        return -1