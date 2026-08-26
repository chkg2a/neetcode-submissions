class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        highest = 0
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            if summ < 0:
                summ = 0
            highest = max(highest,summ)

        return highest
