class solution:
    def containsDuplicate(self, nums: list[int]) ->bool:
        setVar = set()
        for i in nums:
            if i in setVar:
                return True
            else:
                setVar.add(i)
        return False
    
solution = solution()
print(solution.containsDuplicate([1, 2, 3]))