class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        highest = nums[0]
        summ = 0
        for j in range(len(nums)):
            if summ < 0:
                summ = 0
            summ += nums[j]
            highest = max(highest,summ)

        return highest

