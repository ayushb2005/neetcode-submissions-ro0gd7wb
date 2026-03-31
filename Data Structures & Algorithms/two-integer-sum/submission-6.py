class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a hashmap to keep track of key (index value), value (index)
        #if target - current is in hashmap return those index's
        numsMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                return [numsMap[target-nums[i]],i]
            else:
                numsMap[nums[i]] = i
        return []