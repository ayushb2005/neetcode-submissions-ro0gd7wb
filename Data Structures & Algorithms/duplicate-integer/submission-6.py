class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setFromNums = set()
        for i in nums:
            if i in setFromNums:
                return True
            else:
                setFromNums.add(i)
        return False