class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        print("List")
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False

solution = Solution()
print(solution.containsDuplicate([1, 2, 3]))