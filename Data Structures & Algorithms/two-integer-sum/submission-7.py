class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if( need in hashMap):
                return [hashMap[need], i]
            else:
                hashMap[nums[i]] = i
        return []