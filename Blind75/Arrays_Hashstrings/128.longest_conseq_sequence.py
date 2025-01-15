class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        count = set(nums) 
        longest = 0

        for num in count:
            if num - 1 not in count:
                current_num = num
                streak = 1

                while current_num + 1 in count:
                    current_num += 1
                    streak += 1

                longest = max(longest, streak)

        return longest

Solution = Solution()
print(Solution.longestConsecutive([100,4,200,1,3,2]))