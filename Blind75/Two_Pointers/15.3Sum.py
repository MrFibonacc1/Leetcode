class Solution:
    def threeSum(self, nums:list[int]) ->list[list[int]]:
        result = []
        dict = {}
        set = ()
        n = len(nums)
        for i in n:
            lp = i+1
            rp = n - 1
            while lp < i and rp > i:
                if nums[i] + nums[lp] + nums[rp] == 0:
                    t = tuple(nums[i],nums[lp],nums[rp])
                    if t not in set:
                        set.add(t)
                        continue
                
                    
