class Solution:
    def topKFrequent(self, nums:list[int], k:int) ->list[int]:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i]+=1
        top_3_keys = [key for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True)[:k]]

        return top_3_keys

Solution = Solution()
print(Solution.topKFrequent([1,2,3,3,3,3,4,4,1,1,1,1,1,11,1],3))