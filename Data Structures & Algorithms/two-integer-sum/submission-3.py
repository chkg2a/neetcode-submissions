class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(nums):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            if hashMap[target-nums[i]] == nums[i]:
                return [hashMap[target-nums[i]],i]
        return []